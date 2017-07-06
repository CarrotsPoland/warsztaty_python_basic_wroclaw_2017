#! /bin/bash

/home/carrot/.venv/bin/jupyter notebook \
    --ip 0.0.0.0 \
    --port=8888 \
    --allow-root \
    --no-browser \
    --NotebookApp.notebook_dir=/home/carrot/notebooks \
    --NotebookApp.password=$PASSWORD
