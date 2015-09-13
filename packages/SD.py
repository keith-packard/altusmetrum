#!/usr/bin/python
# Copyright 2015 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for Amphenol SD connector
#

# dimensions in mm from amphenol/sd.pdf

PadWidth = 1.50
PadHeight = 1.00
PadX = -24.31
Pad1Y = -8.60 + 2.50
Pad2Y = -8.60 + 5.00
Pad3Y = -8.60 + 5.00 + 1.70 + 1.70
Pad4Y = -8.60 + 5.00 + 1.70 + 1.70 + 1.65
Pad5Y = -8.60 + 15.00 - 2.50
Pad6Y = -8.60 + 15.00
Pad7Y = -8.60 + 15.00 + 2.43
Pad8Y = -8.60 + 15.00 + 2.43 + 1.70
Pad9Y = -8.60
PadCDY = -8.60 + 5.00 + 1.70
PadWPY = -8.60 + 15.00 + 2.43 + 1.70 + 3.35

MntWidth = 2.00
MntHeight = 1.20
MntY1 = 15.00 - 29.20 + (MntHeight / 2)
MntX1 = -3.30
MntY2 = 15.00 - (MntHeight / 2)
MntX2 = -2.10

HoleDiam = 1.50
Hole1Y = -11.30
Hole2Y = 12.85

BoxX = 29.1 + 1.16
BoxXLeft = -23.5 - 1.16
BoxY = 28.9
LineWidth = 1000

MaskAdd = 0.15

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3'
print '# use-license: unlimited'

print 'Element[0x0 "microSD" "" "" 0 0 0 0 0 100 0x0]'
print "("

# mounting pads
print '   Pad[',\
 	mm2mils100(MntX1 - MntWidth/2 + MntHeight/2), \
 	mm2mils100(MntY1), \
 	mm2mils100(MntX1 + MntWidth/2 - MntHeight/2), \
 	mm2mils100(MntY1), \
	mm2mils100(MntHeight), \
	mm2mils100(0), \
  	mm2mils100(MntHeight + MaskAdd), \
	'"12" "12" 0x0100]'

print '   Pad[',\
 	mm2mils100(MntX2 - MntWidth/2 + MntHeight/2), \
 	mm2mils100(MntY2), \
 	mm2mils100(MntX2 + MntWidth/2 - MntHeight/2), \
 	mm2mils100(MntY2), \
	mm2mils100(MntHeight), \
	mm2mils100(0), \
  	mm2mils100(MntHeight + MaskAdd), \
	'"12" "12" 0x0100]'

# signal pads
print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad1Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad1Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad2Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad2Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad3Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad3Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"3" "3" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad4Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad4Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"4" "4" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad5Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad5Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"5" "5" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad6Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad6Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"6" "6" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad7Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad7Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"7" "7" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad8Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad8Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"8" "8" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(Pad9Y), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(Pad9Y), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"9" "9" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(PadCDY), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(PadCDY), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"10" "10" 0x0100]'

print '   Pad[',\
 	mm2mils100(PadX - PadWidth/2 + PadHeight/2), \
 	mm2mils100(PadWPY), \
 	mm2mils100(PadX + PadWidth/2 - PadHeight/2), \
 	mm2mils100(PadWPY), \
	mm2mils100(PadHeight), \
	mm2mils100(0), \
  	mm2mils100(PadHeight + MaskAdd), \
	'"11" "11" 0x0100]'

# mounting holes
print '   Pin[',\
        0, \
        mm2mils100(Hole1Y), \
        mm2mils100(HoleDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(HoleDiam+0.66), \
        mm2mils100(HoleDiam), \
        '"12" "12" 0x0000]'

print '   Pin[',\
        0, \
        mm2mils100(Hole2Y), \
        mm2mils100(HoleDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(HoleDiam+0.66), \
        mm2mils100(HoleDiam), \
        '"12" "12" 0x0000]'

BoxX = 29.1 + 1.16
BoxXLeft = -23.5 - 1.16
BoxY = 28.9

# silkscreen box
print '   ElementLine[', \
        mm2mils100(BoxXLeft), \
        mm2mils100(-BoxY/2), \
        mm2mils100(BoxXLeft), \
        mm2mils100(BoxY/2), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(BoxXLeft + BoxX), \
        mm2mils100(-BoxY/2), \
        mm2mils100(BoxXLeft + BoxX), \
        mm2mils100(BoxY/2), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(BoxXLeft), \
        mm2mils100(-BoxY/2), \
        mm2mils100(BoxXLeft + BoxX), \
        mm2mils100(-BoxY/2), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(BoxXLeft), \
        mm2mils100(BoxY/2), \
        mm2mils100(BoxXLeft + BoxX), \
        mm2mils100(BoxY/2), \
        LineWidth, ']'

print ")"
