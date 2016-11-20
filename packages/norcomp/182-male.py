#!/usr/bin/python
# Copyright 2016 by Bdale Garbee <bdale@gag.com>.  GPLv3+
#
# Program to emit PCB footprint for Norcomp 182-YYY-113RYY1 connectors
# Male, right angle, 0.318 setback
#
# Needs pin count on command line, 9/15/25/37 are valid
#

# dimensions in mm from R182-YYY-213RYY1-1.pdf

PinDiam = 1.09
PinSpacing = 2.77
RowSpacing = 2.84
MntDiam = 3.05
BoxY = 12.42
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
	BoxX = 30.80
	MntX = 24.99
elif pins == 15:
	BoxX = 39.14
	MntX = 33.32
elif pins == 25:
	BoxX = 53.04
	MntX = 47.04
elif pins == 37:
	BoxX = 69.32
	MntX = 63.50
else:
	sys.stderr.write('Valid pin counts are 9|15|25|37\n')
	sys.exit(1)

pinoffset = -(pins - 1) / 4 * PinSpacing
if pins == 15:
	pinoffset += PinSpacing/2

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3+'
print '# use-license: unlimited'

print 'Element[0x0 "DB%iM"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for col in range ((pins+1)/2):
	pinnum = col + 1
        if pinnum == 1:
	    Flags = '0x0101'
        else:
	    Flags = '0x0001'

        print '   Pin[', \
  	    mm2mils100(-(pinnum-1)*PinSpacing-pinoffset), \
	    mm2mils100(RowSpacing/2), \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

	pinnum = col + 1 + (pins+1)/2
	Flags = '0x0001'
	if pinnum <= pins:
          print '   Pin[', \
  	    mm2mils100(-(col)*PinSpacing-pinoffset-PinSpacing/2), \
	    mm2mils100(-RowSpacing/2), \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'



print '   Pin[', \
    mm2mils100(MntX/2), \
    mm2mils100(0), \
    mm2mils100(MntDiam+ARing), \
    mm2mils100(Clearance), \
    mm2mils100(MntDiam+ARing+Clearance), \
    mm2mils100(MntDiam), \
    '"mnt" "0"', '0x0001', ']'

print '   Pin[', \
    mm2mils100(-MntX/2), \
    mm2mils100(0), \
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
