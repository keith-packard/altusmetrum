#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for TDK beeper
#

# dimensions in mm from abm8.pdf Abracon datasheet
BodyDiam = 12.2
PinSpacing = 5.00

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "TDK_PS12" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pin[',\
 	mm2mils100(-PinSpacing/2), \
	0, \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(0.70), \
	'"pin1" "1" 0x0101]'

print '   Pin[',\
 	mm2mils100(PinSpacing/2), \
	0, \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(0.70), \
	'"pin2" "2" 0x0001]'

print '   ElementArc[',\
 	0, \
	0, \
 	mm2mils100(BodyDiam/2), \
	mm2mils100(BodyDiam/2), \
	0, \
	360, \
	1000, \
	']'

print ")"
