#!/usr/bin/python
# Copyright 2015 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Tyco/AMP Micro-MaTch vertical surface-mount female connectors
#
# Needs pin count on command line, in range of 4..20 even numbers only
#

# dimensions in mm from ENG_CD_188275_S3_c-188275_drw.pdf
PadWidth = 1.50
PadHeight = 3.00
PadSpacing = 1.27
RowGap = 1.50		# space between rows

Clearance = 0.006	# in mils

BoxY = 5.2
BoxXbase = 4.55
BoxXstep = 2.55

LineWidth = 600

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = int(sys.argv[1])

if pins < 4:
	sys.stderr.write('Must be at least 4 pins\n')
	sys.exit(1)
if pins > 20:
	sys.stderr.write('Must be no more than 20 pins\n')
	sys.exit(1)

if len(sys.argv) > 2:
    if sys.argv[2] == "latch":
	BoxXbase = 7.15

BoxXOffset = -((pins - 1) * PadSpacing)/2

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "MicroMatch%i"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for col in range ((pins+1)/2):
    for row in range (2):
	if row == 1:
	    origin= (RowGap + PadHeight)/2
	else:
	    origin= -(RowGap + PadHeight)/2
        pinnum = (col * 2) + row + 1
	Flags = '"square,nopaste"'

	print '   Pad[', \
	    mm2mils100((pinnum-1)*PadSpacing + BoxXOffset), \
	    mm2mils100(origin + PadHeight/2 - PadWidth/2), \
	    mm2mils100((pinnum-1)*PadSpacing + BoxXOffset), \
	    mm2mils100(origin - PadHeight/2 + PadWidth/2), \
	    mm2mils100(PadWidth), \
	    0, \
	    mm2mils100(PadWidth)+Clearance*2, \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'
	    
BoxX = BoxXbase + pins/2 * BoxXstep
BoxX1 = -BoxX/2
BoxX2 = BoxX/2
BoxY1 = -BoxY/2
BoxY2 = BoxY/2

print '   ElementLine[', \
  	mm2mils100(BoxX1), \
	mm2mils100(BoxY1), \
	mm2mils100(BoxX1), \
	mm2mils100(BoxY2), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(BoxX1), \
	mm2mils100(BoxY2), \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY2), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY2), \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY1), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY1), \
	mm2mils100(BoxX1), \
	mm2mils100(BoxY1), \
	LineWidth, ']'
  
print ")"
