#!/usr/local/bin/python

import csv

with open('input.txt') as tsvin:
    tsvin = csv.reader(tsvin, delimiter="\t",)

    checksum = 0
    for row in tsvin:
        maximum = minimum = int(row[0])
        for val in row:
            val = int(val)
            maximum = max(maximum, val)
            minimum = min(minimum, val)

        checksum += maximum - minimum

print checksum