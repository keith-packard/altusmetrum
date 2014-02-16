#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for C&K PCM12SMTR SPDT switch
#

# dimensions in mm from C&K datasheet
PinHeight = 1.5
PinWidth = 0.7
Pin12 = 3.0
Pin23 = 1.5
Pin2Offset = 0.75
PinBase = 1.0

PadHeight = 0.8
PadWidth = 1.0
HSpacing = 1.4
WSpacing = 6.3

HoleSize = 0.9
HoleSpacing = 3.0

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "PCM12SMTR" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(WSpacing/2 + PadHeight/2), \
	mm2mils100(-HSpacing/2 - PadHeight/2), \
 	mm2mils100(WSpacing/2 + PadWidth - PadHeight/2), \
	mm2mils100(-HSpacing/2 - PadHeight/2), \
	mm2mils100(PadHeight), \
	mm2mils100(WSpacing - PadWidth), \
  	mm2mils100(PadWidth)+600, \
	'"mnt" "M" 0x0100]'

print '   Pad[',\
 	mm2mils100(WSpacing/2 + PadHeight/2), \
	mm2mils100(HSpacing/2 + PadHeight/2), \
 	mm2mils100(WSpacing/2 + PadWidth - PadHeight/2), \
	mm2mils100(HSpacing/2 + PadHeight/2), \
	mm2mils100(PadHeight), \
	mm2mils100(WSpacing - PadWidth), \
  	mm2mils100(PadWidth)+600, \
	'"mnt" "M" 0x0100]'

print '   Pad[',\
 	mm2mils100(-WSpacing/2 - PadHeight/2), \
	mm2mils100(HSpacing/2 + PadHeight/2), \
 	mm2mils100(-WSpacing/2 - PadWidth + PadHeight/2), \
	mm2mils100(HSpacing/2 + PadHeight/2), \
	mm2mils100(PadHeight), \
	mm2mils100(WSpacing - PadWidth), \
  	mm2mils100(PadWidth)+600, \
	'"mnt" "M" 0x0100]'

print '   Pad[',\
 	mm2mils100(-WSpacing/2 - PadHeight/2), \
	mm2mils100(-HSpacing/2 - PadHeight/2), \
 	mm2mils100(-WSpacing/2 - PadWidth + PadHeight/2), \
	mm2mils100(-HSpacing/2 - PadHeight/2), \
	mm2mils100(PadHeight), \
	mm2mils100(WSpacing - PadWidth), \
  	mm2mils100(PadWidth)+600, \
	'"mnt" "M" 0x0100]'

print '   Pin[',\
        mm2mils100(-HoleSpacing/2), \
        mm2mils100(0), \
        mm2mils100(HoleSize+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(HoleSize+0.66), \
        mm2mils100(HoleSize), \
        '"mnt" "G" 0x0000]'

print '   Pin[',\
        mm2mils100(HoleSpacing/2), \
        mm2mils100(0), \
        mm2mils100(HoleSize+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(HoleSize+0.66), \
        mm2mils100(HoleSize), \
        '"mnt" "G" 0x0000]'

print '   Pad[',\
 	mm2mils100(Pin2Offset - Pin12), \
	mm2mils100(- PinBase - (PinWidth/2)), \
 	mm2mils100(Pin2Offset - Pin12), \
	mm2mils100(- PinBase - PinHeight + (PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(.1524), \
  	mm2mils100(PinWidth + .1524), \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(Pin2Offset), \
	mm2mils100(- PinBase - (PinWidth/2)), \
 	mm2mils100(Pin2Offset), \
	mm2mils100(- PinBase - PinHeight + (PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(.1524), \
  	mm2mils100(PinWidth + .1524), \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(Pin2Offset + Pin23), \
	mm2mils100(- PinBase - (PinWidth/2)), \
 	mm2mils100(Pin2Offset + Pin23), \
	mm2mils100(- PinBase - PinHeight + (PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(.1524), \
  	mm2mils100(PinWidth + .1524), \
	'"pin3" "3" 0x0100]'


print ")"
