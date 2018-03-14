#!/usr/bin/env python3

import csv
import subprocess

def main():
    accountfile = open("student_info.csv")
    csvreader = csv.reader(accountfile)
    for row in csvreader:
        print(row)
        uid = row[0]
        username = row[2]
        password = row[1]
        email = "%s@mail.sustc.edu.cn" % uid
        print(uid, username, password, email)
        subprocess.run(["python3.6","-m","vj4.model.user","add", uid, username, password, email])
    

if __name__ == '__main__':
    main()

