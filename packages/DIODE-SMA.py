#!/usr/bin/python
# Copyright 2012 by Bdale Garbee <bdale@gag.com>.  GPLv3
#
# Program to emit PCB footprint for SMA package used by Diodes, Inc
#

# dimensions in mm from ds16003.pdf
PinWidth = 2.50
PinHeight = 1.70
PinSpacing = 1.50

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "DIODE-SMA" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(-PinSpacing/2 - PinWidth + PinHeight/2), \
	0, \
 	mm2mils100(-PinSpacing/2 - PinHeight/2), \
 	0, \
	mm2mils100(PinHeight), \
	0, \
	mm2mils100(PinHeight+0.4), \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(PinSpacing/2 + PinWidth - PinHeight/2), \
	0, \
 	mm2mils100(PinSpacing/2 + PinHeight/2), \
 	0, \
	mm2mils100(PinHeight), \
	0, \
	mm2mils100(PinHeight+0.4), \
	'"pin2" "2" 0x0100]'

print '   ElementLine[',\
        mm2mils100(PinSpacing * 2.5), \
        mm2mils100(-PinHeight/2), \
        mm2mils100(PinSpacing * 2.5), \
        mm2mils100(PinHeight/2), \
        '1000 ]'

print ")"
