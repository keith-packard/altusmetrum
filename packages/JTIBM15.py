#!/usr/bin/python
# Copyright 2017 by Bdale Garbee <bdale@gag.com>.  GPLv3+
#
# Program to emit PCB footprint for Johanson balun/filter modules
# (parts like the 0433BM15A0001 and 0915BM15A0001 for use with TI's cc1111)
#

# dimensions in mm from 0433BM15A0001.pdf JTI datasheet
PinWidth = 0.35
PinHeight = 1.0
PinSpacing = 0.65
RowCenters = 1.8
RowSpacing = RowCenters - PinHeight
BodyWidth = 1.25
BodyHeight = 2.00

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "JTIBM15" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
for pin in range (0,3):
    print '   Pad[',\
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (6 - pin), '"%i"' % (6 - pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-1) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '0x0100]'

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
        mm2mils100(-1.8 * PinSpacing), \
        mm2mils100(RowSpacing*1.3), \
	'500 500 0 360 1000 ]'

print ")"
