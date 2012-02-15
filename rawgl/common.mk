PYTHON:=/usr/bin/env python
GCCXML:=$(shell which gccxml) # www.gccxml.org
XML2PY:=$(shell which xml2py.py) # pypi.python.org/pypi/ctypeslib/

RAW:=$(TARGET:.py=.raw)
PPHEADER:=$(TARGET:.py=.pp)
XML:=$(TARGET:.py=.xml)

.PHONY: all clean purge

all: $(TARGET)

$(RAW): $(XML)
	$(PYTHON) $(XML2PY) $^ -o $@ -l $(LIBRARY) -d -k amdefst -r 'gl(ut?)?[A-Z].*' -r 'GL(UT?)?_[A-Z].*' -r 'GL(UT?)?[a-z].*'

$(XML): $(PPHEADER)
	$(GCCXML) $(DEFINITIONS) $^ -fxml=$@

$(PPHEADER): $(HEADER)
	cat $^ > $@
	$(GCCXML) $(DEFINITIONS) -E -dM $^ | sort | sed -n \
		-e '/^#define [^ ]*\s*$$/d' \
		-e 's/^#define \([^ ]*\) \([^ ]*\)/#undef \1\nconst unsigned int \1 = \2;/g' \
		-e '/GL\(UT\?\)\?_[_A-Z0-9]* = \(0[xX]\)\?[0-9a-fA-F]*;/p' \
		>> $@

clean:
	@rm -f $(XML) $(PPHEADER) $(RAW) *~ *.pyc

purge:
	@rm -f $(TARGET) $(XML) $(PPHEADER) $(RAW) *~ *.pyc

