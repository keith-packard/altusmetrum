#!/usr/bin/python
# Copyright 2015 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Omron G5RL-1A-E relays
#

# dimensions in mm from footprint drawing in en-g5rl-531959.pdf
BodyWidth = 29			# body outline
BodyHeight = 12.7
PinSpace1 = 20.0
PinSpace2 = 5.0
RowSpace = 7.5
BackSpace = 2.3

Drill = 1.30
Thickness = 2.0 * Drill
Clearance = 1.0
Mask = Thickness + 0.3

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "G5RL-1A-E" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pin[',\
 	mm2mils100(0), \
 	mm2mils100(RowSpace/2), \
 	mm2mils100(Thickness), \
	mm2mils100(Clearance), \
	mm2mils100(Mask), \
	mm2mils100(Drill), \
	'"pin1" "1" 0x0001]'

print '   Pin[',\
 	mm2mils100(PinSpace1), \
 	mm2mils100(RowSpace/2), \
 	mm2mils100(Thickness), \
	mm2mils100(Clearance), \
	mm2mils100(Mask), \
	mm2mils100(Drill), \
	'"pin3" "3" 0x0001]'

print '   Pin[',\
 	mm2mils100(PinSpace1 + PinSpace2), \
 	mm2mils100(RowSpace/2), \
 	mm2mils100(Thickness), \
	mm2mils100(Clearance), \
	mm2mils100(Mask), \
	mm2mils100(Drill), \
	'"pin4" "4" 0x0001]'

print '   Pin[',\
 	mm2mils100(0), \
	mm2mils100(-RowSpace/2), \
 	mm2mils100(Thickness), \
	mm2mils100(Clearance), \
	mm2mils100(Mask), \
	mm2mils100(Drill), \
	'"pin8" "8" 0x0001]'

print '   Pin[',\
 	mm2mils100(PinSpace1), \
 	mm2mils100(-RowSpace/2), \
 	mm2mils100(Thickness), \
	mm2mils100(Clearance), \
	mm2mils100(Mask), \
	mm2mils100(Drill), \
	'"pin6" "6" 0x0001]'

print '   Pin[',\
 	mm2mils100(PinSpace1 + PinSpace2), \
 	mm2mils100(-RowSpace/2), \
 	mm2mils100(Thickness), \
	mm2mils100(Clearance), \
	mm2mils100(Mask), \
	mm2mils100(Drill), \
	'"pin5" "5" 0x0001]'


print '   ElementLine[',\
 	-mm2mils100(BackSpace), \
 	-mm2mils100(BodyHeight/2), \
 	mm2mils100(BodyWidth-BackSpace), \
 	-mm2mils100(BodyHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	-mm2mils100(BackSpace), \
 	mm2mils100(BodyHeight/2), \
 	mm2mils100(BodyWidth-BackSpace), \
 	mm2mils100(BodyHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	-mm2mils100(BackSpace), \
 	mm2mils100(BodyHeight/2), \
 	-mm2mils100(BackSpace), \
 	-mm2mils100(BodyHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	mm2mils100(BodyWidth-BackSpace), \
 	mm2mils100(BodyHeight/2), \
 	mm2mils100(BodyWidth-BackSpace), \
 	-mm2mils100(BodyHeight/2), \
	500, \
	']'

print ")"
