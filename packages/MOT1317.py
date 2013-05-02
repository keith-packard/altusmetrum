#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Motorola 1317 package used by MP3H6115A
#

# dimensions in mm from MP3H6115A.pdf Motorola packaging datasheet
PinWidth = 0.69
PinHeight = 1.35
PinSpacing = 1.27
RowCenters = 9.83
RowSpacing = RowCenters - PinHeight
BodySize = 7.4

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "MOT1317" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
for pin in range (0,4):
    print '   Pad[',\
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (8 - pin), '"%i"' % (8 - pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-1.5) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '0x0100]'

print '   ElementLine[',\
 	mm2mils100(-BodySize/2), \
	mm2mils100(-BodySize/2), \
	mm2mils100(-BodySize/2), \
	mm2mils100( BodySize/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-BodySize/2), \
	mm2mils100( BodySize/2), \
	mm2mils100( BodySize/2), \
	mm2mils100( BodySize/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodySize/2), \
	mm2mils100( BodySize/2), \
	mm2mils100( BodySize/2), \
	mm2mils100(-BodySize/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodySize/2), \
	mm2mils100(-BodySize/2), \
	mm2mils100(-BodySize/2), \
	mm2mils100(-BodySize/2), \
	'1000 ]'

print '   ElementArc[',\
        mm2mils100(-2.5 * PinSpacing), \
        mm2mils100(RowSpacing/2), \
	'500 500 0 360 1000 ]'

print ")"
