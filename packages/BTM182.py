#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Rayson BTM-182 Bluetooth module
#

# dimensions in mm from BTM182\ DataSheet.pdf 

BodyWidth = 14.50
BodyHeight = 25.00

PinWidth = 0.90
PinHeight = 1.60
PinSpacing = 1.27
RowCenters = 14.50
RowSpacing = RowCenters - PinHeight
BodyOffset = 2.88

SmallPinWidth = 1.20
SmallPinHeight = 0.80

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "BTM182" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
for pin in range (0,15):
    print '   Pad[',\
 	mm2mils100((pin-7) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-7) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (30 - pin), '"%i"' % (30 - pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((pin-7) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-7) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '0x0100]'

print '   Pad[',\
 	mm2mils100(-(9.44+SmallPinWidth/2-SmallPinHeight)), \
	mm2mils100(RowCenters/2 - 2.96), \
 	mm2mils100(-(9.44-SmallPinWidth/2+SmallPinHeight)), \
	mm2mils100(RowCenters/2 - 2.96), \
	mm2mils100(SmallPinHeight), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(SmallPinHeight)+600, \
	'"pin%i"' % 31, '"%i"' % 31, '0x0100]'

print '   Pad[',\
 	mm2mils100(-(9.44+SmallPinWidth/2-SmallPinHeight)), \
	mm2mils100(RowCenters/2 - 1.69), \
 	mm2mils100(-(9.44-SmallPinWidth/2+SmallPinHeight)), \
	mm2mils100(RowCenters/2 - 1.69), \
	mm2mils100(SmallPinHeight), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(SmallPinHeight)+600, \
	'"pin%i"' % 32, '"%i"' % 32, '0x0100]'

print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2-BodyOffset), \
	mm2mils100(-BodyWidth/2), \
	mm2mils100(-BodyHeight/2-BodyOffset), \
	mm2mils100( BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2-BodyOffset), \
	mm2mils100( BodyWidth/2), \
	mm2mils100(-BodyHeight/2-BodyOffset+5.13), \
	mm2mils100( BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
	mm2mils100(-BodyHeight/2-BodyOffset+5.13), \
	mm2mils100( BodyWidth/2), \
	mm2mils100(-BodyHeight/2-BodyOffset+5.13), \
	mm2mils100( BodyWidth/2-3.595), \
	'1000 ]'

print '   ElementLine[',\
	mm2mils100(-BodyHeight/2-BodyOffset+5.13), \
	mm2mils100( BodyWidth/2-3.595), \
 	mm2mils100(-BodyHeight/2-BodyOffset+5.13+0.76), \
	mm2mils100( BodyWidth/2-3.595), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2-BodyOffset+5.13+0.76), \
	mm2mils100( BodyWidth/2), \
 	mm2mils100(-BodyHeight/2-BodyOffset+5.13+0.76), \
	mm2mils100( BodyWidth/2-3.595), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2-BodyOffset+5.13+0.76), \
	mm2mils100( BodyWidth/2), \
	mm2mils100( BodyHeight/2-BodyOffset), \
	mm2mils100( BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodyHeight/2-BodyOffset), \
	mm2mils100( BodyWidth/2), \
	mm2mils100( BodyHeight/2-BodyOffset), \
	mm2mils100(-BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodyHeight/2-BodyOffset), \
	mm2mils100(-BodyWidth/2), \
	mm2mils100(-BodyHeight/2-BodyOffset), \
	mm2mils100(-BodyWidth/2), \
	'1000 ]'

print '   ElementArc[',\
	mm2mils100(-7 * PinSpacing), \
	mm2mils100(RowSpacing/2-PinHeight/6), \
	'500 500 0 360 1000 ]'

print ")"
