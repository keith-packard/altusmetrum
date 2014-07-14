#!/usr/bin/python
# Copyright 2014 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for 8mm diameter Panasonic FC series 
# through-hole electrolytic capacitors
#

# dimensions in mm from Panasonic ABA0000CE22.pdf
BodyDiam = 8.0
PinSpacing = 3.5

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "CAP_FC8" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pin[',\
 	mm2mils100(-PinSpacing/2), \
	0, \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(0.80), \
	'"pin1" "1" 0x0101]'

print '   Pin[',\
 	mm2mils100(PinSpacing/2), \
	0, \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(0.80), \
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

print '   ElementLine[',\
 	mm2mils100(-BodyDiam/2), \
 	mm2mils100(-BodyDiam/2), \
 	mm2mils100(-BodyDiam/4), \
 	mm2mils100(-BodyDiam/2), \
	1000, \
	']'

print '   ElementLine[',\
 	mm2mils100(-3*BodyDiam/8), \
 	mm2mils100(-5*BodyDiam/8), \
 	mm2mils100(-3*BodyDiam/8), \
 	mm2mils100(-3*BodyDiam/8), \
	1000, \
	']'

print ")"
