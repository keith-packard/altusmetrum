#!/usr/bin/python
# Copyright 2017 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for TI ADS124S0X in LQFP32 package
#

# TI doesn't provide a recommended footprint for this package, and instead
# points to IPC standards.  Searching on those yielded a LTC packaging 
# datasheet TQFP_32_05-08-1735.pdf, so dimensions in mm taken from that.

PinWidth = 0.27
PinHeight = 1.3
PinSpacing = 0.5
Inside = 5.2		# size of square inside rows of pins

BodySize = 5.0		# size of package for square in silk

# tweaked resist to get 4 mils width between pads to meet OshPark rules
PinResist = PinWidth + (2 * 0.063)

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3'
print '# use-license: unlimited'

print 'Element[0x0 "S-PQFP-G32" "" "" 0 0 0 0 0 100 0x0]'
print "("

# pins
for pin in range (1,9):
    print '   Pad[',\
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(-Inside/2 - PinWidth/2), \
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(-Inside/2 - PinHeight + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (9-pin), '"%i"' % (9-pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(+Inside/2 + PinHeight - PinWidth/2), \
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(+Inside/2 + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (16+pin), '"%i"' % (16+pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(Inside/2 + PinHeight - PinWidth/2), \
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(Inside/2 + PinWidth/2), \
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (33-pin), '"%i"' % (33-pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(-Inside/2 - PinWidth/2), \
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(-Inside/2 - PinHeight + PinWidth/2), \
 	mm2mils100((pin - 4.5) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (8+pin), '"%i"' % (8+pin), '0x0100]'


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
