#!/usr/bin/env python3

from string import Template
# import the smtplib module. It should be included in Python by default
import requests
import csv


def read_template(filename):
    with open(filename, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


def send_account_info(accountfile, messagefile):
    account_list = read_accout_list(accountfile)
    message_temp = read_template(messagefile)
    for account in account_list:
        if len(account) < 1:
            return
        uid = account[0]
        username = uid #account[2]
        password = account[1]
        email = '%s@mail.sustc.edu.cn' % uid
        print(username, password, email)
        body = message_temp.substitute(ACCOUNT=username, PASSWORD=password)
        send_email(email, body)


def read_accout_list(filename):
    account_list = None
    with open(filename, encoding='utf-8') as accountf:
        reader = csv.reader(accountf)
        account_list = list(reader)
    return account_list


def send_email(recipient, body):
    # mailgun
    key = 'key-ec'
    sandbox = 'oj.sustc.space'

    request_url = 'https://api.mailgun.net/v3/{0}/messages'.format(sandbox)
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'SUSTech OJ <noreply@oj.sustc.space>',
        'to': recipient,
        'subject': 'Hello',
        'text': body
    })

    print('Status: {0}'.format(request.status_code))
    print('Body:   {0}'.format(request.text))


def main():
    send_account_info('student_list.csv', 'message.txt')
    # send_email('fangyd1997@outlook.com', 'Hello from Mailgun\nBest regards')


if __name__ == '__main__':
    main()
