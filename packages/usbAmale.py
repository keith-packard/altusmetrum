#!/usr/bin/python
# Copyright 2014 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Keystone model 931 USB A male connector
#

# dimensions in mm from Keystone datasheet
TabDiam = 2.50
TabSpacing = 11.70

PinDiam = 1.10
PinSpacing = 4.60

PadHeight = 1.99
PadWidth = 1.10
Pad14 = 7.0
Pad23 = 2.0
PadRowOffset = 2.50
EdgeOffset = 2.90

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "usbAmale" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(Pad14/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(Pad14/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin4" "4" 0x0100]'

print '   Pad[',\
 	mm2mils100(-Pad14/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(-Pad14/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(Pad23/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(Pad23/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin3" "3" 0x0100]'

print '   Pad[',\
 	mm2mils100(-Pad23/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(-Pad23/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin2" "2" 0x0100]'

print '   Pin[',\
        mm2mils100(-PinSpacing/2), \
        mm2mils100(0), \
        mm2mils100(PinDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(PinDiam+0.66), \
        mm2mils100(PinDiam), \
        '"mnt" "G" 0x0000]'

print '   Pin[',\
        mm2mils100(PinSpacing/2), \
        mm2mils100(0), \
        mm2mils100(PinDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(PinDiam+0.66), \
        mm2mils100(PinDiam), \
        '"mnt" "G" 0x0000]'

print '   Pin[',\
        mm2mils100(-TabSpacing/2), \
        mm2mils100(0), \
        mm2mils100(TabDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(TabDiam+0.66), \
        mm2mils100(TabDiam), \
        '"mnt" "G" 0x0000]'

print '   Pin[',\
        mm2mils100(TabSpacing/2), \
        mm2mils100(0), \
        mm2mils100(TabDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(TabDiam+0.66), \
        mm2mils100(TabDiam), \
        '"mnt" "G" 0x0000]'

print '   ElementLine[',\
       mm2mils100(-TabSpacing/2), \
       mm2mils100(-EdgeOffset), \
       mm2mils100(TabSpacing/2), \
       mm2mils100(-EdgeOffset), \
       '1000 ]'

print ")"
