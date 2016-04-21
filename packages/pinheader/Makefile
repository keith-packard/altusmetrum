FOOTPRINTS = \
	50mil4pin.fp \
	50mil5pin.fp \
	2mm2pin.fp

all: $(FOOTPRINTS) .gitignore

50mil4pin.fp:	50milpitch.py
	./50milpitch.py 4 > 50mil4pin.fp

50mil5pin.fp:	50milpitch.py
	./50milpitch.py 5 > $@

2mm2pin.fp: 2mmpitch.5c
	nickle 2mmpitch.5c -o $@ 2

clean:
	rm -f $(FOOTPRINTS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@
