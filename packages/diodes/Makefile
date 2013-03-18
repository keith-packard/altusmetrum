.SUFFIXES: .5c .py .fp

FOOTPRINTS = \
	powerdi123.fp

.5c.fp:
	nickle $*.5c > $@

.py.fp:
	python $*.py > $@

all: $(FOOTPRINTS) .gitignore

clean:
	rm -f $(FOOTPRINTS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@