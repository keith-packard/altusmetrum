.SUFFIXES: .5c .py .fp

FOOTPRINTS = \
	0605.fp \
	powerdi123.fp \
	topled.fp \
	2125.fp \
	0603-sideled.fp

.5c.fp:
	nickle $*.5c -o $@

.py.fp:
	python $*.py > $@

all: $(FOOTPRINTS) .gitignore

$(FOOTPRINTS): ../footprint.5c

clean:
	rm -f $(FOOTPRINTS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@
