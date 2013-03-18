#!/usr/bin/python
# Copyright 2008 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Molex 1.25mm PicoBlade, vertical through-hole header 53047-XX10, 2-15 pins 
#
# Needs pin count on command line, in range of 2..15
#

# dimensions in mm from 530470410_sd.pdf datasheet
PinDiam = 0.52
PinSpacing = 1.25
BoxOffset = 1.15
BoxHeight = 3.2
BoxEnd = 1.5
LineWidth = 600

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

print 'Element[0x0 "PicoBlade%i"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for pin in range (1,pins+1):
    pinnum = pins + 1 - pin
    if pinnum == 1:
	Flags = '0x0101'
    else:
	Flags = '0x0001'
    print '   Pin[', \
  	mm2mils100((pins-1)*PinSpacing - (pin-1)*PinSpacing), \
	0, \
  	3500, \
	1200, \
	4100, \
	mm2mils100(PinDiam), \
	'"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

BoxWidth = (BoxEnd * 2) + ((pins - 1) * PinSpacing);

print '   ElementLine[', \
  	mm2mils100(-BoxEnd), \
	mm2mils100(-BoxOffset), \
	mm2mils100(-BoxEnd), \
	mm2mils100(BoxHeight-BoxOffset), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(-BoxEnd), \
	mm2mils100(BoxHeight-BoxOffset), \
	mm2mils100(BoxWidth-BoxEnd), \
	mm2mils100(BoxHeight-BoxOffset), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxWidth-BoxEnd), \
	mm2mils100(BoxHeight-BoxOffset), \
	mm2mils100(BoxWidth-BoxEnd), \
	mm2mils100(-BoxOffset), \
	LineWidth, ']'

print '   ElementLine[', \
	mm2mils100(BoxWidth-BoxEnd), \
	mm2mils100(-BoxOffset), \
	mm2mils100(-BoxEnd), \
	mm2mils100(-BoxOffset), \
	LineWidth, ']'
  
print ")"
