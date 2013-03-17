#!/usr/bin/python
# Copyright 2013 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Vishay 1212-8 dual FET package
#

# dimensions in mm from	si7232dn.pdf
PinWidth = 0.405
PinHeight = 0.99
PinSpacing = 0.65
RowOuter = 3.86

DrainWidth = 0.990
DrainHeight = 1.725
DrainSpacing = 0.225

BodyWidth = 3.3
BodyHeight = 3.3

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "1212-8" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
for pin in range (0,4):
    print '   Pad[',\
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(-(RowOuter/2 - PinWidth/2)), \
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(-(RowOuter/2 - PinHeight + PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (8 - pin), '"%i"' % (8 - pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(RowOuter/2 - PinWidth/2), \
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(RowOuter/2 - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '0x0100]'

print '   Pad[',\
    mm2mils100(-(DrainSpacing/2 + DrainWidth/2)), \
    mm2mils100(RowOuter/2 - PinHeight - 0.635 - DrainWidth/2), \
    mm2mils100(-(DrainSpacing/2 + DrainWidth/2)), \
    mm2mils100(RowOuter/2 - PinHeight - 0.635 - DrainHeight + DrainWidth/2), \
    mm2mils100(DrainWidth), \
    mm2mils100(DrainSpacing - DrainWidth), \
    mm2mils100(DrainWidth)+600, \
    '"pin8" "8" 0x0100]'

print '   Pad[',\
    mm2mils100(DrainSpacing/2 + DrainWidth/2), \
    mm2mils100(RowOuter/2 - PinHeight - 0.635 - DrainWidth/2), \
    mm2mils100(DrainSpacing/2 + DrainWidth/2), \
    mm2mils100(RowOuter/2 - PinHeight - 0.635 - DrainHeight + DrainWidth/2), \
    mm2mils100(DrainWidth), \
    mm2mils100(DrainSpacing - DrainWidth), \
    mm2mils100(DrainWidth)+600, \
    '"pin5" "5" 0x0100]'

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
        mm2mils100(-2 * PinSpacing), \
        mm2mils100(0.60 * RowOuter), \
	'500 500 0 360 1000 ]'

print ")"
