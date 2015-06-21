#!/usr/bin/python
# Copyright 2015 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for BU2032 battery holder by Memory Protection Devices
#

# dimensions in mm from mpd/BU2032SM-BT-GTR-datasheet.pdf

PinWidth = 3.20
PinHeight = 4.20
PinSpacing = 26.10
BodyDiam = 22.40
BodyWidth = 31.86
BodyHeight = 7.00

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3'
print '# use-license: unlimited'

print 'Element[0x0 "BU2032" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(-PinSpacing/2 - PinWidth/2), \
	mm2mils100(-PinHeight/2 + PinWidth/2), \
 	mm2mils100(-PinSpacing/2 - PinWidth/2), \
	mm2mils100(PinHeight/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(1.5), \
	mm2mils100(PinWidth+0.4), \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(PinSpacing/2 + PinWidth/2), \
	mm2mils100(-PinHeight/2 + PinWidth/2), \
 	mm2mils100(PinSpacing/2 + PinWidth/2), \
	mm2mils100(PinHeight/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(1.5), \
	mm2mils100(PinWidth+0.4), \
	'"pin2" "2" 0x0100]'

print '   ElementArc[',\
 	0, \
	0, \
 	mm2mils100(BodyDiam/2), \
	mm2mils100(BodyDiam/2), \
	0, \
	360, \
	1000, \
	']'

print '   ElementLine[',\
        mm2mils100(-BodyWidth/2), \
        mm2mils100(-BodyHeight/2), \
        mm2mils100(BodyWidth/2), \
        mm2mils100(-BodyHeight/2), \
        '1000 ]'

print '   ElementLine[',\
        mm2mils100(-BodyWidth/2), \
        mm2mils100(BodyHeight/2), \
        mm2mils100(BodyWidth/2), \
        mm2mils100(BodyHeight/2), \
        '1000 ]'

print '   ElementLine[',\
        mm2mils100(BodyWidth/2), \
        mm2mils100(-BodyHeight/2), \
        mm2mils100(BodyWidth/2), \
        mm2mils100(BodyHeight/2), \
        '1000 ]'

print '   ElementLine[',\
        mm2mils100(-BodyWidth/2), \
        mm2mils100(-BodyHeight/2), \
        mm2mils100(-BodyWidth/2), \
        mm2mils100(BodyHeight/2), \
        '1000 ]'

print ")"
