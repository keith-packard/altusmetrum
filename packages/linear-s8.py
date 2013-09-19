#!/usr/bin/python
# Copyright 2013 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Linear Technologies S8 footprint,
# which is used on parts like the LT1963A series.
#

# dimensions in inches from 1963aff.pdf 
PinWidth = 0.030
PinHeight = 0.045
PinSpacing = 0.050
RowSpacing = 0.160
BodyWidth = 0.197
BodyHeight = 0.157

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )
def inch2mils100( inch ):
	return int( inch * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "MOT1317" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
for pin in range (0,4):
    print '   Pad[',\
 	inch2mils100((pin-1.5) * PinSpacing), \
	inch2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	inch2mils100((pin-1.5) * PinSpacing), \
	inch2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
	inch2mils100(PinWidth), \
	inch2mils100(PinSpacing - PinWidth), \
  	inch2mils100(PinWidth)+600, \
	'"pin%i"' % (8 - pin), '"%i"' % (8 - pin), '0x0100]'

    print '   Pad[',\
 	inch2mils100((pin-1.5) * PinSpacing), \
	inch2mils100(RowSpacing/2 + PinWidth/2), \
 	inch2mils100((pin-1.5) * PinSpacing), \
	inch2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	inch2mils100(PinWidth), \
	inch2mils100(PinSpacing - PinWidth), \
  	inch2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '0x0100]'

#print '   ElementLine[',\
# 	inch2mils100(-BodyHeight/2), \
#	inch2mils100(-BodyWidth/2), \
#	inch2mils100(-BodyHeight/2), \
#	inch2mils100( BodyWidth/2), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	inch2mils100(-BodyHeight/2), \
#	inch2mils100( BodyWidth/2), \
#	inch2mils100( BodyHeight/2), \
#	inch2mils100( BodyWidth/2), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	inch2mils100( BodyHeight/2), \
#	inch2mils100( BodyWidth/2), \
#	inch2mils100( BodyHeight/2), \
#	inch2mils100(-BodyWidth/2), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	inch2mils100( BodyHeight/2), \
#	inch2mils100(-BodyWidth/2), \
#	inch2mils100(-BodyHeight/2), \
#	inch2mils100(-BodyWidth/2), \
#	'1000 ]'

print '   ElementArc[',\
        inch2mils100(-1.5 * PinSpacing), \
        inch2mils100(RowSpacing/3), \
	'500 500 0 360 1000 ]'

print ")"
