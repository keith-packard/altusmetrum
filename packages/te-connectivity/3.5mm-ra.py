#!/usr/bin/python
# Copyright 2014 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Tyco Electronics 3.5mm pitch right-angle terminal blocks ala 284512-4
#
# Needs pin count on command line, in range of 2..25
#

# dimensions in mm from ENG_CD_284512_E3.pdf
PinDiam = 1.2
PinSpacing = 3.5
RowOffset = 8.0
BoxHeight = 9.2
BoxEnd = 2.75
LineWidth = 600
Thickness = 2.0
Clearance = .32
Mask = Thickness + 0.32

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = int(sys.argv[1])
if pins < 2:
	sys.stderr.write('Must be at least 2 pins\n')
	sys.exit(1)
if pins > 25:
	sys.stderr.write('Must be no more than 25 pins\n')
	sys.exit(1)

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "284512-%i"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for pin in range (1,pins+1):
    pinnum = pins + 1 - pin
    if pinnum == 1:
	Flags = '0x0101'
    else:
	Flags = '0x0001'
    print '   Pin[', \
        mm2mils100(BoxEnd + (pin-1)*PinSpacing), \
        mm2mils100(RowOffset), \
        mm2mils100(Thickness), \
        mm2mils100(Clearance), \
        mm2mils100(Mask), \
        mm2mils100(PinDiam), \
        '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

BoxWidth = (BoxEnd * 2) + ((pins - 1) * PinSpacing);

print '   ElementLine[', \
        mm2mils100(0), \
        mm2mils100(0), \
        mm2mils100(0), \
        mm2mils100(BoxHeight), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(0), \
        mm2mils100(BoxHeight), \
        mm2mils100(BoxWidth), \
        mm2mils100(BoxHeight), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(BoxWidth), \
        mm2mils100(BoxHeight), \
        mm2mils100(BoxWidth), \
        mm2mils100(0), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(BoxWidth), \
        mm2mils100(0), \
        mm2mils100(0), \
        mm2mils100(0), \
        LineWidth, ']'

print ")"
