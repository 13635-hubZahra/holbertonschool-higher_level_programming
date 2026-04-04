#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) - 1
    total = 0
    for i in range(1, count + 1):
        total += int(sys.argv[i])
    print("{:d}".format(total))
