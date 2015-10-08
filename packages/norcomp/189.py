#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Norcomp 182-YYY-213RYY1 connectors
# dual (stacked) female, right angle, 0.318 setback
#
# Needs pin count on command line, 9/15/25/37 are valid
#

# dimensions in mm from 189-YYY-513R571.pdf

PinDiam = 1.20
PinSpacing = 2.77
RowSpacing = 2.84
DualSpacing = 6.58
MntDiam = 3.05
BoxY = 19.304
FaceY = 8.08
ARing = 0.8
Clearance = 0.36

LineWidth = 1000

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = int(sys.argv[1])

if pins == 9:
	BoxX = 30.58
	MntX = 24.99
elif pins == 15:
	BoxX = 38.99
	MntX = 33.32
elif pins == 25:
	BoxX = 52.78
	MntX = 46.99
elif pins == 37:
	BoxX = 69.19
	MntX = 63.50
else:
	sys.stderr.write('Valid pin counts are 9|15|25|37\n')
	sys.exit(1)

pinoffset = (pins - 1) / 4 * PinSpacing
if pins == 15:
	pinoffset += PinSpacing/2

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "DB%iF"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for col in range ((pins+1)/2):
	pinnum = col + 1
        if pinnum == 1:
	    Flags = '0x0101'
        else:
	    Flags = '0x0001'

        print '   Pin[', \
  	    mm2mils100((pinnum-1)*PinSpacing-pinoffset), \
	    mm2mils100(RowSpacing/2), \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

	pinnum2 = pinnum + pins
        print '   Pin[', \
  	    mm2mils100((pinnum-1)*PinSpacing-pinoffset), \
	    mm2mils100(RowSpacing/2+DualSpacing), \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum2, '"%i"' % pinnum2, Flags, ']'

	pinnum = col + 1 + (pins+1)/2
	Flags = '0x0001'
	if pinnum <= pins:
          print '   Pin[', \
  	    mm2mils100((col)*PinSpacing-pinoffset+PinSpacing/2), \
	    mm2mils100(-RowSpacing/2), \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

	  pinnum2 = pinnum + pins
          print '   Pin[', \
  	    mm2mils100((col)*PinSpacing-pinoffset+PinSpacing/2), \
	    mm2mils100(-RowSpacing/2+DualSpacing), \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum2, '"%i"' % pinnum2, Flags, ']'

print '   Pin[', \
    mm2mils100(MntX/2), \
    mm2mils100(-RowSpacing/2), \
    mm2mils100(MntDiam+ARing), \
    mm2mils100(Clearance), \
    mm2mils100(MntDiam+ARing+Clearance), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0001', ']'

print '   Pin[', \
    mm2mils100(-MntX/2), \
    mm2mils100(-RowSpacing/2), \
    mm2mils100(MntDiam+ARing), \
    mm2mils100(Clearance), \
    mm2mils100(MntDiam+ARing+Clearance), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0001', ']'

print '   Pin[', \
    mm2mils100(MntX/2), \
    mm2mils100(DualSpacing), \
    mm2mils100(MntDiam+ARing), \
    mm2mils100(Clearance), \
    mm2mils100(MntDiam+ARing+Clearance), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0001', ']'

print '   Pin[', \
    mm2mils100(-MntX/2), \
    mm2mils100(DualSpacing), \
    mm2mils100(MntDiam+ARing), \
    mm2mils100(Clearance), \
    mm2mils100(MntDiam+ARing+Clearance), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0001', ']'

print '   ElementLine[', \
  	mm2mils100(-BoxX/2), \
	mm2mils100(-FaceY-RowSpacing/2), \
	mm2mils100(BoxX/2), \
	mm2mils100(-FaceY-RowSpacing/2), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(-BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing/2), \
	mm2mils100(BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing/2), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(BoxX/2), \
	mm2mils100(-FaceY-RowSpacing/2), \
	mm2mils100(BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing/2), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(-BoxX/2), \
	mm2mils100(-FaceY-RowSpacing/2), \
	mm2mils100(-BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing/2), \
	LineWidth, ']'

print ")"
