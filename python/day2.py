#!/usr/bin/env python3
# day2.py

import sys

if (len(sys.argv) - 1 < 1):
    print("Usage: day2.py INPUT_FILE [TARGET_OUTPUT]")
    exit(1)

def calc(opcode_list, noun=12, verb=2):
    list = opcode_list.copy()

    list[1] = noun
    list[2] = verb

    i = 0
    while i < len(list):
        opcode = list[i]
        if opcode == 1:
            list[list[i + 3]] = list[list[i+1]] + list[list[i + 2]]
        elif opcode == 2:
            list[list[i + 3]] = list[list[i+1]] * list[list[i + 2]]
        elif opcode == 99:
            break
        else:
            print("Unknown opcode {} @ {}. Malformed input?".format(opcode, i))
            exit(1)
        i += 4

    return list[0]

def search(opcode_list, target):
    for n in range(100):
        for v in range(100):
            if calc(opcode_list, n, v) == target:
                return [n, v]
    return []

def main():
    input_file = sys.argv[1]

    f = open(input_file, "r")
    opcode_list = f.readline().rstrip().split(',')
    opcode_list = list(map(int, opcode_list))

    print("Part 1 answer: {}".format(calc(opcode_list)))

    if (len(sys.argv) == 3):
        target_output = int(sys.argv[2])
        solution = search(opcode_list, target_output)

        if (len(solution) < 2):
            print("Part 2 answer not found. Malformed input?")
        else:
            noun, verb = solution
            print("Part 2 answer: {}".format(100 * noun + verb))

if __name__ == "__main__":
    main()