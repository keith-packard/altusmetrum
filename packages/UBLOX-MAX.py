#!/usr/bin/python
# Copyright 2013 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for U-Blox MAX-6 GPS receiver
#

# dimensions in mm fromL
#	LEA-6_NEO-6_MAX-6_HardwareIntegrationManual_(GPS.G6-HW-09007).pdf

BodyHeight = 10.1
BodyWidth = 12.5			# physical is 9.7, 12.5 includes paste

CornerPinWidth = 0.7
MainPinWidth = 0.8
PinHeight = 1.8
PinSpacing = 1.1
RowCenters = 9.7 - (1.0 - 0.8)
RowSpacing = RowCenters - PinHeight

PasteTongueWidthDelta = 0.2
PasteRowSpacing = 9.7
PasteHeight = (12.5 - 9.7) / 2
#PasteHeight = 0.8			# not quite what the manual says

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "UBLOX-MAX" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
# first, lay down the copper but with no paste mask defined
for pin in range (0,9):
    if (pin == 0) or (pin == 8):
	PinWidth = CornerPinWidth
    else:
	PinWidth = MainPinWidth
    print '   Pad[',\
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (18 - pin), '"%i"' % (18 - pin), '"square,nopaste"]'

    print '   Pad[',\
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '"square,nopaste"]'

# now define the paste mask, which needs two rectangles per pad in T-shape
# the first rectangle is full pin height but narrower
for pin in range (0,9):
    if (pin == 0) or (pin == 8):
	PinWidth = CornerPinWidth - PasteTongueWidthDelta
    else:
	PinWidth = MainPinWidth - PasteTongueWidthDelta
    print '   Pad[',\
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(-(RowSpacing/2 + PinHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (18 - pin), '"%i"' % (18 - pin), '"square"]'

    print '   Pad[',\
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(RowSpacing/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '"square"]'

# the second rectangle is partial height but full width
for pin in range (0,9):
    if (pin == 0) or (pin == 8):
	PinWidth = CornerPinWidth
    else:
	PinWidth = MainPinWidth
    print '   Pad[',\
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(-(PasteRowSpacing/2 + PinWidth/2)), \
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(-(PasteRowSpacing/2 + PasteHeight - PinWidth/2)), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (18 - pin), '"%i"' % (18 - pin), '"square"]'

    print '   Pad[',\
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(PasteRowSpacing/2 + PinWidth/2), \
 	mm2mils100((pin-4) * PinSpacing), \
	mm2mils100(PasteRowSpacing/2 + PasteHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth)+600, \
	'"pin%i"' % (1 + pin), '"%i"' % (1 + pin), '"square"]'


print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	mm2mils100(-BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100(-BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	mm2mils100( BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodyHeight/2), \
	mm2mils100( BodyWidth/2), \
	mm2mils100( BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	'1000 ]'

print '   ElementLine[',\
 	mm2mils100( BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	mm2mils100(-BodyHeight/2), \
	mm2mils100(-BodyWidth/2), \
	'1000 ]'

print '   ElementArc[',\
	mm2mils100(-4 * PinSpacing), \
	mm2mils100(RowSpacing/2-PinHeight/2), \
	'500 500 0 360 1000 ]'

print ")"
