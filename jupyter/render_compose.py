# -*- coding: utf-8 -*-

import yaml
from notebook.auth import passwd


passwords = []
for i in range(1, 25):
    passwords.append(passwd("karotki{}".format(i)))


def render():
    volumes = {}
    services = {}
    with open("./docker-compose.yml", "w") as f:
        for i, password in enumerate(passwords):
            num = i + 1

            volume = "carrot_notebook_vol_{}".format(num)
            volumes[volume] = {}
            services.setdefault('notebook-{}'.format(num), {
                "image": "carrot",
                "container_name": "carrot{}".format(num),
                "build": {
                    "context": ".",
                    "dockerfile": "./notebook.dockerfile",
                },
                "command": "/home/carrot/run.sh",
                "ports": ["{port}:8888".format(port=8000 + num)],
                "environment": {
                    "PASSWORD": password
                },
                "restart": "always",
                "user": "carrot",
                "volumes": ["{vol}:/home/carrot/notebooks".format(vol=volume)]
            })

        f.write(yaml.dump({
            "version": "2",
            "services": services,
            "volumes": volumes,
        }, default_flow_style=False))


if __name__ == '__main__':
    render()
