#! /bin/bash

IN_PATH="../intro_to_programming_msobczak/komplemenciarz.ipynb"
OUT_PATH="/home/carrot/notebooks/komplemenciarz.ipynb"

for i in {1..24}
do
    bash -c "docker cp $IN_PATH carrot$i:$OUT_PATH"
done
