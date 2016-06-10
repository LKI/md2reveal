#!/bin/sh

SRC=`eval dirname $0`
DEST=${1-"md2reveal"}
ln -sf "$SRC/md2reveal/cmdline.py" $DEST
