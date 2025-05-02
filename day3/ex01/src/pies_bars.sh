#!/bin/bash

DATA_DIR="data"
DATA_FILE="$DATA_DIR/data1.dat"

mkdir -p "$DATA_DIR"

{   
    echo "@ Pies,Bars"
    echo "2007  73.32   70.52"
    echo "2008  81.23   93.00"
    echo "2009  181.43  135.10"
    echo "2010  110.21    95.00"
    echo "2011  93.97   90.45"
} > "$DATA_FILE"



termgraph "$DATA_FILE" --color green blue 

