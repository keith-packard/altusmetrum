#!/usr/bin/python
# Copyright 2016 by Bdale Garbee <bdale@gag.com>.  GPLv3+
#
# Program to emit PCB footprint for CUI MD-60S Mini DIN Connector
#

# dimensions in mm from footprint drawing at DigiKey
BodyWidth = 14.0		# body outline
BodyHeight = 12.4
InnerPinSpace = 2.6
OuterPinSpace = 6.8
PinDiam = 0.90
MntSetback = 4.7
Row1Setback = 8.5
Row2Setback = 11.0
MntDiam = 2.32			# round hole for rectangular tab
ARing = 0.8
Clearance = 0.36

LineWidth = 1000

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3+'
print '# use-license: unlimited'

print 'Element[0x0 "MD-60S" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pin[',\
 	mm2mils100(-InnerPinSpace/2), \
	mm2mils100(Row1Setback), \
 	mm2mils100(PinDiam+ARing), \
	mm2mils100(Clearance), \
	mm2mils100(PinDiam+ARing+Clearance), \
	mm2mils100(PinDiam), \
	'"pin1" "1" 0x0001]'

print '   Pin[',\
 	mm2mils100(InnerPinSpace/2), \
 	mm2mils100(Row1Setback), \
 	mm2mils100(PinDiam+ARing), \
	mm2mils100(Clearance), \
	mm2mils100(PinDiam+ARing+Clearance), \
	mm2mils100(PinDiam), \
	'"pin2" "2" 0x0001]'

print '   Pin[',\
 	mm2mils100(-OuterPinSpace/2), \
	mm2mils100(Row1Setback), \
 	mm2mils100(PinDiam+ARing), \
	mm2mils100(Clearance), \
	mm2mils100(PinDiam+ARing+Clearance), \
	mm2mils100(PinDiam), \
	'"pin3" "3" 0x0001]'

print '   Pin[',\
 	mm2mils100(OuterPinSpace/2), \
	mm2mils100(Row1Setback), \
 	mm2mils100(PinDiam+ARing), \
	mm2mils100(Clearance), \
	mm2mils100(PinDiam+ARing+Clearance), \
	mm2mils100(PinDiam), \
	'"pin4" "4" 0x0001]'

print '   Pin[',\
 	mm2mils100(-OuterPinSpace/2), \
	mm2mils100(Row2Setback), \
 	mm2mils100(PinDiam+ARing), \
	mm2mils100(Clearance), \
	mm2mils100(PinDiam+ARing+Clearance), \
	mm2mils100(PinDiam), \
	'"pin5" "5" 0x0001]'

print '   Pin[',\
 	mm2mils100(OuterPinSpace/2), \
	mm2mils100(Row2Setback), \
 	mm2mils100(PinDiam+ARing), \
	mm2mils100(Clearance), \
	mm2mils100(PinDiam+ARing+Clearance), \
	mm2mils100(PinDiam), \
	'"pin6" "6" 0x0001]'

print '   Pin[',\
 	0, \
	mm2mils100(MntSetback), \
 	mm2mils100(MntDiam+ARing), \
	mm2mils100(Clearance), \
	mm2mils100(MntDiam+ARing+Clearance), \
	mm2mils100(MntDiam), \
	'"pin7" "7" 0x0001]'

print '   ElementLine[',\
 	-mm2mils100(BodyWidth/2), \
 	0, \
 	mm2mils100(BodyWidth/2), \
 	0, \
	LineWidth, \
	']'
print '   ElementLine[',\
 	-mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight), \
 	mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight), \
	LineWidth, \
	']'
print '   ElementLine[',\
 	-mm2mils100(BodyWidth/2), \
	0, \
 	-mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight), \
	LineWidth, \
	']'
print '   ElementLine[',\
 	mm2mils100(BodyWidth/2), \
	0, \
 	mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight), \
	LineWidth, \
	']'

print ")"
