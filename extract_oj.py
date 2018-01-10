#!/usr/bin/env python3
'''
This program is used to extract the exported csv file forom the SUSTech OJ system
For MOSS plagirasim detection.
'''

import csv
import os


def extract_csv(filename):
    '''
    extract csv into different folders and files
    input: standard csv file
    '''
    csvfile = open(filename)
    reader = csv.reader(csvfile)
    for row in reader:
        codefile = "./data/%s/%s/%s.java" % (row[1], row[0], row[2])
        os.makedirs(os.path.dirname(codefile), exist_ok=True)
        with open(codefile, "w") as filed:
            filed.write(row[3])

def check_language(code_str):
    pass


def main():
    '''
    main
    '''
    csvfile = open('./data/oj.csv')
    valid_data = dict()
    # special escapechar
    reader = csv.reader(csvfile, delimiter=',', escapechar='\\')
    valid_record = 0
    fetch_row(reader, valid_data)
    print(valid_record)
    csvfile.close()
    with open('./data/output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(dict2list(valid_data))


def fetch_row(csv_reader, valid_data):
    '''
    csv row generator
    actually a filter
    '''
    total_record = 0
    # verbose = False
    # exception_count = 0
    for record in csv_reader:
        total_record += 1
        if len(record) == 4:
            lab_num = record[1]
            if lab_num.isdigit():
                lab_num = int(record[1])
                if lab_num > 1000 and lab_num < 1019:
                    try:
                        valid_data[record[0]][record[2]] = [record[1],record[3]]
                    except KeyError:
                        valid_data[record[0]] = dict()
                        valid_data[record[0]][record[2]] = [record[1],record[3]]

            # verbose = False
        else:
            # just ignore only 7 instance, unknown reason
            continue
            '''
            if not verbose:
                exception_count += 1
            # print("length unexpected")
            verbose = True
            '''
        '''
        if verbose:
            print(record)
        '''
    print(total_record)

def dict2list(dict_data):
    list_data = list()
    for key1, val1 in dict_data.items():
        for key2, val2 in val1.items():
            row = [key1, val2[0], key2, val2[1]]
            list_data.append(row)
    return list_data


if __name__ == '__main__':
    main()
