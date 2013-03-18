#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   JST PH series 2mm vertical entry through-hole (shrouded) connectors
#
# Needs pin count on command line, in range of 2..15
#

# dimensions in mm from ePH.pdf datasheet
PinDiam = 0.75
PinSpacing = 2.0
RowOffset = (4.5 - 1.7)
BoxHeight = 4.5
BoxEnd = 1.95
LineWidth = 600
Thickness = 1.3
Clearance = .305
Mask = 1.46

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = int(sys.argv[1])
if pins < 2:
	sys.stderr.write('Must be at least 2 pins\n')
	sys.exit(1)
if pins > 15:
	sys.stderr.write('Must be no more than 15 pins\n')
	sys.exit(1)

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "B%iB-PH"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
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
