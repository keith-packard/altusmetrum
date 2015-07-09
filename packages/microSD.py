#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Amphenol micro SD connector
#

# dimensions in mm from 101-00303-xx.pdf
PinWidth = 0.60
PinHeight = 1.05
PinSpacing = 1.10
PinY = 9.47
PinXOffset = 4.53

MntWidth = 1.05
MntHeight = 1.50
MntY1 = 3.60
MntY2 = 12.00
MntX = 13.60

BoxX = 13.60
BoxY = 13.30
LineWidth = 1000

MaskAdd = 0.15

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "microSD" "" "" 0 0 0 0 0 100 0x0]'
print "("

# mounting pads
print '   Pad[',\
 	mm2mils100(-MntX/2), \
 	mm2mils100(MntY1-(MntHeight/2)+(MntWidth/2)), \
 	mm2mils100(-MntX/2), \
 	mm2mils100(MntY1+(MntHeight/2)-(MntWidth/2)), \
	mm2mils100(MntWidth), \
	mm2mils100(0), \
  	mm2mils100(MntWidth + MaskAdd), \
	'"9" "9" 0x0100]'

print '   Pad[',\
 	mm2mils100(MntX/2), \
 	mm2mils100(MntY1-(MntHeight/2)+(MntWidth/2)), \
 	mm2mils100(MntX/2), \
 	mm2mils100(MntY1+(MntHeight/2)-(MntWidth/2)), \
	mm2mils100(MntWidth), \
	mm2mils100(0), \
  	mm2mils100(MntWidth + MaskAdd), \
	'"9" "9" 0x0100]'

print '   Pad[',\
 	mm2mils100(-MntX/2), \
 	mm2mils100(MntY2-(MntHeight/2)+(MntWidth/2)), \
 	mm2mils100(-MntX/2), \
 	mm2mils100(MntY2+(MntHeight/2)-(MntWidth/2)), \
	mm2mils100(MntWidth), \
	mm2mils100(0), \
  	mm2mils100(MntWidth + MaskAdd), \
	'"9" "9" 0x0100]'

print '   Pad[',\
 	mm2mils100(MntX/2), \
 	mm2mils100(MntY2-(MntHeight/2)+(MntWidth/2)), \
 	mm2mils100(MntX/2), \
 	mm2mils100(MntY2+(MntHeight/2)-(MntWidth/2)), \
	mm2mils100(MntWidth), \
	mm2mils100(0), \
  	mm2mils100(MntWidth + MaskAdd), \
	'"9" "9" 0x0100]'

# signal pads
for pin in range (1,9):
    print '   Pad[',\
 	mm2mils100(-PinXOffset + (8-pin) * PinSpacing), \
 	mm2mils100(PinY-(PinHeight/2)+(PinWidth/2)), \
 	mm2mils100(-PinXOffset + (8-pin) * PinSpacing), \
 	mm2mils100(PinY+(PinHeight/2)-(PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth + MaskAdd), \
	'"pin%i"' % (pin), '"%i"' % (pin), '0x0100]'

# silkscreen box
print '   ElementLine[', \
        mm2mils100(BoxX/2), \
        mm2mils100(0), \
        mm2mils100(BoxX/2), \
        mm2mils100(BoxY), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(-BoxX/2), \
        mm2mils100(0), \
        mm2mils100(-BoxX/2), \
        mm2mils100(BoxY), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(-BoxX/2), \
        mm2mils100(0), \
        mm2mils100(+BoxX/2), \
        mm2mils100(0), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(-BoxX/2), \
        mm2mils100(BoxY), \
        mm2mils100(+BoxX/2), \
        mm2mils100(BoxY), \
        LineWidth, ']'


print ")"
