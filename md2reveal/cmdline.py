#!/usr/bin/env python

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
    parser.add_argument('-q', '--qrcode', help='add qrcode as last section', action='store_true')
    parser.add_argument('-l', '--qrurl',  help='the qrcode url')
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
        print "Generating [{}]".format(out)
        m = MD(md)
        if args.qrcode:
            m.set_qr_url(args.qrurl or 'window.location.href')
        r = Reveal(m.dump_sections(), theme)
        r.generate(out, args.title or basename(splitext(md)[0]))
        print "Finish, you can find it at [{}]".format(out)

if __name__ == '__main__':
    execute()
