#!/usr/bin/env python3
# day4.py
import sys

def main():
    if (len(sys.argv) - 1 < 2):
        print("Usage: day4.py MIN MAX")
        exit(1)

    part1 = 0
    part2 = 0
    min = int(sys.argv[1])
    max = int(sys.argv[2])

    for i in range(min, max + 1):
        result = naive_check(i)
        if result[0]:
            part1 = part1 + 1

        if result[1]:
            part2 = part2 + 1

    print("Part 1 answer: {}".format(part1))
    print("Part 2 answer: {}".format(part2))

def naive_check(num): # assume num is 6-digit and within range
    part1 = False
    part2 = False

    highest = -1
    last = None
    matching_group = 0

    str_num = str(num)
    for i in range(len(str_num)):
        char = str_num[i]
        int_char = int(char)

        if int_char > highest:
            highest = int_char

        if int_char < highest:
            return [False, False]

        if last == char:
            matching_group = matching_group + 1
        
        if last != char or i == len(str_num) - 1:
            if not part1 and matching_group > 0:
                part1 = True

            if not part2 and matching_group == 1:
                part2 = True

            matching_group = 0

        last = char

    return [part1, part2]

if __name__ == "__main__":
    main()