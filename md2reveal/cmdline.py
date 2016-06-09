#!/usr/bin/env python

import sys
import os.path
import argparse

def execute(argv=None):
    if argv is None:
        argv = sys.argv
    parser = argparse.ArgumentParser(
        description='convert markdown file to reveal.js html page'
    )
    parser.add_argument(
        '-theme',
        help='the reveal.js theme',
    )
    parser.add_argument(
        'markdown_file',
        help='the markdown file',
    )
    themes = ['beige', 'black', 'blood', 'league', 'moon', 'night', 'serif', 'simple', 'sky', 'solarized', 'white']
    args = parser.parse_args()
    md = args.markdown_file
    if not os.path.isfile(md):
        print md, "is not a file."
        exit(1)
    else:
        print "Converting ", md
