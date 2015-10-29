AM=../altusmetrum
SCHEME=$(AM)/scheme

.SUFFIXES: .sch .pcb .ps .pdf

# need to have PROJECT defined
ifndef PROJECT
	PROJECT=undefined
endif

# if SCHEMATICS not defined, default to one sheet with project name
ifndef SCHEMATICS
	SCHEMATICS=$(PROJECT).sch
endif

CONFIG=gafrc attribs project

all:	drc partslist partslist.csv pcb

drc:	$(PROJECT).drc

$(PROJECT).drc: $(PROJECT).sch Makefile $(CONFIG)
	-gnetlist -g drc2 $(PROJECT).sch -o $@

partslist:	$(PROJECT).sch Makefile $(AM)/preferred-parts $(CONFIG)
	gnetlist -g bom -o $(PROJECT).unsorted $(SCHEMATICS)
	head -n1 $(PROJECT).unsorted > partslist
	tail -n+2 $(PROJECT).unsorted | sort | awk -f $(AM)/bin/fillpartslist >> partslist
	rm -f $(PROJECT).unsorted

partslist.csv:	$(SCHEMATICS) Makefile $(AM)/preferred-parts $(CONFIG)
	gnetlist -L $(SCHEME) -g partslistgag -o $(PROJECT).csvtmp $(SCHEMATICS)
	(head -n1 $(PROJECT).csvtmp; tail -n+2 $(PROJECT).csvtmp | sort -t \, -k 8 | awk -f $(AM)/bin/fillpartscsv ) > $@ && rm -f $(PROJECT).csvtmp

partslist.dk: partslist.csv
	$(AM)/bin/partslist-vendor --vendor digikey partslist.csv > $@

partslist-check.dk: partslist.csv
	$(AM)/bin/partslist-vendor --vendor digikey --mfg partslist.csv > $@

partslist.mouser: partslist.csv
	$(AM)/bin/partslist-vendor --vendor mouser partslist.csv > $@

partslist.other: partslist.csv
	$(AM)/bin/partslist-vendor --not-vendor digikey,mouser partslist.csv > $@

$(PROJECT)-seeed.csv: partslist.csv
	$(AM)/bin/partslist-vendor --vendor seeed partslist.csv > $@

pcb:	$(SCHEMATICS) Makefile $(CONFIG)
	gsch2pcb project

$(PROJECT).xy:	$(PROJECT).pcb $(CONFIG)
	pcb -x bom $(PROJECT).pcb

$(PROJECT).bottom.gbr:	$(PROJECT).pcb $(CONFIG)
	pcb -x gerber $(PROJECT).pcb
	@case "$(SILK)" in \
	none) 	rm -f $(PROJECT).topsilk.gbr $(PROJECT).bottom.gbr; \
		;; \
	top) 	rm -f $(PROJECT).bottomsilk.gbr; \
		;; \
	bottom) rm -f $(PROJECT).topsilk.gbr; \
		;; \
	both) \
		;; \
	*) 	echo "Invalid silk $(SILK)"; exit 1; \
		;; \
	esac

zip: $(PROJECT).zip

$(PROJECT).zip: $(PROJECT).bottom.gbr Makefile
	zip $(PROJECT).zip $(PROJECT).*.gbr $(PROJECT).*.cnc $(PROJECT).xy # $(PROJECT).xls

oshpark: $(PROJECT)-oshpark.zip

$(PROJECT)-oshpark.zip: $(PROJECT).bottom.gbr
	cp $(PROJECT).bottom.gbr bottom\ layer.ger
	cp $(PROJECT).bottommask.gbr bottom\ solder\ mask.ger
	if [ -f $(PROJECT).bottomsilk.gbr ]; then \
		cp $(PROJECT).bottomsilk.gbr bottom\ silk\ screen.ger; \
	fi
	if [ -f $(PROJECT).topsilk.gbr ]; then \
		cp $(PROJECT).topsilk.gbr top\ silk\ screen.ger; \
	fi
	cp $(PROJECT).outline.gbr board\ outline.ger
	cp $(PROJECT).top.gbr top\ layer.ger
	cp $(PROJECT).topmask.gbr top\ solder\ mask.ger
	cp $(PROJECT).plated-drill.cnc drills.xln
	if [ -f $(PROJECT).group1.gbr -a -f $(PROJECT).group2.gbr ]; then \
		cp $(PROJECT).group1.gbr internal\ plane\ 1.ger; \
		cp $(PROJECT).group2.gbr internal\ plane\ 2.ger; \
	elif [ -f $(PROJECT).group2.gbr -a -f $(PROJECT).group3.gbr ]; then \
		cp $(PROJECT).group2.gbr internal\ plane\ 1.ger; \
		cp $(PROJECT).group3.gbr internal\ plane\ 2.ger; \
	fi
	zip $(PROJECT)-oshpark.zip *.ger *.xln

seeed: $(PROJECT)-seeed.zip $(PROJECT)-seeed.csv

$(PROJECT)-seeed.zip: $(PROJECT).bottom.gbr
	cp $(PROJECT).bottom.gbr $(PROJECT).gbl
	cp $(PROJECT).bottommask.gbr $(PROJECT).gbs
	if [ -f $(PROJECT).bottomsilk.gbr ]; then \
		cp $(PROJECT).bottomsilk.gbr $(PROJECT).gbo; \
	fi
	if [ -f $(PROJECT).topsilk.gbr ]; then \
		cp $(PROJECT).topsilk.gbr $(PROJECT).gto; \
	fi
	cp $(PROJECT).outline.gbr $(PROJECT).gml
	cp $(PROJECT).top.gbr $(PROJECT).gtl
	cp $(PROJECT).topmask.gbr $(PROJECT).gts
	cp $(PROJECT).plated-drill.cnc $(PROJECT).txt
	if [ -f $(PROJECT).group1.gbr -a -f $(PROJECT).group2.gbr ]; then \
		cp $(PROJECT).group1.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group2.gbr $(PROJECT).gl3; \
	elif [ -f $(PROJECT).group2.gbr -a -f $(PROJECT).group3.gbr ]; then \
		cp $(PROJECT).group2.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group3.gbr $(PROJECT).gl3; \
	fi
	zip $(PROJECT)-seeed.zip $(PROJECT).gbl $(PROJECT).gbs $(PROJECT).gbo \
		$(PROJECT).gto $(PROJECT).gml $(PROJECT).gtl $(PROJECT).txt \
		$(PROJECT).gl2 $(PROJECT).gl3

stencil:	$(PROJECT).bottom.gbr $(PROJECT).toppaste.gbr $(PROJECT).outline.gbr
	zip $(PROJECT)-stencil.zip $(PROJECT).toppaste.gbr $(PROJECT).outline.gbr

clean:
	rm -f *.bom *.drc *.log *~ $(PROJECT).ps *.gbr *.cnc *bak* *- *.zip 
	rm -f *.net *.xy *.cmd *.png partslist partslist.csv *.ger *.xln
	rm -f *.partslist *.new.pcb *.unsorted $(PROJECT).xls muffin-5267.pdf
	rm -f $(PROJECT)-sch.ps $(PROJECT)-sch.pdf $(PROJECT)-pcb.ps $(PROJECT)-pcb.pdf
	rm -f $(PROJECT).gbl $(PROJECT).gbs $(PROJECT).gbo $(PROJECT).gto $(PROJECT).gml
	rm -f $(PROJECT).gtl $(PROJECT).gts $(PROJECT).txt $(PROJECT).gl2 $(PROJECT).gl3
	rm -f $(PROJECT)-seeed.zip $(PROJECT)-seeed.csv
	rm -f $(PROJECT)*.ps $(PROJECT)*.pdf

muffins: partslist.csv $(AM)/glabels/muffin-short-5267.glabels
	glabels-3-batch $(AM)/glabels/muffin-short-5267.glabels \
		-i partslist.csv -o muffin-5267.ps >/dev/null && \
		ps2pdf muffin-5267.ps && rm muffin-5267.ps

.sch.ps:
	gschem -p -o $*.ps -s /usr/share/gEDA/scheme/print.scm $*.sch

$(PROJECT)-sch.ps:	$(SCHEMATICS:.sch=.ps)
	psmerge -o$(PROJECT)-sch.ps $(SCHEMATICS:.sch=.ps)

$(PROJECT)-sch.pdf:	$(PROJECT)-sch.ps
	ps2pdf $(PROJECT)-sch.ps

$(PROJECT)-pcb.ps:	$(PROJECT).pcb
	pcb -x ps --psfile $(PROJECT)-pcb.ps --media Letter $(PROJECT).pcb

$(PROJECT)-pcb.pdf:	$(PROJECT)-pcb.ps
	ps2pdf $(PROJECT)-pcb.ps

pdf:	$(PROJECT)-sch.pdf $(PROJECT)-pcb.pdf

