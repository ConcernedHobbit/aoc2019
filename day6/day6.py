#!/usr/bin/env python3
# day6.py

# this is ugly.
import sys

def main():
    if (len(sys.argv) - 1 < 1):
        print("Usage: day6.py INPUT_FILE")
        exit(1)

    f = open(sys.argv[1], 'r')
    orbits = {}
    for line in f:
        (orbiting, name) = line.rstrip().split(')')
        orbits[name] = orbiting

    num_orbits = 0
    for orbiter in orbits.keys():
        while orbiter in orbits:
            num_orbits = num_orbits + 1
            orbiter = orbits[orbiter]

    print("Part 1 answer: {}".format(num_orbits))

    you_distances = {}
    san_distances = {}

    you_orbiter = 'YOU'
    num_you = 0
    while you_orbiter in orbits:
        next_orbiter = orbits[you_orbiter]
        you_distances[next_orbiter] = num_you
        num_you = num_you + 1
        you_orbiter = next_orbiter

    san_orbiter = 'SAN'
    num_san = 0
    while san_orbiter in orbits:
        next_orbiter = orbits[san_orbiter]
        san_distances[next_orbiter] = num_san
        num_san = num_san + 1
        san_orbiter = next_orbiter

    you_set = set(you_distances)
    san_set = set(san_distances)

    common_orbits = you_set.intersection(san_set)
    min_dist = -1
    for common_orbit in common_orbits:
        dist = you_distances[common_orbit] + san_distances[common_orbit]
        if min_dist == -1 or dist < min_dist:
            min_dist = dist

    print("Part 2 answer: {}".format(min_dist))

if __name__ == "__main__":
    main()