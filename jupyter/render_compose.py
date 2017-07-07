# -*- coding: utf-8 -*-

import yaml


passwords = [
    "sha1:5787b99282f3:dd43b9a19dd95526d8685135da37a346c954d105",
    "sha1:ec875c41cff8:ece7d94aee0d4baa7d5c0759b5292d0325757c15",
    "sha1:9b779e22ce48:57eadfe7c462098f1e82633a5d9f0067294a1df2",
]


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
