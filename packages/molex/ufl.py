#!/usr/bin/python
# Copyright 2009 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Molex version of U.FL micro coax connector
#

# dimensions in mm from 734120110_sd.pdf datasheet
PinWidth =   1.00
PinHeight =  1.05
PinOffset =  1.00
GndHeight =  2.20
GndInside =  1.90
GndOutside = 4.00
GndWidth = (GndOutside - GndInside) / 2

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "UFL" "" "" 0 0 0 0 0 100 0x0]'
print "("

print '   Pad[',\
 	mm2mils100(-(GndOutside - GndInside)/4 - (GndInside / 2) ), \
	mm2mils100(-(GndHeight / 2) + (GndWidth / 2)), \
 	mm2mils100(-(GndOutside - GndInside)/4 - (GndInside / 2) ), \
	mm2mils100((GndHeight / 2) - (GndWidth / 2)), \
	mm2mils100(GndWidth), \
	mm2mils100(0.1), \
  	mm2mils100(GndWidth+0.2), \
	'"pin2"', '"2"', '0x0100]'

print '   Pad[',\
 	0, \
	mm2mils100(PinOffset + PinWidth/2), \
 	0, \
	mm2mils100(PinOffset + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(0.1), \
  	mm2mils100(PinWidth+0.2), \
	'"pin1"', '"1"', '0x0100]'

print '   Pad[',\
 	mm2mils100((GndOutside - GndInside)/4 + (GndInside / 2) ), \
	mm2mils100(-(GndHeight / 2) + (GndWidth / 2)), \
 	mm2mils100((GndOutside - GndInside)/4 + (GndInside / 2) ), \
	mm2mils100((GndHeight / 2) - (GndWidth / 2)), \
	mm2mils100(GndWidth), \
	mm2mils100(0.1), \
  	mm2mils100(GndWidth+0.2), \
	'"pin2"', '"2"', '0x0100]'


print ")"
