#!/usr/bin/env python3

import csv
import random
import string


def gen_password():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))


def gen_account_data(student_list):
    account_data = list(student_list)
    for idx, _ in enumerate(account_data):
        account_data[idx].insert(1, gen_password())
    return account_data


def save_account_data(account_data, filename):
    output = open(filename,mode='w')
    csvwriter = csv.writer(output)
    csvwriter.writerows(account_data)
    output.close()


def read_student_list(list_file):
    student_list = []
    csvfile = open(list_file)
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        student_list.append(row)
    csvfile.close()
    return student_list


def main():
    student_list = read_student_list("list.csv")
    account_data = gen_account_data(student_list)
    save_account_data(account_data, "output.csv")
    print("Done")


if __name__ == '__main__':
    main()
