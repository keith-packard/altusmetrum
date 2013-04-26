#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for C&K KSCJ SPST switch
#

# dimensions in mm from C&K KSC_31aug10.pdf datasheet

PadHeight = 1.0
PadWidth = 2.8
HSpacing = 4.0
WSpacing = 3.0

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "PCM12SMTR" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(WSpacing/2 + PadHeight/2), \
	mm2mils100(-HSpacing/2), \
 	mm2mils100(WSpacing/2 + PadWidth - PadHeight/2), \
	mm2mils100(-HSpacing/2), \
	mm2mils100(PadHeight), \
	0, \
  	mm2mils100(PadHeight)+600, \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(WSpacing/2 + PadHeight/2), \
	mm2mils100(HSpacing/2), \
 	mm2mils100(WSpacing/2 + PadWidth - PadHeight/2), \
	mm2mils100(HSpacing/2), \
	mm2mils100(PadHeight), \
	0, \
  	mm2mils100(PadHeight)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(-WSpacing/2 - PadHeight/2), \
	mm2mils100(HSpacing/2), \
 	mm2mils100(-WSpacing/2 - PadWidth + PadHeight/2), \
	mm2mils100(HSpacing/2), \
	mm2mils100(PadHeight), \
	0, \
  	mm2mils100(PadHeight)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(-WSpacing/2 - PadHeight/2), \
	mm2mils100(-HSpacing/2), \
 	mm2mils100(-WSpacing/2 - PadWidth + PadHeight/2), \
	mm2mils100(-HSpacing/2), \
	mm2mils100(PadHeight), \
	0, \
  	mm2mils100(PadHeight)+600, \
	'"pin2" "2" 0x0100]'

print ")"
