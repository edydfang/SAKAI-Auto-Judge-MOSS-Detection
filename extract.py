#!/usr/bin/env python3
# -*- coding=utf-8 -*-
'''
This program is to extract all file downloaded from SAKAI
Assignment Section recursively
'''
import argparse
import logging
import shutil
import os
import errno
import re
import sys
import patoolib
import patoolib.util

def is_compressed_file(filename):
    if re.match(r".+\/[^\/]+\.(7z|zip|rar)$", filename) is not None:
        return True
    return False

def eliminate_whitespace():
    for root, dirs, files in os.walk("./judge", topdown=False):
        for name in dirs:
            if ' ' in name:
                new_name = name.replace(" ", "_")
                print(name, new_name)
                shutil.move(os.path.join(root, name), os.path.join(root, new_name))

def recursively_extract():
    for root, dirs, files in os.walk("./judge", topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            if is_compressed_file(filename):
                try:
                    patoolib.extract_archive(
                        filename, outdir=root, verbosity=0, interactive=False)
                except:
                    print('Error extracting:', filename, file=sys.stderr)
                    input("Press Enter to continue...")
                print(filename)
                os.remove(filename)
        # for name in dirs:
        #     print(os.path.join(root, name))

def main():
    '''
    argument parsing
    '''
    parser = argparse.ArgumentParser(
        description='SAKAI Bulk file judging')
    parser.add_argument('filename', type=argparse.FileType('r'),
                        help='filename for the bulk file')
    args = parser.parse_args()
    try:
        os.makedirs('./judge')
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise
    patoolib.extract_archive(
        args.filename.name, outdir='./judge', verbosity=0, interactive=False)
    recursively_extract()
    eliminate_whitespace()

if __name__ == "__main__":
    main()

