.SUFFIXES: .5c .py .fp

FOOTPRINTS= \
	MS5607.fp \
	uson-8.fp \
	wson6x5.fp \
	hvqfn33.fp \
	ZX62-B-5PA.fp \
	TDK_PS12.fp \
	ABM3B.fp \
	1212-8.fp \
	AN3111.fp

.5c.fp:
	nickle $*.5c > $@

.py.fp:
	python $*.py > $@

all: $(FOOTPRINTS) .gitignore

clean:
	rm -f $(FOOTPRINTS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@