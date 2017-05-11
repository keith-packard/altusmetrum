#!/usr/bin/python
# Copyright 2017 by Bdale Garbee <bdale@gag.com>.  GPLv2+
#
# Program to emit PCB footprint for
#   TE Connectivity (AMP) through-hole BNC connectors 5227673 & 5227677
#
#   This footprint is meant to allow the right-angle connector to be installed
#   on the "top" surface of the board, and the straight connector to be 
#   installed on the top or bottom of the board.
#
# dimensions in mm from ENG_CD_5227673_A.pdf & ENG_CD_5227677_A1.pdf

PinDiam = 0.89
PinSpacing = 2.54

MntDiam = 2.01
MntSpacing = 10.16
Mnt2Edge = 7.75

SilkBox = 14.76

LineWidth = 600
ThicknessDelta = 1.0
Clearance = .32
MaskDelta = 0.32

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2+'
print '# use-license: unlimited'

print 'Element[0x0 "AMP BNC" "" "" 0 0 0 0 0 100 0x0]'
print "("

print '   Pin[', \
        0, \
        0, \
        mm2mils100(PinDiam+ThicknessDelta), \
        mm2mils100(Clearance), \
        mm2mils100(PinDiam+ThicknessDelta+MaskDelta), \
        mm2mils100(PinDiam), \
	'"1"', \
	'"1"', \
	"0x0001", ']'

print '   Pin[', \
        0, \
        mm2mils100(-PinSpacing), \
        mm2mils100(PinDiam+ThicknessDelta), \
        mm2mils100(Clearance), \
        mm2mils100(PinDiam+ThicknessDelta+MaskDelta), \
        mm2mils100(PinDiam), \
	'"GND"', \
	'"2"', \
	"0x0001", ']'

print '   Pin[', \
        mm2mils100(MntSpacing/2), \
        mm2mils100(MntSpacing/2), \
        mm2mils100(MntDiam+ThicknessDelta), \
        mm2mils100(Clearance), \
        mm2mils100(MntDiam+ThicknessDelta+MaskDelta), \
        mm2mils100(MntDiam), \
	'"GND"', \
	'"2"', \
	"0x0001", ']'

print '   Pin[', \
        mm2mils100(-MntSpacing/2), \
        mm2mils100(MntSpacing/2), \
        mm2mils100(MntDiam+ThicknessDelta), \
        mm2mils100(Clearance), \
        mm2mils100(MntDiam+ThicknessDelta+MaskDelta), \
        mm2mils100(MntDiam), \
	'"GND"', \
	'"2"', \
	"0x0001", ']'

print '   Pin[', \
        mm2mils100(MntSpacing/2), \
        mm2mils100(-MntSpacing/2), \
        mm2mils100(MntDiam+ThicknessDelta), \
        mm2mils100(Clearance), \
        mm2mils100(MntDiam+ThicknessDelta+MaskDelta), \
        mm2mils100(MntDiam), \
	'"GND"', \
	'"2"', \
	"0x0001", ']'

print '   Pin[', \
        mm2mils100(-MntSpacing/2), \
        mm2mils100(-MntSpacing/2), \
        mm2mils100(MntDiam+ThicknessDelta), \
        mm2mils100(Clearance), \
        mm2mils100(MntDiam+ThicknessDelta+MaskDelta), \
        mm2mils100(MntDiam), \
	'"GND"', \
	'"2"', \
	"0x0001", ']'


print '   ElementLine[', \
        mm2mils100(MntSpacing/2+Mnt2Edge-SilkBox), \
        mm2mils100(SilkBox/2), \
        mm2mils100(MntSpacing/2+Mnt2Edge), \
        mm2mils100(SilkBox/2), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(MntSpacing/2+Mnt2Edge-SilkBox), \
        mm2mils100(-SilkBox/2), \
        mm2mils100(MntSpacing/2+Mnt2Edge), \
        mm2mils100(-SilkBox/2), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(MntSpacing/2+Mnt2Edge-SilkBox), \
        mm2mils100(SilkBox/2), \
        mm2mils100(MntSpacing/2+Mnt2Edge-SilkBox), \
        mm2mils100(-SilkBox/2), \
        LineWidth, ']'

print '   ElementLine[', \
        mm2mils100(MntSpacing/2+Mnt2Edge), \
        mm2mils100(SilkBox/2), \
        mm2mils100(MntSpacing/2+Mnt2Edge), \
        mm2mils100(-SilkBox/2), \
        LineWidth, ']'

print ")"
