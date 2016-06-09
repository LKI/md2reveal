#!usr/bin/env python

from md import MD
from os.path import basename, isfile, splitext
import argparse
import sys

def execute(argv=None):
    if argv is None:
        argv = sys.argv[1:]
    parser = argparse.ArgumentParser(description='convert markdown file to reveal.js html page')
    parser.add_argument('markdown_file', help='the markdown file')
    parser.add_argument('-t', '--theme', help='the reveal.js theme')
    parser.add_argument('-o', '--outfile', help='output file name')
    args   = parser.parse_args(argv)
    md     = args.markdown_file
    theme  = args.theme or 'black'
    themes = ['beige', 'black', 'blood', 'league', 'moon', 'night', 'serif', 'simple', 'sky', 'solarized', 'white']
    if theme not in themes:
        print theme, "is not a valid theme"
        print "These are the valid themes:", themes
    elif not isfile(md):
        print md, "is not a file."
        exit(1)
    else:
        out = args.outfile or (basename(splitext(md)[0])+".html")
        m = MD(md)
        for l in m.dump_reveal():
            print l,

if __name__ == '__main__':
    execute(argv=['-h'])
