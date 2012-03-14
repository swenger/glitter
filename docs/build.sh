#!/bin/sh

epydoc -v --html -o api ../glitter ../examples ../tests

mkdir -p examples

DOCDIR=`pwd`
cd ..
for i in examples/*.py; do
	python -m mylit $i $DOCDIR/${i%.py}.html
done
cd -

cp ../examples/pygments_style.css examples
rm examples/__init__.html

python build_index.py

