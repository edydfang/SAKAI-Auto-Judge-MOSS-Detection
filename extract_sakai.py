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
    '''
    check whethter the file is an compressed file
    '''
    if re.match(r".+\/[^\/]+\.(7z|zip|rar|tar\.gz)$", filename) is not None:
        return True
    return False

def eliminate_whitespace(directory):
    '''
    eliminate all whitespaces in filenames or direnames
    '''
    for root, dirs, files in os.walk(directory, topdown=False):
        for name in dirs:
            if ' ' in name:
                new_name = name.replace(" ", "_")
                print(name, new_name)
                shutil.move(os.path.join(root, name), os.path.join(root, new_name))
        for name in files:
            if ' ' in name:
                new_name = name.replace(" ", "_")
                print(name, new_name)
                shutil.move(os.path.join(root, name), os.path.join(root, new_name))

def recursively_extract(directory):
    '''
    recursively extract all files in a compressed file
    '''
    for root, _, files in os.walk(directory, topdown=False):
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
    recursively_extract("./judge")
    eliminate_whitespace("./judge")

if __name__ == "__main__":
    main()

