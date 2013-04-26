#!/usr/bin/python
# Copyright 2010 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for NHD-C0216CU-FN-GBW-3V 2x16 text LCD
#

# dimensions in mm from Newhaven Display International datasheet
BodyWidth = 49.7
BodyHeight = 25.3
PinDiam = 0.72			# 0.50 +- 0.5 x 0.30 +- 0.05 rectangular pins
				# worst case 0.66mm diagonal, plus some slack
PinSpacing = 1.50
Pins = 17
ViewWidth = 45.70
ViewHeight = 14.30
ViewHCtr = (BodyHeight/2) - (18.30 / 2)

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "NHD-C0216" "" "" 0 0 0 0 0 100 0x0]'
print "("

# pins
	# pin( x y thickness clearance mask drillhole name number flags)
for pin in range (1,Pins+1):
    if pin == 1:
        Flags = '0x0101'
    else:
        Flags = '0x0001'

    print '   Pin[',\
	mm2mils100((pin - 9)*PinSpacing), \
 	mm2mils100(-BodyHeight/2), \
 	mm2mils100(PinDiam * 1.75), \
	1200, \
 	mm2mils100(PinDiam * 1.75) + 600, \
	mm2mils100(PinDiam), \
	'"pin%i"' % (pin), '"%i"' % (pin), Flags, ']'

print '   ElementLine[',\
 	-mm2mils100(BodyWidth/2), \
 	-mm2mils100(BodyHeight/2), \
 	mm2mils100(BodyWidth/2), \
 	-mm2mils100(BodyHeight/2), \
	500, \
	']'
print '   ElementLine[',\
 	-mm2mils100(BodyWidth/2), \
	-mm2mils100(BodyHeight/2), \
 	-mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight/2), \
	500, \
	']'
print '   ElementLine[',\
 	-mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight/2), \
 	mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight/2), \
	500, \
	']'
print '   ElementLine[',\
 	mm2mils100(BodyWidth/2), \
	mm2mils100(BodyHeight/2), \
 	mm2mils100(BodyWidth/2), \
	-mm2mils100(BodyHeight/2), \
	500, \
	']'

# mark viewable area
#	ViewWidth = 45.70
#	ViewHeight = 14.30
#	ViewHCtr = BodyHeight - (18.30 / 2)

print '   ElementLine[',\
 	mm2mils100(-ViewWidth/2), \
	mm2mils100(ViewHCtr + ViewHeight/2), \
 	mm2mils100(ViewWidth/2), \
	mm2mils100(ViewHCtr + ViewHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	mm2mils100(-ViewWidth/2), \
	mm2mils100(ViewHCtr - ViewHeight/2), \
 	mm2mils100(ViewWidth/2), \
	mm2mils100(ViewHCtr - ViewHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	mm2mils100(-ViewWidth/2), \
	mm2mils100(ViewHCtr - ViewHeight/2), \
 	mm2mils100(-ViewWidth/2), \
	mm2mils100(ViewHCtr + ViewHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	mm2mils100(ViewWidth/2), \
	mm2mils100(ViewHCtr - ViewHeight/2), \
 	mm2mils100(ViewWidth/2), \
	mm2mils100(ViewHCtr + ViewHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	mm2mils100(ViewWidth/2), \
	mm2mils100(ViewHCtr - ViewHeight/2), \
 	mm2mils100(-ViewWidth/2), \
	mm2mils100(ViewHCtr + ViewHeight/2), \
	500, \
	']'

print '   ElementLine[',\
 	mm2mils100(-ViewWidth/2), \
	mm2mils100(ViewHCtr - ViewHeight/2), \
 	mm2mils100(ViewWidth/2), \
	mm2mils100(ViewHCtr + ViewHeight/2), \
	500, \
	']'

print ")"
