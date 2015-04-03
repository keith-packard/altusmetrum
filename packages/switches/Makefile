.SUFFIXES: .5c .py .fp

FOOTPRINTS = \
	20571.fp \
	cus-12.fp \
	lph.fp

.5c.fp:
	nickle $*.5c > $@

.py.fp:
	python $*.py > $@

all: $(FOOTPRINTS) .gitignore

$(FOOTPRINTS): ../footprint.5c

clean:
	rm -f $(FOOTPRINTS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@
