#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Analog Devices ADXL78 accelerometer
#

# dimensions in mm from 4326543067473486309AN652_0.pdf
PinWidth = 0.80
PinHeight = 2.60
PinSpacing = 1.27
RowCenters = 4.55
RowSpacing = RowCenters - PinHeight
BodyWidth = 5.0
BodyHeight = 5.0

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "ADXL78" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
for pin in range (0,3):
    print '   Pad[',\
	mm2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (pin+1), '"%i"' % (pin+1), '0x0100]'

    print '   Pad[',\
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (7 - pin), '"%i"' % (7 - pin), '0x0100]'

print '   Pad[',\
 	0, \
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	0, \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (4), '"%i"' % (4), '0x0100]'

print '   Pad[',\
 	0, \
	mm2mils100(-RowSpacing/2 - PinWidth/2), \
 	0, \
	mm2mils100(- RowSpacing/2 - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (8), '"%i"' % (8), '0x0100]'

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
        mm2mils100(-0.6 * BodyWidth), \
        mm2mils100(-0.45 * BodyHeight), \
	'500 500 0 360 1000 ]'

print ")"
