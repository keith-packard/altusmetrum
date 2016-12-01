#!/usr/bin/python
# Copyright 2016 by Bdale Garbee <bdale@gag.com>.  GPLv3+
#
# Program to emit PCB footprint for Microchip BM70BLES1FC2 Bluetooth LE module
#

# dimensions in mm from BM70/71 Data Sheet

BodyWidth = 12.00
BodyHeight = 22.00

GndEdgeLine = 18.00

PinWidth = 0.7
PinHeight = 1.5
PinSpacing = 1.1
PinOffset = 0.5

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3+'
print '# use-license: unlimited'

print 'Element[0x0 "BM70BLES1FC2" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(BodyHeight - 21.2), \
	mm2mils100(BodyWidth + PinOffset - PinWidth/2), \
 	mm2mils100(BodyHeight - 21.2), \
	mm2mils100(BodyWidth + PinOffset - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(BodyHeight - 21.2), \
	mm2mils100(-PinOffset + PinWidth/2), \
 	mm2mils100(BodyHeight - 21.2), \
	mm2mils100(-PinOffset + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin33" "33" 0x0100]'

print '   Pad[',\
 	mm2mils100(BodyHeight - 20.1), \
	mm2mils100(BodyWidth + PinOffset - PinWidth/2), \
 	mm2mils100(BodyHeight - 20.1), \
	mm2mils100(BodyWidth + PinOffset - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(BodyHeight - 20.1), \
	mm2mils100(-PinOffset + PinWidth/2), \
 	mm2mils100(BodyHeight - 20.1), \
	mm2mils100(-PinOffset + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin32" "32" 0x0100]'

print '   Pad[',\
 	mm2mils100(BodyHeight - 13.9), \
	mm2mils100(BodyWidth + PinOffset - PinWidth/2), \
 	mm2mils100(BodyHeight - 13.9), \
	mm2mils100(BodyWidth + PinOffset - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin3" "3" 0x0100]'

print '   Pad[',\
 	mm2mils100(BodyHeight - 12.8), \
	mm2mils100(BodyWidth + PinOffset - PinWidth/2), \
 	mm2mils100(BodyHeight - 12.8), \
	mm2mils100(BodyWidth + PinOffset - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin4" "4" 0x0100]'

for pin in range (5,15):
    print '   Pad[',\
 	mm2mils100(BodyHeight - 11.7 + ((pin - 5) * PinSpacing)), \
	mm2mils100(BodyWidth + PinOffset - PinWidth/2), \
 	mm2mils100(BodyHeight - 11.7 + ((pin - 5) * PinSpacing)), \
	mm2mils100(BodyWidth + PinOffset - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % pin, '"%i"' % pin, '0x0100]'

    print '   Pad[',\
 	mm2mils100(BodyHeight - 11.7 + ((pin - 5) * PinSpacing)), \
	mm2mils100(- PinOffset + PinWidth/2), \
 	mm2mils100(BodyHeight - 11.7 + ((pin - 5) * PinSpacing)), \
	mm2mils100(- PinOffset + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (36 - pin), '"%i"' % (36 - pin), '0x0100]'

for pin in range (15,22):
    print '   Pad[',\
	mm2mils100(BodyHeight + PinOffset - PinWidth/2), \
 	mm2mils100(BodyWidth - 2.7 + (-(pin - 15) * PinSpacing)), \
	mm2mils100(BodyHeight - PinHeight + PinOffset + PinWidth/2), \
 	mm2mils100(BodyWidth - 2.7 + (-(pin - 15) * PinSpacing)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % pin, '"%i"' % pin, '0x0100]'


# body outline

print '   ElementLine[',\
	0, \
	0, \
	0, \
	mm2mils100(BodyWidth), \
	'1000 ]'

print '   ElementLine[',\
	0, \
	mm2mils100(BodyWidth), \
	mm2mils100(BodyHeight), \
	mm2mils100(BodyWidth), \
	'1000 ]'

print '   ElementLine[',\
	mm2mils100(BodyHeight), \
	mm2mils100(BodyWidth), \
	mm2mils100(BodyHeight), \
	0, \
	'1000 ]'

print '   ElementLine[',\
	mm2mils100(BodyHeight), \
	0, \
	0, \
	0, \
	'1000 ]'

# hash marks where gnd plane should end

print '   ElementLine[',\
	mm2mils100(BodyHeight-GndEdgeLine), \
	mm2mils100(BodyWidth-1), \
	mm2mils100(BodyHeight-GndEdgeLine), \
	mm2mils100(BodyWidth-3), \
	'1000 ]'

print '   ElementLine[',\
	mm2mils100(BodyHeight-GndEdgeLine), \
	mm2mils100(1), \
	mm2mils100(BodyHeight-GndEdgeLine), \
	mm2mils100(3), \
	'1000 ]'

print ")"
