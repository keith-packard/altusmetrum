#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for STM32L151 LQFP100 14 x 14 mm package
#

# dimensions in mm from STM32L151 data sheet 
PinWidth = 0.3
PinHeight = 1.2
PinResist = PinWidth + 0.16
PinSpacing = 0.5
BodySize = 10
Overall = 12.7

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "LQFP100" "" "" 0 0 0 0 0 100 0x0]'
print "("

# pins
for pin in range (1,17):
    print '   Pad[',\
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (17-pin), '"%i"' % (17-pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(+Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(+Overall/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (32+pin), '"%i"' % (32+pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(Overall/2 - PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (65-pin), '"%i"' % (65-pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (16+pin), '"%i"' % (16+pin), '0x0100]'


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
	mm2mils100(  (BodySize/2)+0.3), \
	mm2mils100(-((BodySize/2)+0.3)), \
	'500 500 0 360 1000 ]'
print ")"
