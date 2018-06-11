#!/usr/bin/python
# Copyright 2018 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for Omnetics A29100-009 connector

# dimensions in mm from A29100-009 datasheet

PinDiam = 1.78
PinSpacing = 6.86
PinOffset = 1.88
ARing = 0.8
Clearance = 0.36

PadHeight = 1.07
PadWidth = 0.43
PadRowSpacing = 1.27
Row1Spacing = 2.54 / 4.0
Row2Spacing = 1.91 / 3.0

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3+'
print '# use-license: unlimited'

print 'Element[0x0 "A29100-009" "" "" 0 0 0 0 0 100 0x0]'
print "("

for pad in range (0,5):
    print '   Pad[',\
 	mm2mils100((pad-2) * Row1Spacing), \
 	mm2mils100(PadHeight/2 - PadWidth/2), \
 	mm2mils100((pad-2) * Row1Spacing), \
 	mm2mils100(-PadHeight/2 + PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin%i"' % (pad+1), '"%i"' % (pad+1), '0x0100]'

for pad in range (0,4):
    print '   Pad[',\
 	mm2mils100((pad-1.5) * Row2Spacing), \
 	mm2mils100(-PadRowSpacing - PadHeight/2 + PadWidth/2), \
 	mm2mils100((pad-1.5) * Row2Spacing), \
 	mm2mils100(-PadRowSpacing + PadHeight/2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin%i"' % (pad+6), '"%i"' % (pad+6), '0x0100]'

print '   Pin[',\
        mm2mils100(PinSpacing/2), \
        mm2mils100(PinOffset), \
        mm2mils100(PinDiam+ARing), \
        mm2mils100(Clearance), \
        mm2mils100(PinDiam+ARing+Clearance ), \
        mm2mils100(PinDiam), \
        '"mnt" "G" 0x0000]'

print '   Pin[',\
        mm2mils100(-PinSpacing/2), \
        mm2mils100(PinOffset), \
        mm2mils100(PinDiam+ARing), \
        mm2mils100(Clearance), \
        mm2mils100(PinDiam+ARing+Clearance ), \
        mm2mils100(PinDiam), \
        '"mnt" "G" 0x0000]'

print ")"
