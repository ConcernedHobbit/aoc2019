#!/usr/bin/env python3
# day5.py
import sys

def main():
    if (len(sys.argv) - 1 < 1):
        print("Usage: day5.py INPUT_FILE")
        exit(1)

    f = open(sys.argv[1], "r")
    opcode_list = f.readline().rstrip().split(',')
    opcode_list = list(map(int, opcode_list))

    run(opcode_list)

def get_values(i, list, params, num_params=3):
    params = params.ljust(num_params, '0')
    j = 0
    return_values = []
    while j < num_params:
        value = list[i + 1 + j]
        if params[j] == '0' and j != num_params - 1:
            return_values.append(list[value])
        else:
            return_values.append(value)

        j = j + 1

    return return_values

def run(opcode_list):
    list = opcode_list[:]

    i = 0
    while i < len(list):
        op = str(list[i])
        opcode = int(op[-2:])
        params = op[0:-2][::-1]
        skip = 1

        if opcode == 1:
            skip = 4
            (a, b, to) = get_values(i, list, params)
            list[to] = a + b

        elif opcode == 2:
            skip = 4
            (a, b, to) = get_values(i, list, params)
            list[to] = a * b

        elif opcode == 3:
            skip = 2
            (to) = get_values(i, list, params, 1)[0]
            list[to] = int(input("{} < ".format(to)))

        elif opcode == 4:
            skip = 2
            (a) = get_values(i, list, params, 1)[0]
            print("{}".format(list[a]))

        elif opcode == 5:
            skip = 3
            (cond, to, _) = get_values(i, list, params, 3)
            if cond != 0:
                i = to
                continue

        elif opcode == 6:
            skip = 3
            (cond, to, _) = get_values(i, list, params, 3)
            if cond == 0:
                i = to
                continue

        elif opcode == 7:
            skip = 4
            (a, b, to) = get_values(i, list, params)
            if a < b:
                list[to] = 1
            else:
                list[to] = 0

        elif opcode == 8:
            skip = 4
            (a, b, to) = get_values(i, list, params)
            if a == b:
                list[to] = 1
            else:
                list[to] = 0

        elif opcode == 99:
            break

        else:
            print("Unknown opcode {}".format(opcode))
            exit(1)
        
        i = i + skip

if __name__ == "__main__":
    main()