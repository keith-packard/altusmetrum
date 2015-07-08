#!/usr/bin/python
# Copyright 2015 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Emit PCB footprint for TO-252AA parts from International Rectifier
#

# dimensions in mm from ir/dpakfootprint.pdf

PinWidth = 1.50
PinHeight = 2.50
PinSpacing = 4.60

PadSquare = 7.00
Pad2Pin = 6.90

BodyWidth = 7.00
BodyHeight = 10.50
BodyOffset = 1.90

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3'
print '# use-license: unlimited'

print 'Element[0x0 "TO252AA" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(0), \
	mm2mils100(0), \
 	mm2mils100(0), \
	mm2mils100(0), \
	mm2mils100(PadSquare), \
	mm2mils100(1.5), \
	mm2mils100(PadSquare+0.4), \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(-PinSpacing/2 - PinWidth/2), \
	mm2mils100(Pad2Pin + PinWidth/2), \
 	mm2mils100(-PinSpacing/2 - PinWidth/2), \
	mm2mils100(Pad2Pin - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(1.5), \
	mm2mils100(PinWidth+0.4), \
	'"pin3" "3" 0x0100]'

print '   Pad[',\
 	mm2mils100(PinSpacing/2 + PinWidth/2), \
	mm2mils100(Pad2Pin + PinWidth/2), \
 	mm2mils100(PinSpacing/2 + PinWidth/2), \
	mm2mils100(Pad2Pin - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(1.5), \
	mm2mils100(PinWidth+0.4), \
	'"pin2" "2" 0x0100]'

print '   ElementLine[',\
        mm2mils100(-BodyWidth/2), \
        mm2mils100(BodyOffset - BodyHeight/2), \
        mm2mils100(BodyWidth/2), \
        mm2mils100(BodyOffset - BodyHeight/2), \
        '1000 ]'

print '   ElementLine[',\
        mm2mils100(-BodyWidth/2), \
        mm2mils100(BodyOffset + BodyHeight/2), \
        mm2mils100(BodyWidth/2), \
        mm2mils100(BodyOffset + BodyHeight/2), \
        '1000 ]'

print '   ElementLine[',\
        mm2mils100(BodyWidth/2), \
        mm2mils100(BodyOffset - BodyHeight/2), \
        mm2mils100(BodyWidth/2), \
        mm2mils100(BodyOffset + BodyHeight/2), \
        '1000 ]'

print '   ElementLine[',\
        mm2mils100(-BodyWidth/2), \
        mm2mils100(BodyOffset - BodyHeight/2), \
        mm2mils100(-BodyWidth/2), \
        mm2mils100(BodyOffset + BodyHeight/2), \
        '1000 ]'

print ")"
