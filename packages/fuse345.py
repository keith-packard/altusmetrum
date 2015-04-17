#!/usr/bin/python
# Copyright 2015 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for littlefuse 345 fuse holder
#

# dimensions in mils from footprint drawing at DigiKey
BodyWidth = 1570		# body outline (width not counting projection)
BodyHeight = 490
PinSpace1 = 700
PinSpace2 = 600

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "littlefuse345" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pin(',\
 	0, \
	0, \
 	125, \
	30, \
	150, \
	56, \
	'"pin1" "1" 0x0001)'

print '   Pin(',\
	PinSpace1, \
	0, \
 	125, \
	30, \
	150, \
	56, \
	'"pin2" "2" 0x0001)'

print '   Pin(',\
	PinSpace1 + PinSpace2, \
	0, \
 	125, \
	30, \
	150, \
	56, \
	'"pin3" "3" 0x0001)'


print '   ElementLine(',\
 	0, \
 	-(BodyHeight/2), \
 	0, \
 	(BodyHeight/2), \
	5, \
	')'

print '   ElementLine(',\
 	0, \
 	-(BodyHeight/2), \
 	BodyWidth, \
 	-(BodyHeight/2), \
	5, \
	')'

print '   ElementLine(',\
 	0, \
 	(BodyHeight/2), \
 	BodyWidth, \
 	(BodyHeight/2), \
	5, \
	')'

print ")"
