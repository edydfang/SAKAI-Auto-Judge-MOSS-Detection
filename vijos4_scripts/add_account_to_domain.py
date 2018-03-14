#!/usr/bin/env python3

import csv
import subprocess

def main():
    accountfile = open("student_info.csv")
    csvreader = csv.reader(accountfile)
    for row in csvreader:
        domainid = "CS208"
        uid = row[0]
        role = "student"
        print(domainid, uid, role)
        subprocess.run(["python3.6","-m","vj4.model.domain","add_user_role", domainid, uid, role])
    

if __name__ == '__main__':
    main()
