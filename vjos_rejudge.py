#!/usr/bin/env python3
# -*- coding=utf-8 -*-

import requests
from lxml import etree


def main():
    cookies = input("Your webs ite Cookies value for [sid]:")
    # 5aa26098e1382365c391f638
    contest_id = input("Contest Id:")
    # 5a9e7aa8e1382347d8bc0c33
    problem_id = input("Problem Id:")
    print("Rejudging......")
    # sid=xxxx
    cookies = dict(sid=cookies)
    url_prefix = 'https://adoj.sustc.edu.cn/d/CS208/records'
    url = url_prefix + \
        '?uid_or_name=&pid={0}&tid={1}'.format(problem_id, contest_id)

    while True:
        response = requests.get(url, cookies=cookies)
        tree = etree.HTML(response.text)
        id_list = tree.xpath(r"/html/body/div//div/table/tbody/tr/@data-rid")
        if len(id_list) < 1:
            break
        else:
            for rid in id_list:
                print("id: {0}".format(rid))
                token = dict(csrf_token=tree.xpath(
                    r"/html/body/div//div/table/tbody/tr[1]//form/input/@value")[0])
                result = post_for_rejudge(rid, cookies, token)
                print(result)
        next_page = tree.xpath(
            r"/html/body//a[contains(@class, 'next')]/@href")[0]
        url = url_prefix + next_page
    # print(response.text)


def post_for_rejudge(rid, cookies, token):
    resp = requests.post('https://adoj.sustc.edu.cn/records/{0}/rejudge'.format(rid), cookies=cookies, data=token)
    return resp.status_code

if __name__ == '__main__':
    main()
