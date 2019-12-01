#!/bin/bash
# day1.sh

if [ $# -lt 1 ]; then
    echo "Usage: ./day1.sh INPUT_FILE"
    exit 1
fi

recursive_sum=0
simple_sum=0

while read line
do
    (( i=($line/3-2) ))
    (( simple_sum+=$i ))
    
    while [ $i -gt 0 ];
    do
        (( recursive_sum+=$i ))
        (( i=($i/3-2) ))
    done
done < "$1"

echo -e "Recursive sum: \t$recursive_sum"
echo -e "Simple sum: \t$simple_sum"