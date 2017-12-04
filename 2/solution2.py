#!/usr/local/bin/python

import csv

# with open('input2.txt') as tsvin:
with open('input.txt') as tsvin:
    tsvin = csv.reader(tsvin, delimiter="\t",)

    checksum = 0
    for row in tsvin:
        row_result = None

        for i in range(len(row) - 1):
            val = int(row[i])

            for j in range(i + 1, len(row)):
                val2 = int(row[j])

                big = max(val, val2)
                small = min(val, val2)

                if big % small == 0:
                    row_result = big / small
                    break

            if row_result:
                break

        checksum += row_result


print checksum