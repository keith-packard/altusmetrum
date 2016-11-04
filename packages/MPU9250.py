#!/usr/bin/python
# Copyright 2016 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for 3x3x1mm QFN24 package used by MPU-9250
#

# dimensions in mm from Invensense MPU-9250-Datasheet.pdf
PinWidth = 0.20		
PinResist = PinWidth + (2 * 0.07)
PinHeight = 0.30
PinSpacing = 0.40
Overall = 3.80

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "ITG3200" "" "" 0 0 0 0 0 100 0x0]'
print "("

# pins
for pin in range (1,7):
    print '   Pad[',\
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (19-pin), '"%i"' % (19-pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(+Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(+Overall/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % pin, '"%i"' % pin, '0x0100]'

    print '   Pad[',\
	mm2mils100(Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(Overall/2 - PinWidth/2), \
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (13-pin), '"%i"' % (13-pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
 	mm2mils100((-3.5 + pin) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (18+pin), '"%i"' % (18+pin), '0x0100]'

print '   ElementArc[',\
	mm2mils100(-(Overall/2)), \
	mm2mils100(Overall/2), \
	'500 500 0 360 1000 ]'
print ")"
