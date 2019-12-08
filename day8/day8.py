#!/usr/bin/env python3
# day8.py
import sys
import re

# more ugly code please disregard
# maybe i'll clean this up later
# (i won't)

def main():
    if (len(sys.argv) - 1 < 1):
        print("Usage: day8.py INPUT_FILE")
        exit(1)

    f = open(sys.argv[1], 'r')
    least_zeroes = -1
    part1 = -1
    layers = []
    image = ""
    while True:
        layer = f.read(25 * 6)
        if not layer:
            break

        zeroes = layer.count('0')
        if least_zeroes == -1 or zeroes < least_zeroes:
            least_zeroes = zeroes
            part1 = layer.count('1') * layer.count('2')

        layers.append(layer)

    for i in range(25 * 6):
        stack = [layer[i] for layer in layers]
        len_stack = len(stack)

        for j in range(len_stack):
            if stack[j] == '0':
                image += '\u2588'
                break
            if stack[j] == '1':
                image += '\u2591'
                break
            if stack[j] == '2' and j != len_stack - 1:
                continue
            image += '\u2588'


    print("Part 1 answer: {}".format(part1))
    print("Image:")
    print(re.sub("(.{25})", "\\1\n", image, 0, re.DOTALL))
if __name__ == "__main__":
    main()