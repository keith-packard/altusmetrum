#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   JST PH Series 2mm Side Entry SMT (Shrouded) connectors
#
# Needs pin count on command line, in range of 2..15
#

# dimensions in mm from PH Series.pdf datasheet
TabWidth = 1.5
TabHeight = 3.4
TabPinSpacing = 2.1
PinWidth = 1.0
PinHeight = 3.5
PinSpacing = 2.0
FirstPin = 3.1

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

print 'Element[0x0 "S%iB-PH"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for pin in range (1,pins+1):
    pinnum = pins + 1 - pin
    print '   Pad[', \
  	mm2mils100(FirstPin + (pin-1)*PinSpacing), \
	mm2mils100(TabHeight+TabPinSpacing+PinWidth/2), \
  	mm2mils100(FirstPin + (pin-1)*PinSpacing), \
	mm2mils100(TabHeight+TabPinSpacing+PinHeight-PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.2), \
	'"pin%i"' % pinnum, '"%i"' % pinnum, '0x0100]'


print '   Pad[', \
  	mm2mils100(TabWidth/2), \
	mm2mils100(TabWidth/2), \
	mm2mils100(TabWidth/2), \
	mm2mils100(TabHeight - TabWidth/2), \
	mm2mils100(TabWidth), \
	0, \
  	mm2mils100(TabWidth + 0.2), \
	'"tab1" "G" 0x0100]'

print '   Pad[', \
  	mm2mils100(FirstPin*2 + (pins-1)*PinSpacing - TabWidth/2), \
	mm2mils100(TabWidth/2), \
  	mm2mils100(FirstPin*2 + (pins-1)*PinSpacing - TabWidth/2), \
	mm2mils100(TabHeight - TabWidth/2), \
	mm2mils100(TabWidth), \
	0, \
  	mm2mils100(TabWidth + 0.2), \
	'"tab2" "G" 0x0100]'

print ")"
