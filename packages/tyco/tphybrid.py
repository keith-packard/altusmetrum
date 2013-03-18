#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for a 16 pin
#   Tyco/AMP Micro-MaTch vertical through-hole female connectors
# overlaid with a 10-pin 
#   Tyco Electronics Buchanan 2.54mm pitch terminal blocks
#

# dimensions in mm from C_215079_v.pdf datasheet
BUPinDiam = 1.1		# screw terminals
MMPinDiam = 0.8		# micromatch
PinSpacing = 1.27
RowSpacing = 2.54

MntX = 1.4
MntY = 1.8
MntDiam = 1.5

BoxY = 5.1

LineWidth = 600

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = 17

BoxXbase = 5.89
BoxEnd = 1.5

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "tphybrid" "" "" 0 0 0 0 0 100 0x0]'
print "("
for col in range ((pins+1)/2):
    for row in range (2):
	if row == 1:
	    spacing=0
	else:
	    spacing=RowSpacing
        pinnum = (col * 2) + row + 1
	if pinnum != 18:
            if pinnum == 1:
	        Flags = '0x0101'
            else:
	        Flags = '0x0001'
	    if pinnum % 2 == 0:
		PinDiam = MMPinDiam
	    else:
		PinDiam = BUPinDiam
            print '   Pin[', \
  	        mm2mils100((pinnum-1)*PinSpacing), \
	        mm2mils100(spacing), \
  	        mm2mils100(PinDiam + 0.70), \
	        1200, \
  	        mm2mils100(PinDiam + 0.86), \
	        mm2mils100(PinDiam), \
	        '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

print '   Pin[', \
    mm2mils100((-2)*PinSpacing), \
    mm2mils100(RowSpacing), \
    mm2mils100(PinDiam + 0.32), \
    1200, \
    mm2mils100(PinDiam + 0.48), \
    mm2mils100(PinDiam), \
    '"pin18"' , '"18"', Flags, ']'

# add a hole for the index pin.  plated to save non-plated-hole extra fab cost.
print '   Pin[', \
    mm2mils100(-MntX), \
    mm2mils100(RowSpacing-MntY), \
    mm2mils100(MntDiam)+1400, \
    1400, \
    mm2mils100(MntDiam)+1400+600, \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0001', ']'

# pins-2 accounts for the extra pin used by screw terminal overlay
BoxX = (pins - 2) * PinSpacing + BoxXbase
BoxX1 = -(BoxXbase/2)
BoxX2 = BoxX1 + BoxX
# re-compute X1 after computing X2 to account for screw terminal overlay
BoxX1 = -2*PinSpacing - BoxEnd
BoxY1 = -(BoxY - RowSpacing)/2
BoxY2 = BoxY1 + BoxY

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
