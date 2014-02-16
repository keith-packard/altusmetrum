#!/usr/bin/python
# Copyright 2014 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for edge-launch wire antenna
#

# dimensions in 1/100 mil from CONSMA003.062.pdf datasheet, modified to
# accomidate a wider range of new and surplus edge-launched SMA connectors
PinWidth =    6000	# the center pin
GndWidth =   15000	# the "side" pins for the gnd "wings" 
PinHeight =  15000
PinSpacing = PinWidth / 2 + 4000

import sys

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "wire-ant" "" "" 0 0 0 0 0 0 0x0]'
print "("

print '   Pad[',\
 	(-PinSpacing - GndWidth/2), \
	(GndWidth/2), \
 	(-PinSpacing - GndWidth/2), \
	(PinHeight - GndWidth/2), \
	(GndWidth), \
	0, \
  	(GndWidth + 600), \
	'"pin2"', '"2"', '"square,nopaste"]'
print '   Pad[',\
 	0, \
	(PinWidth/2), \
 	0, \
	(PinHeight - PinWidth/2), \
	(PinWidth), \
	0, \
  	(PinWidth + 600), \
	'"pin1"', '"1"', '"square,nopaste"]'
print '   Pad[',\
 	(PinSpacing + GndWidth/2), \
	(GndWidth/2), \
 	(PinSpacing + GndWidth/2), \
	(PinHeight - GndWidth/2), \
	(GndWidth), \
	0, \
  	(GndWidth + 600), \
	'"pin2"', '"2"', '"square,nopaste"]'

print ")"
