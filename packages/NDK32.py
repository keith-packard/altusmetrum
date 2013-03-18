#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for package used by NDK 32mhz crystal
#

# dimensions in mm from abm8.pdf Abracon datasheet
PinHeight = 1.40
PinWidth = 1.20
HSpacing = 2.20 - 1.40
WSpacing = 1.6 - 1.20

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "NDK32" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(-(HSpacing/2 + PinWidth/2)), \
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(-(HSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth)+600, \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(HSpacing/2 + PinWidth/2), \
 	mm2mils100(WSpacing/2 + PinWidth/2), \
	mm2mils100(HSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(HSpacing/2 + PinWidth/2), \
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(HSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth)+600, \
	'"pin4" "4" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(-(HSpacing/2 + PinWidth/2)), \
 	mm2mils100(-(WSpacing/2 + PinWidth/2)), \
	mm2mils100(-(HSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth)+600, \
	'"pin3" "3" 0x0100]'

print '   ElementArc[',\
	mm2mils100(PinWidth*1.4), \
	mm2mils100(PinHeight*1.4), \
	'500 500 0 360 1000 ]'

print ")"
