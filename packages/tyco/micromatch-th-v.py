#!/usr/bin/python
# Copyright 2009 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Tyco/AMP Micro-MaTch vertical through-hole female connectors
#
# Needs pin count on command line, in range of 4..20 even numbers only
#

# dimensions in mm from C_215079_v.pdf datasheet
PinDiam = 0.8
PinSpacing = 1.27
RowSpacing = 2.54

MntX = 1.4
MntY = 1.8
MntDiam = 1.5

BoxY = 5.1
BoxXbase = 4.79

LineWidth = 600

# freedfm.com round-off error bites us if we make this 700...
MinAnnular = 725
MinClearance = 600
MaskDelta = 300

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = int(sys.argv[1])

if pins < 4:
	sys.stderr.write('Must be at least 4 pins\n')
	sys.exit(1)
if pins == 22:
	sys.stderr.write('There is no 22 pin version!\n')
	sys.exit(1)
if pins > 24:
	sys.stderr.write('Must be no more than 24 pins\n')
	sys.exit(1)

if len(sys.argv) > 2:
    if sys.argv[2] == "latch":
	BoxXbase = 5.89
	if pins == 24:
		sys.stderr.write('There is no 24 pin latching version!\n')
		sys.exit(1)

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "MicroMatch%i"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for col in range ((pins+1)/2):
    for row in range (2):
	if row == 1:
	    spacing=0
	else:
	    spacing=RowSpacing
        pinnum = (col * 2) + row + 1
        if pinnum == 1:
	    Flags = '0x0101'
        else:
	    Flags = '0x0001'
        print '   Pin[', \
  	    mm2mils100((pinnum-1)*PinSpacing), \
	    mm2mils100(spacing), \
  	    mm2mils100(PinDiam)+(MinAnnular*2), \
	    (MinClearance*2), \
  	    mm2mils100(PinDiam)+(MinAnnular*2)+(MaskDelta*2), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

# add a hole for the index pin.  plated to save non-plated-hole extra fab cost.
print '   Pin[', \
    mm2mils100(-MntX), \
    mm2mils100(RowSpacing-MntY), \
    mm2mils100(MntDiam)+(MinAnnular*2), \
    (MinClearance*2), \
    mm2mils100(MntDiam)+(MinAnnular*2)+(MaskDelta*2), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0001', ']'

BoxX = (pins - 1) * PinSpacing + BoxXbase
BoxX1 = -(BoxXbase/2)
BoxX2 = BoxX1 + BoxX
BoxY1 = -(BoxY - RowSpacing)/2
BoxY2 = BoxY1 + BoxY

print '   ElementLine[', \
  	mm2mils100(BoxX1), \
	mm2mils100(BoxY1), \
	mm2mils100(BoxX1), \
	mm2mils100(BoxY2), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(BoxX1), \
	mm2mils100(BoxY2), \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY2), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY2), \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY1), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxX2), \
	mm2mils100(BoxY1), \
	mm2mils100(BoxX1), \
	mm2mils100(BoxY1), \
	LineWidth, ']'
  
print ")"
