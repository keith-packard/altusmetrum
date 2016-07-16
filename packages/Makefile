.SUFFIXES: .5c .py .fp

DIRS= \
	diodes \
	jst \
	molex \
	norcomp \
	phoenix \
	pinheader \
	switches \
	tyco 

SOIC=soic-16.fp

FOOTPRINTS= \
	$(SOIC) \
	s-pwson-n8.fp \
	s-pwson-n6.fp \
	MS5607.fp \
	uson-8.fp \
	wson6x5.fp \
	hvqfn33.fp \
	ZX62-B-5PA.fp \
	TDK_PS12.fp \
	ABM3B.fp \
	ABM8.fp \
	7S.fp \
	1212-8.fp \
	AN3111.fp \
	lqfp32.fp \
	lqfp48.fp \
	lqfp64.fp \
	lqfp100.fp \
	LPCC16.fp \
	MPU6000.fp \
	UBLOX-MAX.fp \
	TI-QFN32.fp \
	TI-QFN36.fp \
	TI-QFN32-new.fp \
	NDK32.fp \
	sma-edge.fp \
	MO-220.fp \
	8ufson2x2.fp \
	ti-qfn20.fp \
	qfn-16.fp \
	ap.10g.fp \
	BTM182.fp \
	PNswitchDPDT.fp \
	NHD-C0216.fp \
	KSCJ.fp \
	ADXL78.fp \
	MOT1317.fp \
	mlp8-4x3.fp \
	saw.fp \
	fotofab2x3.fp \
	linear-s8.fp \
	ufqfpn48.fp \
	saw.fp \
	tfsoj-8.fp \
	bc4aa.fp \
	linear-s8.fp \
	PJ-037A.fp \
	cx1vsm.fp \
	pklcs1212.fp \
	CR32.fp \
	FTDI-QFN32.fp \
	g6z1f.fp \
	g6z1fe.fp \
	W3011A.fp \
	DIODE-SMA.fp \
	2512.fp \
	lipo-15x24.fp \
	wire-ant.fp \
	PCM12SMTR.fp \
	usbAmale.fp \
	usbAmale-around.fp \
	nx3215sa.fp \
	DR127.fp \
	PowerPAD32.fp \
	usb_onboard.fp \
	u-pdfn-8.fp \
	ufqfpn28.fp \
	sot666.fp \
	sot323.fp \
	sod123.fp \
	0806.fp \
	fuse345.fp \
	g5rl1ae.fp \
	DO-214AC.fp \
	BU2032SM.fp \
	TO252AA.fp \
	TO252.fp \
	TO252FET.fp \
	SD.fp \
	microSD.fp \
	v-bite.fp \
	qfn16-3x3.fp \
	1051330011.fp \
	2013499-1.fp \
	servo.fp \
	servo-motor.fp \
	TDK_PS12-small.fp \
	CAP_FC8.fp \
	3568.fp \
	ABM12.fp

.5c.fp:
	nickle $*.5c -o $@

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

$(FOOTPRINTS): footprint.5c

clean: $(CLEANDIRS)
	rm -f $(FOOTPRINTS)

.PHONY: subdirs $(DIRS)
.PHONY: subdirs $(BUILDDIRS)
.PHONY: subdirs $(CLEANDIRS)

.gitignore: Makefile
	for i in $@ $(FOOTPRINTS); do echo $$i; done > $@

soic-16.fp: soic.5c
	nickle soic.5c 16 > $@

lipo-15x24.fp: lipo-pad.5c
	nickle lipo-pad.5c 15 24 > $@
