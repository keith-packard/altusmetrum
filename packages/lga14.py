#!/usr/bin/python
# Copyright 2018 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for LGA 14 such as ADXL375
#

# dimensions in mm from ADXL375.pdf

PinWidth = 0.55
PinHeight = 1.145
PinSpacing = 0.8
RowCenters = 3.340 - PinHeight
RowSpacing = RowCenters - PinHeight
EndCenters = 5.340 - PinHeight
EndSpacing = EndCenters - PinHeight
BodyWidth = 3.0
BodyHeight = 5.0

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3'
print '# use-license: unlimited'

print 'Element[0x0 "lga14" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
for pin in range (0,6):
    print '   Pad[',\
 	mm2mils100((pin-2.5) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-2.5) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (13 - pin), '"%i"' % (13 - pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((pin-2.5) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-2.5) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(EndSpacing/2 + PinWidth/2), \
 	0, \
	mm2mils100(EndSpacing/2 + PinHeight - PinWidth/2), \
 	0, \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % 7, '"%i"' % 7, '0x0100]'

    print '   Pad[',\
	-mm2mils100(EndSpacing/2 + PinWidth/2), \
 	0, \
	-mm2mils100(EndSpacing/2 + PinHeight - PinWidth/2), \
 	0, \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % 14, '"%i"' % 14, '0x0100]'

print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	mm2mils100(-BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	mm2mils100( BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	mm2mils100( BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	mm2mils100(-BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	'1000 ]'

print '   ElementArc[',\
        mm2mils100(-2.75 * PinSpacing), \
        mm2mils100(RowSpacing*2), \
	'500 500 0 360 1000 ]'

print ")"
