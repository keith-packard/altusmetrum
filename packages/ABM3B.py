#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for ABM3B package used by Xtals
#

# dimensions in mm from abm3b.pdf Abracon datasheet
PinHeight = 1.80
PinWidth = 1.20
HSpacing = 4.0 - 1.8
WSpacing = 2.4 - 1.2

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "ABM3B" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(-(HSpacing/2 + PinWidth/2)), \
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(-(HSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(HSpacing/2 + PinWidth/2), \
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(HSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(HSpacing/2 + PinWidth/2), \
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(HSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin4" "4" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(-(HSpacing/2 + PinWidth/2)), \
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(-(HSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin3" "3" 0x0100]'

print '   ElementArc[',\
	mm2mils100(WSpacing*0.2), \
	mm2mils100(HSpacing/2+PinHeight*0.8), \
	'500 500 0 360 1000 ]'

print ")"