#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for 0605 dual LED
#

### WARNING 
### origin is on one corner, not in the center, so XYRS will be wrong!

PinHeight = 0.85
PinWidth = 0.65
HSpacing = 0.6
WSpacing = 0.2

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "0605" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(PinWidth/2), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(PinWidth/2), \
	mm2mils100(PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(PinWidth + WSpacing + PinWidth/2), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(PinWidth + WSpacing + PinWidth/2), \
	mm2mils100(PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(PinWidth/2), \
	mm2mils100(PinHeight + HSpacing + PinWidth/2), \
 	mm2mils100(PinWidth/2), \
	mm2mils100(PinHeight + HSpacing + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin4" "4" 0x0100]'

print '   Pad[',\
 	mm2mils100(PinWidth + WSpacing + PinWidth/2), \
	mm2mils100(PinHeight + HSpacing + PinWidth/2), \
 	mm2mils100(PinWidth + WSpacing + PinWidth/2), \
	mm2mils100(PinHeight + HSpacing + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(WSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin3" "3" 0x0100]'

print ")"
