#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for ABM8 package used by Xtals
#

# dimensions in mm from abm8.pdf Abracon datasheet
PinHeight = 1.30
PinWidth = 1.05
HSpacing = 1.00
WSpacing = 0.8

# freedfm.com round-off error bites us if we make this 700...
MinAnnular = 725
MinClearance = 600
MaskDelta = 300

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "ABM8" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(-(HSpacing/2 + PinWidth/2)), \
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(-(HSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(HSpacing/2 + PinWidth/2), \
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(HSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(HSpacing/2 + PinWidth/2), \
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(HSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"pin4" "4" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(-(HSpacing/2 + PinWidth/2)), \
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(-(HSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"pin3" "3" 0x0100]'

print '   ElementArc[',\
	mm2mils100(WSpacing*0.2), \
	mm2mils100(HSpacing/2+PinHeight*0.8), \
	'500 500 0 360 1000 ]'

print ")"
