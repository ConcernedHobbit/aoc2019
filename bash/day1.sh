#!/bin/bash
# day1.sh

# https://github.com/fearside/ProgressBar/
function ProgressBar {
    let _progress=(${1}*100/${2}*100)/100
    let _done=(${_progress}*4)/10
    let _left=40-$_done

    _fill=$(printf "%${_done}s")
    _empty=$(printf "%${_left}s")

    printf "\rProgress: \t[${_fill// /#}${_empty// /-}] ${_progress}%%"
}

function fuel() {
    (( i=$(echo "$1 / 3 - 2" |bc) ));
}

if [ $# -lt 1 ]; then
    echo "Usage: ./day1.sh INPUT_FILE"
    exit 1
fi

lines=$(wc -l < "$1")
recursive_sum=0
simple_sum=0
count=0

while read line
do
    fuel $line
    (( simple_sum+=$i ))
    while [ $i -gt 0 ];
    do
        (( recursive_sum+=$i ))
        fuel $i
    done
    (( count++ ))
    
    ProgressBar $count $lines
done < "$1"
echo -ne "\n"
echo -e "Recursive sum: \t$recursive_sum"
echo -e "Simple sum: \t$simple_sum"