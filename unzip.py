#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
This is a prototype for Assignment grading automatation
'''
import zipfile
import sys
import os
import errno
from pathlib import Path

def mkdir(dirname):
    '''
    Test and make new directory if not exists
    '''
    if not os.path.exists(dirname):
        try:
            os.makedirs(dirname)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise


def unzip(file, encoding, verbose):
    '''
    unzip a zip file
    '''
    with zipfile.ZipFile(file) as zipf:
        for filename in zipf.namelist():
            if verbose:
                print(filename)
            path = Path(filename,encoding = encoding)
            if filename[-1] == '/':
                mkdir(filename)
            else:
                mkdir(str(path.parent))
                with path.open('wb') as wf:
                    wf.write(zipf.read(filename))

if __name__ == '__main__':
    for i in sys.argv[1:]:
        unzip(i, 'utf-8', 1)
