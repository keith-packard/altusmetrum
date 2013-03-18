#!/usr/bin/python
# Copyright 2012 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for LPCC 16 package used by HMC5883L
#

# dimensions in mm from DS00049AR.pdf Microchip packaging datasheet
PinWidth = 0.300
PinHeight = 0.450
PinSpacing = 0.500
Overall = 3.0

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "LPCC16" "" "" 0 0 0 0 0 100 0x0]'
print "("

for pin in range (1,5):
    print '   Pad[',\
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.1), \
	'"pin%i"' % (13-pin), '"%i"' % (13-pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(+Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(+Overall/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.1), \
	'"pin%i"' % pin, '"%i"' % pin, '0x0100]'

    print '   Pad[',\
	mm2mils100(Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(Overall/2 - PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.1), \
	'"pin%i"' % (9-pin), '"%i"' % (9-pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.1), \
	'"pin%i"' % (12+pin), '"%i"' % (12+pin), '0x0100]'

print '   ElementArc[',\
	mm2mils100(-Overall/2), \
	mm2mils100(Overall/2), \
	'500 500 0 360 1000 ]'
print ")"
