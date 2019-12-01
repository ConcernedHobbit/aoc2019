#!/bin/bash
# day1.sh

if [ $# -lt 1 ]; then
    echo "Usage: ./day1.sh INPUT_FILE"
    exit 1
fi

while read line
do
    (( sum+=($line/3-2) ))
done < "$1"

echo $sum