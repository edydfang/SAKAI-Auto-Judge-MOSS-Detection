#!/usr/bin/env python3
from threading import Thread
import logging
import os
from bs4 import BeautifulSoup
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def add_encoding_header(soup):
    if soup.meta is None or soup.meta.get('charset') is None:
        charset_tag = soup.new_tag("meta", charset="utf-8")
        soup.head.append(charset_tag)
    return soup


def read_index_file(filename):
    filed = open(filename)
    html = filed.read()
    basename = os.path.basename(filename)
    return html, basename


def read_network_html(url):
    logging.debug("Processing URL: " + url)
    response = urlopen(url)
    html = response.read()
    basename = os.path.basename(url)
    return html, basename


def process_url(url, urls, base_url, path):
    html, basename = read_network_html(url)
    process_html(html, basename, urls, base_url, path)


def process_html(html, file_name, urls, base_url, path):
    soup = BeautifulSoup(html, 'lxml')
    # Not file name eg. 123456789 or is None
    if not file_name or len(file_name.split(".")) == 1:
        file_name = "index.html"
    for more_url in soup.find_all(['a', 'frame']):
        if more_url.has_attr('href'):
            link = more_url.get('href')
        else:
            link = more_url.get('src')

        if link and (link.find("match") != -1):  # Download only results urls
            link_components = link.split('#')  # remove fragment from url
            anchor = None
            if len(link_components) > 1:
                anchor = link_components[1]
            link = link_components[0]
            basename = os.path.basename(link)

            if basename == link:  # Handling relative urls
                link = base_url + basename
            # add anchor
            if anchor:
                basename = "%s#%s" % (basename, anchor)
            if more_url.name == "a":
                more_url['href'] = basename
            elif more_url.name == "frame":
                more_url['src'] = basename

            if link not in urls:
                urls.append(link)

    f = open(path + file_name, 'w')
    soup = add_encoding_header(soup)
    f.write(str(soup))  # saving soup will save updated href
    f.close()


def retrive_report(indexfile, base_url, connections=4, log_level=logging.DEBUG):
    logging.basicConfig(level=log_level)
    path = os.path.dirname(indexfile) + '/'
    if not os.path.exists(indexfile):
        raise Exception("Index file not exists.")
    html, basename = read_index_file(indexfile)
    urls = []
    threads = []
    base_url = base_url + '/'
    process_html(html, basename, urls, base_url, path)
    multi_threading(urls, base_url, path, threads, connections)


def download_report(url, path, connections=8, log_level=logging.DEBUG):
    logging.basicConfig(level=log_level)
    if len(url) == 0:
        raise Exception("Empty url supplied")

    if not os.path.exists(path):
        os.makedirs(path)

    base_url = url + "/"
    urls = [url]
    threads = []
    multi_threading(urls, base_url, path, threads, connections)


def multi_threading(urls, base_url, path, threads, connections):
    logging.debug("=" * 80)
    logging.debug("Downloading Moss Report")
    logging.debug("=" * 80)

    # Handling thread
    for url in urls:
        t = Thread(target=process_url, args=[url, urls, base_url, path])
        t.start()
        threads.append(t)

        if len(threads) == connections or len(urls) < connections:
            for thread in threads:
                thread.join()
                threads.remove(thread)
                break

    logging.debug("Waiting for all threads to complete")
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    retrive_report("./judge/report/lab9/index.html",
                   "http://moss.stanford.edu/results/86775130")
