#!/usr/bin/env python3
# day2.py

import sys

if (len(sys.argv) - 1 < 1):
    print("Usage: day2.py INPUT_FILE [TARGET_OUTPUT]")
    exit(1)

def calc(input_file, noun=12, verb=2):
    f = open(input_file, "r")
    l = f.readline().rstrip().split(',')
    l = list(map(int, l))

    l[1] = noun
    l[2] = verb

    i = 0
    while i < len(l):
        opcode = l[i]
        if opcode == 1:
            l[l[i + 3]] = l[l[i+1]] + l[l[i + 2]]
        elif opcode == 2:
            l[l[i + 3]] = l[l[i+1]] * l[l[i + 2]]
        elif opcode == 99:
            break
        else:
            print("Unknown opcode {} @ {}. Malformed input?".format(opcode, i))
            exit(1)
        i += 4

    return l[0]

def search(target):
    for n in range(100):
        for v in range(100):
            if calc(input_file, n, v) == target:
                return [n, v]
    return []

input_file = sys.argv[1]
print("Part 1 answer: {}".format(calc(input_file)))

if (len(sys.argv) == 3):
    target_output = int(sys.argv[2])
    solution = search(target_output)

    if (len(solution) < 2):
        print("Part 2 answer not found. Malformed input?")
    else:
        noun, verb = solution
        print("Part 2 answer: {}".format(100 * noun + verb))