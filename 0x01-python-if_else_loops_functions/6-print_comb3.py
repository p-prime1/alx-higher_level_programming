#!/usr/bin/python3
for tens in range(10):
    for unit in range(tens + 1, 10):
        print("{:02d}, ".format(tens * 10 + unit), end='')
