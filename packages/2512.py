#!/usr/bin/python
# Copyright 2014 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for 2512 package used by Vishay resistors
#

# dimensions in mm from dcrcwe3.pdf
PinWidth = 1.00
PinHeight = 3.20
PinSpacing = 5.20

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "2512" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(-PinSpacing/2 - PinWidth/2), \
	mm2mils100(-PinHeight/2 + PinWidth/2), \
 	mm2mils100(-PinSpacing/2 - PinWidth/2), \
	mm2mils100(PinHeight/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	0, \
	mm2mils100(PinWidth+0.4), \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(PinSpacing/2 + PinWidth/2), \
	mm2mils100(-PinHeight/2 + PinWidth/2), \
 	mm2mils100(PinSpacing/2 + PinWidth/2), \
	mm2mils100(PinHeight/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	0, \
	mm2mils100(PinWidth+0.4), \
	'"pin2" "2" 0x0100]'

print '   ElementLine[',\
        mm2mils100(-PinSpacing/2 + 0.5), \
        mm2mils100(PinHeight/2), \
        mm2mils100(PinSpacing/2 - 0.5), \
        mm2mils100(PinHeight/2), \
        '1000 ]'

print '   ElementLine[',\
        mm2mils100(-PinSpacing/2 + 0.5), \
        mm2mils100(-PinHeight/2), \
        mm2mils100(PinSpacing/2 - 0.5), \
        mm2mils100(-PinHeight/2), \
        '1000 ]'

print ")"
