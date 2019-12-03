#!/usr/bin/env python3
# day3.py
import sys

def main():
    if (len(sys.argv) - 1 < 1):
        print("Usage: day3.py INPUT_FILE")
        exit(1)

    wire_id = 0
    coordinates = {}
    collisions = []

    with open(sys.argv[1]) as f:
        for wire in f:
            x = 0
            y = 0

            instructions = wire.rstrip().split(',')

            for instruction in instructions:
                direction = instruction[:1]
                length = int(instruction[1:])

                for i in range(length):
                    if direction == 'L':
                        x -= 1
                    if direction == 'R':
                        x += 1
                    if direction == 'D':
                        y += 1
                    if direction == 'U':
                        y -= 1
                    
                    coords = "{},{}".format(x, y)
                    if coords in coordinates:
                        if coordinates[coords] != wire_id:
                            collisions.append([x, y])
                    else:
                        coordinates[coords] = wire_id
            wire_id += 1

    shortest_dist = -1
    for collision in collisions:
        dist = abs(collision[0]) + abs(collision[1])
        if shortest_dist == -1 or dist < shortest_dist:
            shortest_dist = dist
    print("Part 1 answer: {}".format(shortest_dist))

if __name__ == "__main__":
    main()