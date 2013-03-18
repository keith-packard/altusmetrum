#!/usr/bin/python
# Copyright 2008 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Molex 1.25mm PicoBlade, vertical through-hole header 53047-XX10, 2-15 pins 
#
# Needs pin count on command line, in range of 2..15
#

# dimensions in mm from 903257004_sd.pdf datasheet
PinDiam = 0.8
PinSpacing = 2.54
RowSpacing = 2.54
RowOffset = 1.27
BoxHeight = 5.98
BoxEnd = 2.755
MntX = 1.8
MntY = 1.48
MntDiam = 1.5
LineWidth = 600

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = int(sys.argv[1])
if pins < 4:
	sys.stderr.write('Must be at least 4 pins\n')
	sys.exit(1)
if pins > 26:
	sys.stderr.write('Must be no more than 26 pins\n')
	sys.exit(1)

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "PicoFlex%i"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for col in range ((pins+1)/2):
    for row in range (2):
	if row == 1:
	    offset=RowOffset
	    spacing=RowSpacing
	else:
	    offset=0
	    spacing=0
        pinnum = (col * 2) + row + 1
        if pinnum == 1:
	    Flags = '0x0101'
        else:
	    Flags = '0x0001'
        print '   Pin[', \
  	    mm2mils100(col*PinSpacing + offset), \
	    mm2mils100(spacing), \
  	    mm2mils100(PinDiam*2), \
	    600, \
  	    mm2mils100(PinDiam*2)+1000, \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

print '   Pin[', \
    mm2mils100(-MntX), \
    mm2mils100(-MntY), \
    mm2mils100(MntDiam), \
    0, \
    mm2mils100(MntDiam), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0008', ']'

print '   Pin[', \
    mm2mils100(((pins+1)/2-1)*PinSpacing+RowOffset+MntX), \
    mm2mils100(-MntY), \
    mm2mils100(MntDiam), \
    0, \
    mm2mils100(MntDiam), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0008', ']'

BoxWidth = BoxEnd + ((pins/2-1) * PinSpacing + RowOffset);
BoxYOff = MntY + MntDiam/2 + .1524

print '   ElementLine[', \
  	mm2mils100(-BoxEnd), \
	mm2mils100(-BoxYOff), \
	mm2mils100(-BoxEnd), \
	mm2mils100(BoxHeight-BoxYOff), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(-BoxEnd), \
	mm2mils100(BoxHeight-BoxYOff), \
	mm2mils100(BoxWidth), \
	mm2mils100(BoxHeight-BoxYOff), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxWidth), \
	mm2mils100(BoxHeight-BoxYOff), \
	mm2mils100(BoxWidth), \
	mm2mils100(-BoxYOff), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxWidth), \
	mm2mils100(-BoxYOff), \
	mm2mils100(-BoxEnd), \
	mm2mils100(-BoxYOff), \
	LineWidth, ']'
  
print ")"
