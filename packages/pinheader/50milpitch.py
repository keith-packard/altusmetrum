#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Sullins Connector Solutions single row 0.050" header pins
#
# Needs pin count on command line, in range of 2..50
#

# dimensions in mm
PinSpacing = 1.27

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

print 'Element[0x0 "50mil%ipin"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
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
  	4200, \
	1200, \
	4800, \
	2800, \
	'"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

print ")"