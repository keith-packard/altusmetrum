.SUFFIXES: .5c .py .fp

DIRS= \
	diodes \
	jst \
	molex \
	pinheader \
	switches \
	tyco

FOOTPRINTS= \
	MS5607.fp \
	uson-8.fp \
	wson6x5.fp \
	hvqfn33.fp \
	ZX62-B-5PA.fp \
	TDK_PS12.fp \
	ABM3B.fp \
	1212-8.fp \
	AN3111.fp \
	lqfp48.fp \
	lqfp64.fp \
	lqfp100.fp \
	LPCC16.fp \
	MPU6000.fp \
	UBLOX-MAX.fp \
	TI-QFN32.fp \
	NDK32.fp \
	sma-edge.fp \
	MO-220.fp \
	8ufson2x2.fp

.5c.fp:
	nickle $*.5c > $@

.py.fp:
	python $*.py > $@

BUILDDIRS=$(DIRS:%=build-%)
CLEANDIRS=$(DIRS:%=clean-%)

all: $(BUILDDIRS) $(FOOTPRINTS) .gitignore
$(DIRS): $(BUILDDIRS) 
$(BUILDDIRS): 
	$(MAKE) -C $(@:build-%=%)

$(CLEANDIRS):
	$(MAKE) -C $(@:clean-%=%) clean

clean: $(CLEANDIRS)
	rm -f $(FOOTPRINTS)

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(BUILDDIRS)
.PHONY: subdirs $(CLEANDIRS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@

