#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Pules Electronics W3011A GPS chip antenna
#
#   dimensions in mm from W3011.pdf
PinWidth = 0.80
PinHeight = 0.65
PadHeight = 1.60
PinSpacing = 2.40
ClearWidth = 4.00
ClearHeight = 6.25

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "W3011A" "" "" 0 0 0 0 0 100 0x0]'
print "("
# pad 1 (signal trace)
print '   Pad[',\
 	mm2mils100(+PinSpacing/2+PinHeight/2), \
	mm2mils100(1.60 - PinHeight/2), \
 	mm2mils100(+PinSpacing/2+PinWidth+PinHeight/2), \
	mm2mils100(1.60 - PinHeight/2), \
	mm2mils100(PinHeight), \
	0, \
  	mm2mils100(PinHeight + 0.1), \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(+PinSpacing/2+PinHeight/2), \
	mm2mils100(PinHeight/2), \
 	mm2mils100(+PinSpacing/2+PinWidth+PinHeight/2), \
	mm2mils100(PinHeight/2), \
	mm2mils100(PinHeight), \
	0, \
  	mm2mils100(PinHeight + 0.1), \
	'"pin2" "2" 0x0100]'

print '   Pad[',\
 	mm2mils100(-PinSpacing/2-PinWidth/2), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(-PinSpacing/2-PinWidth/2), \
	mm2mils100(PadHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	0, \
  	mm2mils100(PinWidth + 0.1), \
	'"pin3" "3" 0x0100]'

print '   ElementLine[',\
 	mm2mils100(ClearWidth/2), \
	mm2mils100(0), \
	mm2mils100(ClearWidth/2), \
	mm2mils100(ClearHeight), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-ClearWidth/2), \
	mm2mils100(0), \
	mm2mils100(-ClearWidth/2), \
	mm2mils100(ClearHeight), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-ClearWidth/2-0.2), \
	mm2mils100(0), \
	mm2mils100(ClearWidth/2+0.2), \
	mm2mils100(0), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-ClearWidth/2), \
	mm2mils100(ClearHeight), \
	mm2mils100(ClearWidth/2), \
	mm2mils100(ClearHeight), \
	'1000 ]'

print ")"
