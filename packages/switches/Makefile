.SUFFIXES: .5c .py .fp

FOOTPRINTS = \
	cus-12.fp

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
