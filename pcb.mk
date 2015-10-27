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

all:	drc partslist partslist.csv pcb

drc:	$(PROJECT).sch Makefile
	-gnetlist -g drc2 $(PROJECT).sch -o $(PROJECT).drc

partslist:	$(PROJECT).sch Makefile $(AM)/preferred-parts
	gnetlist -g bom -o $(PROJECT).unsorted $(SCHEMATICS)
	head -n1 $(PROJECT).unsorted > partslist
	tail -n+2 $(PROJECT).unsorted | sort | awk -f $(AM)/bin/fillpartslist >> partslist
	rm -f $(PROJECT).unsorted

partslist.csv:	$(SCHEMATICS) Makefile $(AM)/preferred-parts
	gnetlist -L $(SCHEME) -g partslistgag -o $(PROJECT).csvtmp $(SCHEMATICS)
	(head -n1 $(PROJECT).csvtmp; tail -n+2 $(PROJECT).csvtmp | sort -t \, -k 8 | awk -f $(AM)/bin/fillpartscsv ) > $@ && rm -f $(PROJECT).csvtmp

partslist.dk: $(SCHEMATICS) Makefile $(AM)/preferred-parts partslist.csv
	$(AM)/bin/partslist-vendor --vendor digikey partslist.csv > $@

partslist-check.dk: $(SCHEMATICS) Makefile $(AM)/preferred-parts partslist.csv
	$(AM)/bin/partslist-vendor --vendor digikey --mfg partslist.csv > $@

partslist.mouser: $(SCHEMATICS) Makefile $(SCHEME)/gnet-partslist-bom.scm
	$(AM)/bin/partslist-vendor --vendor mouser partslist.csv > $@

partslist.other: $(SCHEMATICS) Makefile $(SCHEME)/gnet-partslist-bom.scm
	$(AM)/bin/partslist-vendor --not-vendor digikey,mouser partslist.csv > $@

pcb:	$(SCHEMATICS) project Makefile
	gsch2pcb project

$(PROJECT).xy:	$(PROJECT).pcb
	pcb -x bom $(PROJECT).pcb

$(PROJECT).bottom.gbr:	$(PROJECT).pcb
	pcb -x gerber $(PROJECT).pcb

zip:	$(PROJECT).bottom.gbr $(PROJECT).bottommask.gbr $(PROJECT).fab.gbr $(PROJECT).top.gbr $(PROJECT).topmask.gbr $(PROJECT).toppaste.gbr $(PROJECT).group2.gbr $(PROJECT).group3.gbr $(PROJECT).plated-drill.cnc $(PROJECT).xy  Makefile # $(PROJECT).xls
	rm -f $(PROJECT).topsilk.gbr
	zip $(PROJECT).zip $(PROJECT).*.gbr $(PROJECT).*.cnc $(PROJECT).xy # $(PROJECT).xls

oshpark: $(PROJECT).bottom.gbr $(PROJECT).bottommask.gbr $(PROJECT).top.gbr $(PROJECT).topmask.gbr $(PROJECT).plated-drill.cnc
	cp $(PROJECT).bottom.gbr bottom\ layer.ger
	cp $(PROJECT).bottommask.gbr bottom\ solder\ mask.ger
	cp $(PROJECT).bottomsilk.gbr bottom\ silk\ screen.ger
	cp $(PROJECT).outline.gbr board\ outline.ger
	cp $(PROJECT).top.gbr top\ layer.ger
	cp $(PROJECT).topmask.gbr top\ solder\ mask.ger
	cp $(PROJECT).plated-drill.cnc drills.xln
	cp $(PROJECT).group2.gbr internal\ plane\ 1.ger
	cp $(PROJECT).group3.gbr internal\ plane\ 2.ger
	zip $(PROJECT)-oshpark.zip *.ger *.xln

stencil:	$(PROJECT).bottom.gbr $(PROJECT).toppaste.gbr $(PROJECT).outline.gbr
	zip $(PROJECT)-stencil.zip $(PROJECT).toppaste.gbr $(PROJECT).outline.gbr

clean:
	rm -f *.bom *.drc *.log *~ $(PROJECT).ps *.gbr *.cnc *bak* *- *.zip 
	rm -f *.net *.xy *.cmd *.png partslist partslist.csv *.ger *.xln
	rm -f *.partslist *.new.pcb *.unsorted $(PROJECT).xls muffin-5267.pdf
	rm -f $(PROJECT)-sch.ps $(PROJECT)-sch.pdf $(PROJECT)-pcb.ps $(PROJECT)-pcb.pdf

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

