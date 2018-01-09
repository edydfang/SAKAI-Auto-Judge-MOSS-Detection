#!/usr/bin/env python3
'''
This program is used to extract the exported csv file forom the SUSTech OJ system
For MOSS plagirasim detection.
'''

import csv

def main():
    csvfile = open('oj.csv') 
    reader = csv.reader(csvfile, delimiter=',',escapechar='\\')


if __name__ == '__main__':
    main()
