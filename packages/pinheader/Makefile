FOOTPRINTS = \
	50mil4pin.fp

all: $(FOOTPRINTS) .gitignore

50mil4pin.fp:	50milpitch.py
	./50milpitch.py 4 > 50mil4pin.fp

clean:
	rm -f $(FOOTPRINTS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@