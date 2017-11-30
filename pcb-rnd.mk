AM=../altusmetrum
SCHEME=$(AM)/scheme

.SUFFIXES: .sch .lht .ps .pdf

# need to have PROJECT defined
ifndef PROJECT
	PROJECT=undefined
endif

# if SCHEMATICS not defined, default to one sheet with project name
ifndef SCHEMATICS
	SCHEMATICS=$(PROJECT).sch
endif

CONFIG=gafrc attribs project project.lht

all:	drc partslist partslist.csv pcb

drc:	$(PROJECT).drc

$(PROJECT).drc: $(SCHEMATICS) Makefile $(CONFIG)
	-gnetlist -g drc2 $(SCHEMATICS) -o $@

partslists: partslist partslist.csv partslist.dk partslist-check.dk partslist-mouser.csv partslist.other

partslist:	$(SCHEMATICS) Makefile $(AM)/preferred-parts $(CONFIG)
	gnetlist -g bom -o $(PROJECT).unsorted $(SCHEMATICS)
	head -n1 $(PROJECT).unsorted > partslist
	tail -n+2 $(PROJECT).unsorted | sort | awk -f $(AM)/bin/fillpartslist >> partslist
	rm -f $(PROJECT).unsorted

partslist.csv:	$(SCHEMATICS) Makefile $(AM)/preferred-parts $(CONFIG)
	gnetlist -L $(SCHEME) -g partslistgag -o $(PROJECT).csvtmp $(SCHEMATICS)
	(head -n1 $(PROJECT).csvtmp; tail -n+2 $(PROJECT).csvtmp | sort -t \, -k 8 | awk -f $(AM)/bin/fillpartscsv | sort ) > $@ && rm -f $(PROJECT).csvtmp

partslist.dk: partslist.csv
	$(AM)/bin/partslist-vendor --vendor digikey partslist.csv > $@

partslist-check.dk: partslist.csv
	$(AM)/bin/partslist-vendor --vendor digikey --mfg partslist.csv > $@

partslist-mouser.csv: partslist.csv
	$(AM)/bin/partslist-vendor --vendor mouser partslist.csv > $@

partslist.other: partslist.csv
	$(AM)/bin/partslist-vendor --not-vendor digikey,mouser partslist.csv > $@

$(PROJECT)-seeed.csv: partslist.csv
	$(AM)/bin/partslist-vendor --vendor seeed partslist.csv > $@

$(PROJECT)-goldphoenix.csv: partslist.csv
	$(AM)/bin/partslist-vendor --vendor goldphoenix partslist.csv > $@

pcb:	$(SCHEMATICS) Makefile $(CONFIG)
	gsch2pcb-rnd project

$(PROJECT).xy:	$(PROJECT).lht $(CONFIG)
	pcb-rnd -x bom $(PROJECT).lht

$(PROJECT).bottom.gbr:	$(PROJECT).lht $(CONFIG)
	pcb-rnd -x gerber $(PROJECT).lht
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

$(PROJECT).all-drill.cnc: $(PROJECT).bottom.gbr
	gerbv -x drill -o $(PROJECT).all-drill.cnc $(PROJECT).plated-drill.cnc $(PROJECT).unplated-drill.cnc

zip: $(PROJECT).zip

$(PROJECT).zip: $(PROJECT).bottom.gbr $(PROJECT).xy Makefile
	rm -f $@ && zip $@ $(PROJECT).*.gbr $(PROJECT).*.cnc $(PROJECT).xy # $(PROJECT).xls

ac: $(PROJECT)-ac.zip $(PROJECT)-bom.csv

$(PROJECT)-bom.csv: partslist.csv
	cp partslist.csv $@

$(PROJECT)-ac.zip:  $(PROJECT).bottom.gbr $(PROJECT).xy
	cp $(PROJECT).bottom.gbr $(PROJECT).gbl
	cp $(PROJECT).bottommask.gbr $(PROJECT).gbs
	if [ -f $(PROJECT).bottomsilk.gbr ]; then \
		cp $(PROJECT).bottomsilk.gbr $(PROJECT).gbo; \
	fi
	if [ -f $(PROJECT).bottompaste.gbr ]; then \
		cp $(PROJECT).bottompaste.gbr $(PROJECT).gbp; \
	fi
	if [ -f $(PROJECT).topsilk.gbr ]; then \
		cp $(PROJECT).topsilk.gbr $(PROJECT).gto; \
	fi
	if [ -f $(PROJECT).toppaste.gbr ]; then \
		cp $(PROJECT).toppaste.gbr $(PROJECT).gtp; \
	fi
	cp $(PROJECT).outline.gbr $(PROJECT).gml
	cp $(PROJECT).top.gbr $(PROJECT).gtl
	cp $(PROJECT).topmask.gbr $(PROJECT).gts
	cp $(PROJECT).plated-drill.cnc $(PROJECT).ncd
	if [ -f $(PROJECT).unplated-drill.cnc ]; then \
		cp $(PROJECT).unplated-drill.cnc $(PROJECT).drd; \
	fi
	if [ -f $(PROJECT).group1.gbr -a -f $(PROJECT).group2.gbr ]; then \
		cp $(PROJECT).group1.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group2.gbr $(PROJECT).gl3; \
	elif [ -f $(PROJECT).group2.gbr -a -f $(PROJECT).group3.gbr ]; then \
		cp $(PROJECT).group2.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group3.gbr $(PROJECT).gl3; \
	fi
	rm -f $@ && zip $@ \
		$(PROJECT).gtl $(PROJECT).gts $(PROJECT).gto $(PROJECT).gtp \
		$(PROJECT).gbl $(PROJECT).gbs $(PROJECT).gbo $(PROJECT).gbp \
		$(PROJECT).gml $(PROJECT).ncd $(PROJECT).gml $(PROJECT).drd \
		$(PROJECT).gl2 $(PROJECT).gl3 \
		$(PROJECT).xy

oshpark: $(PROJECT)-oshpark.zip

$(PROJECT)-oshpark.zip: $(PROJECT).bottom.gbr $(PROJECT).all-drill.cnc 
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
	cp $(PROJECT).all-drill.cnc drills.xln
	if [ -f $(PROJECT).group1.gbr -a -f $(PROJECT).group2.gbr ]; then \
		cp $(PROJECT).group1.gbr internal\ plane\ 1.ger; \
		cp $(PROJECT).group2.gbr internal\ plane\ 2.ger; \
	elif [ -f $(PROJECT).group2.gbr -a -f $(PROJECT).group3.gbr ]; then \
		cp $(PROJECT).group2.gbr internal\ plane\ 1.ger; \
		cp $(PROJECT).group3.gbr internal\ plane\ 2.ger; \
	fi
	rm -f $@ && zip $@ *.ger *.xln

seeed: $(PROJECT)-seeed.zip $(PROJECT)-seeed.csv

$(PROJECT)-seeed.zip: $(PROJECT).bottom.gbr $(PROJECT).all-drill.cnc $(PROJECT)-sch.pdf $(PROJECT).xy $(SEEED_EXTRA)
	cp $(PROJECT).bottom.gbr $(PROJECT).gbl
	cp $(PROJECT).bottommask.gbr $(PROJECT).gbs
	if [ -f $(PROJECT).bottomsilk.gbr ]; then \
		cp $(PROJECT).bottomsilk.gbr $(PROJECT).gbo; \
	fi
	if [ -f $(PROJECT).bottompaste.gbr ]; then \
		cp $(PROJECT).bottompaste.gbr $(PROJECT).gbp; \
	fi
	if [ -f $(PROJECT).topsilk.gbr ]; then \
		cp $(PROJECT).topsilk.gbr $(PROJECT).gto; \
	fi
	if [ -f $(PROJECT).toppaste.gbr ]; then \
		cp $(PROJECT).toppaste.gbr $(PROJECT).gtp; \
	fi
	cp $(PROJECT).outline.gbr $(PROJECT).gml
	cp $(PROJECT).top.gbr $(PROJECT).gtl
	cp $(PROJECT).topmask.gbr $(PROJECT).gts
	cp $(PROJECT).all-drill.cnc $(PROJECT).txt
	if [ -f $(PROJECT).group1.gbr -a -f $(PROJECT).group2.gbr ]; then \
		cp $(PROJECT).group1.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group2.gbr $(PROJECT).gl3; \
	elif [ -f $(PROJECT).group2.gbr -a -f $(PROJECT).group3.gbr ]; then \
		cp $(PROJECT).group2.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group3.gbr $(PROJECT).gl3; \
	fi
	rm -f $@ && zip $@ \
		$(PROJECT).gtl $(PROJECT).gts $(PROJECT).gto $(PROJECT).gtp \
		$(PROJECT).gbl $(PROJECT).gbs $(PROJECT).gbo $(PROJECT).gbp \
		$(PROJECT).gml $(PROJECT).txt \
		$(PROJECT).gl2 $(PROJECT).gl3 \
		$(PROJECT).xy $(PROJECT)-sch.pdf \
		$(SEEED_EXTRA)

goldphoenix: $(PROJECT)-goldphoenix.zip

$(PROJECT)-goldphoenix.zip: $(PROJECT).bottom.gbr $(PROJECT).all-drill.cnc $(PROJECT)-sch.pdf $(PROJECT).xy $(PROJECT)-goldphoenix.csv
	cp $(PROJECT).bottom.gbr $(PROJECT).gbl
	cp $(PROJECT).bottommask.gbr $(PROJECT).gbs
	if [ -f $(PROJECT).bottomsilk.gbr ]; then \
		cp $(PROJECT).bottomsilk.gbr $(PROJECT).gbo; \
	fi
	if [ -f $(PROJECT).bottompaste.gbr ]; then \
		cp $(PROJECT).bottompaste.gbr $(PROJECT).gbp; \
	fi
	if [ -f $(PROJECT).topsilk.gbr ]; then \
		cp $(PROJECT).topsilk.gbr $(PROJECT).gto; \
	fi
	if [ -f $(PROJECT).toppaste.gbr ]; then \
		cp $(PROJECT).toppaste.gbr $(PROJECT).gtp; \
	fi
	cp $(PROJECT).outline.gbr $(PROJECT).gml
	cp $(PROJECT).top.gbr $(PROJECT).gtl
	cp $(PROJECT).topmask.gbr $(PROJECT).gts
	cp $(PROJECT).all-drill.cnc $(PROJECT).txt
	if [ -f $(PROJECT).group1.gbr -a -f $(PROJECT).group2.gbr ]; then \
		cp $(PROJECT).group1.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group2.gbr $(PROJECT).gl3; \
	elif [ -f $(PROJECT).group2.gbr -a -f $(PROJECT).group3.gbr ]; then \
		cp $(PROJECT).group2.gbr $(PROJECT).gl2; \
		cp $(PROJECT).group3.gbr $(PROJECT).gl3; \
	fi
	rm -f $@ && zip $@ \
		$(PROJECT).gtl $(PROJECT).gts $(PROJECT).gto $(PROJECT).gtp \
		$(PROJECT).gbl $(PROJECT).gbs $(PROJECT).gbo $(PROJECT).gbp \
		$(PROJECT).gml $(PROJECT).txt \
		$(PROJECT).gl2 $(PROJECT).gl3 \
		$(PROJECT).xy $(PROJECT)-sch.pdf \
		$(PROJECT)-goldphoenix.csv

stencilsunlimited:	$(PROJECT).bottom.gbr $(PROJECT).toppaste.gbr $(PROJECT).outline.gbr
	rm -f $(PROJECT)-stencil.zip && zip $(PROJECT)-stencil.zip $(PROJECT).toppaste.gbr $(PROJECT).outline.gbr

stencil:	$(PROJECT).lht
	pcb-rnd -x gerber -c design/paste_adjust=-10mil $(PROJECT).lht
	mv $(PROJECT).toppaste.gbr stencil.gbr

clean:
	rm -f *.bom *.drc *.log *~ $(PROJECT).ps *.gbr *.cnc *bak* *- *.zip 
	rm -f *.net *.xy *.cmd *.png partslist partslist.csv *.ger *.xln
	rm -f *.partslist *.unsorted $(PROJECT).xls muffin-5267.pdf muffin-keithp.pdf
	rm -f partslist-check.dk partslist.dk partslist-mouser.csv partslist.other
	rm -f $(PROJECT)-sch.ps $(PROJECT)-sch.pdf $(PROJECT)-pcb.ps $(PROJECT)-pcb.pdf
	rm -f $(PROJECT).gbl $(PROJECT).gbs $(PROJECT).gbo $(PROJECT).gbp $(PROJECT).ncd
	rm -f $(PROJECT).gto $(PROJECT).gtp $(PROJECT).gml $(PROJECT).gtl $(PROJECT).gts
	rm -f $(PROJECT).txt $(PROJECT).gl2 $(PROJECT).gl3
	rm -f $(PROJECT)-seeed.zip $(PROJECT)-seeed.csv
	rm -f $(PROJECT)-goldphoenix.zip $(PROJECT)-goldphoenix.csv
	rm -f $(PROJECT)*.ps $(PROJECT)*.pdf

muffins: muffin-5267.pdf muffin-keithp.pdf

muffin-5267.pdf: partslist.csv $(AM)/glabels/muffin-short-5267.glabels
	glabels-3-batch $(AM)/glabels/muffin-short-5267.glabels -i partslist.csv -o $@ > /dev/null

muffin-keithp.pdf: partslist.csv $(AM)/glabels/muffin-5267.glabels
	glabels-3-batch $(AM)/glabels/muffin-5267.glabels -i partslist.csv -o $@ > /dev/null

.sch.ps:
	gschem -p -o $@ -s /usr/share/gEDA/scheme/print.scm $*.sch

.ps.pdf:
	ps2pdf $*.ps

SCHEMATICS_PS=$(SCHEMATICS:.sch=.ps)
SCHEMATICS_PDF=$(SCHEMATICS:.sch=.pdf)

$(PROJECT)-sch.pdf:	$(SCHEMATICS_PDF)
	pdfjoin -o $@ $(SCHEMATICS_PDF)

$(PROJECT)-pcb.ps:	$(PROJECT).lht $(CONFIG)
	pcb-rnd -x ps --psfile $@ --media Letter --ps-color $(PROJECT).lht

$(PROJECT)-pcb.pdf:	$(PROJECT)-pcb.ps
	ps2pdf $(PROJECT)-pcb.ps

$(PROJECT)-big.ps:	$(PROJECT).lht $(CONFIG)
	pcb-rnd -x ps --psfile $@ --media Letter --ps-color --fill-page --no-align-marks $(PROJECT).lht

$(PROJECT)-big.pdf:	$(PROJECT)-big.ps
	ps2pdf $(PROJECT)-big.ps

pdf:	$(PROJECT)-sch.pdf $(PROJECT)-pcb.pdf $(PROJECT)-big.pdf

project:
	(echo 'schematics $(SCHEMATICS)'; \
	 echo 'output-name $(PROJECT)'; \
	 echo 'skip-m4') > $@

attribs: $(AM)/attribs
	cp $(AM)/attribs $@

gafrc:
	(echo '; empty the library path and populate it with only our own symbols'; \
	 echo '(reset-component-library)'; \
	 echo '(load "../altusmetrum/gafrc")') > $@

.gitignore: $(AM)/gitignore.in
	sed 's/@@PROJECT@@/$(PROJECT)/g' $(AM)/gitignore.in > .gitignore
