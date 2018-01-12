#!/usr/bin/env python3
# -*- coding=utf-8 -*-
import csv


def main():
    file = open('./daas_total.csv', newline='', encoding='gbk')
    reader = csv.reader(file, delimiter=',')
    default_score = 2
    content = [line for line in reader]
    binary = True
    columnum = 4
    while True:
        student_id = int(input("Student ID:"))
        if student_id == -1:
            break
        if binary:
            score = default_score
        else:
            score = input("score")
        result = set_score(content, student_id, score)
        if result:
            print('Success, %s' % result)
        else:
            print('Not found')
    file.close()
    file = open('./daas_total.csv', mode='w', newline='', encoding='gbk')
    writer = csv.writer(file)
    writer.writerows(content)


def set_score(content, student_id, score):
    for idx, line in enumerate(content):
        if str(student_id) == line[0]:
            content[idx][4] = score
            return line[1]
    return None


if __name__ == '__main__':
    main()
