.SUFFIXES: .5c .py .fp

FOOTPRINTS= \
	MS5607.fp \
	uson-8.fp \
	wson6x5.fp \
	hvqfn33.fp

.5c.fp:
	nickle $*.5c > $@

.py.fp:
	python $*.py > $@

all: $(FOOTPRINTS)