#!/usr/bin/python
# Copyright 2016 by Bdale Garbee <bdale@gag.com>.  GPLv3+
#
# Program to emit PCB footprint for Norcomp 181-YYY-213RYY1 connectors
# Female, right angle, 0.318 setback
#
# Needs pin count on command line, 15/26/44/62 are valid
#

# dimensions in mm from R181-YYY-213RYY1-1.pdf

PinDiam = 0.94
PinSpacing = 2.29
RowSpacing = 2.54
MntDiam = 3.05
BoxY = 16.24
FaceY = 8.89
ARing = 0.8
Clearance = 0.36

LineWidth = 1000

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

pins = int(sys.argv[1])
pinoffset = (pins - 1) / 6 * PinSpacing

if pins == 15:
	BoxX = 30.80
	MntX = 24.99
	pinoffset = pinoffset - (0.010 * 25.4)
elif pins == 26:
	BoxX = 39.19
	MntX = 33.32
	pinoffset = pinoffset - (0.020 * 25.4)
elif pins == 44:
	BoxX = 53.00
	MntX = 47.04
	pinoffset = pinoffset - (0.020 * 25.4)
elif pins == 62:
	BoxX = 69.30
	MntX = 63.50
	pinoffset = pinoffset - (0.023 * 25.4)
else:
	sys.stderr.write('Valid pin counts are 15|26|44|62\n')
	sys.exit(1)

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 3+'
print '# use-license: unlimited'

print 'Element[0x0 "DB%iFHD"' % pins,'"" "" 0 0 0 0 0 100 0x0]'
print "("
for col in range ((pins+1)/3):
	pinnum = col + 1
        if pinnum == 1:
	    Flags = '0x0101'
        else:
	    Flags = '0x0001'

        print '   Pin[', \
  	    mm2mils100((col)*PinSpacing-pinoffset), \
	    mm2mils100(RowSpacing), \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

	pinnum = col + 1 + (pins+1)/3
	Flags = '0x0001'
        print '   Pin[', \
  	    mm2mils100((col)*PinSpacing-pinoffset-PinSpacing/2), \
	    0, \
  	    mm2mils100(PinDiam+ARing), \
  	    mm2mils100(Clearance), \
  	    mm2mils100(PinDiam+ARing+Clearance), \
	    mm2mils100(PinDiam), \
	    '"pin%i"' % pinnum, '"%i"' % pinnum, Flags, ']'

	pinnum = col + 1 + 2*(pins+1)/3
	Flags = '0x0001'
	if pinnum <= pins:
          print '   Pin[', \
  	    mm2mils100((col)*PinSpacing-pinoffset), \
	    mm2mils100(-RowSpacing), \
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
	mm2mils100(-FaceY-RowSpacing), \
	mm2mils100(BoxX/2), \
	mm2mils100(-FaceY-RowSpacing), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(-BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing), \
	mm2mils100(BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(BoxX/2), \
	mm2mils100(-FaceY-RowSpacing), \
	mm2mils100(BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing), \
	LineWidth, ']'

print '   ElementLine[', \
  	mm2mils100(-BoxX/2), \
	mm2mils100(-FaceY-RowSpacing), \
	mm2mils100(-BoxX/2), \
	mm2mils100(BoxY-FaceY-RowSpacing), \
	LineWidth, ']'

print ")"
