#!usr/bin/env python

from md import MD
from os.path import basename, isfile, splitext
from reveal import Reveal
import argparse
import sys

def execute(argv=None):
    if argv is None:
        argv = sys.argv[1:] or ['-h']
    parser = argparse.ArgumentParser(description='convert markdown file to reveal.js html page')
    parser.add_argument('markdown_file', help='the markdown file')
    parser.add_argument('-m', '--theme', help='the reveal.js theme')
    parser.add_argument('-t', '--title', help='the html title')
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
        print "Generating"
        title = args.title or basename(splitext(md)[0])
        out = args.outfile or (title+".html")
        m = MD(md)
        r = Reveal(m.dump_sections(title), theme)
        r.generate(out, title)
        print "Finish, you can find it at [{}]".format(out)

if __name__ == '__main__':
    execute()
