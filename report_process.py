#!/usr/bin/env python3
# -*- coding=utf-8 -*-
'''
This script is used to download the moss report and process it for a better output
'''
import logging
import re

try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen
import mosspy
import argparse
from bs4 import BeautifulSoup


def filter_report_cate(report_url):
    logging.debug("Filtering URL: " + report_url)
    response = urlopen(report_url)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    soup = add_encoding_header(soup)
    allrows = soup.find_all("tr")[1:]
    for row in allrows:
        tds = row.find_all("td")[0:2]
        results = list()
        for td in tds:
            # print(td)
            result = get_studentId_percentage(td.a.text)
            results.append(result)
        if results[0][0] == results[1][0]:
            row.decompose()
        else:
            for idx, td in enumerate(tds):
                td.a.string = "ID: %s, Percentage: (%s%%)" % results[idx]
            print(results)
    return soup.prettify(formatter="html")


def add_encoding_header(soup):
    if soup.meta is None or soup.meta.get('charset') is None:
        charset_tag = soup.new_tag("meta", charset="utf-8")
        soup.head.append(charset_tag)
    return soup


def get_studentId_percentage(rawtext):
    '''
    return the studentId matched by file name
    '''
    rawtext = rawtext.strip()
    regex_id = r'11[2-6][1|2][0-3][0-9]{3}'
    regex_percentage = r'\((\d{1,2})\%\)$'
    match_id = re.search(regex_id, rawtext)
    match_percentage = re.search(regex_percentage, rawtext)
    std_id = None
    percentatge = 0
    if match_id:
        std_id = match_id.group()
    if match_percentage:
        percentatge = match_percentage.group(1)
    return std_id, percentatge


def download_report(report_url):
    '''
    download all reports from the server for offline usage
    '''
    mosspy.download_report(report_url, "./judge/report/", connections=8)


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('-l', metavar='Base URL of the report', type=str, required=True,
                        help='The URL of the report')
    parser.add_argument('-o', metavar='location downloaded index file', type=argparse.FileType(mode='w+'), required=True,
                        help='The location of the report files')
    args = parser.parse_args()
    # download_report("http://moss.stanford.edu/results/813904023/")
    filtered_report = filter_report_cate(args.l)
    filed = args.o
    filed.write(filtered_report)
    filed.close()


if __name__ == '__main__':
    main()
