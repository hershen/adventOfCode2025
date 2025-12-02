#!/home/hershen/venvs/jupyter/bin/python

import copy
import sys
from collections import defaultdict
import math
import pdb;

sys.setrecursionlimit(10000)

DEBUG = False

def main():
    if len(sys.argv) < 2:
        print("Please enter input filename")
        return

    filename = sys.argv[1]
    with open(filename, "r") as f:
        lines = f.readlines()

    current = 50
    zero_count = 0
    passes_zero = 0

    for line in lines:
        clicks = int(line[1:])
        print(clicks)
        if line[0] == 'R':
            for i in range(clicks):
                current += 1
                if current == 100:
                    current = 0
                passes_zero += current == 0
        else:
            for i in range(clicks):
                current -= 1
                if current == -1:
                    current = 99
                passes_zero += current == 0
        zero_count += current == 0
#        print(line, current)

    print(f"Number of zeros : {zero_count}")
    print(f"Passed through zero : {passes_zero}")
    # for part 2


            #while current < 0:
            #    print(f"line = {line[:-1]}, current = {current}, passes_zero = {passes_zero}", end='')
            #    current += 100
            #    passes_zero +=1
            #    print(f",||| current = {current}, passes_zero = {passes_zero}")


if __name__ == "__main__":
    main()
