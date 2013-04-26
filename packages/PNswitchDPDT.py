#!/usr/bin/python
# Copyright 2010 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for C&K PN22SJNA03QE DPDT switch
#

# dimensions in mm from footprint drawing at DigiKey
BodyWidth = 12			# body outline
BodyHeight = 6.8
PinSpace = 2.49
PinDiam = 0.89
MntWidth = 11.40
MntHeight = 4.19
MntDiam = 1.50

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "PN22SJNA03QE" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pin[',\
 	mm2mils100(-PinSpace), \
	mm2mils100(-PinSpace/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(PinDiam), \
	'"pin1" "1" 0x0101]'

print '   Pin[',\
 	mm2mils100(0), \
 	mm2mils100(-PinSpace/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(PinDiam), \
	'"pin2" "2" 0x0001]'

print '   Pin[',\
 	mm2mils100(PinSpace), \
	mm2mils100(-PinSpace/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(PinDiam), \
	'"pin3" "3" 0x0001]'

print '   Pin[',\
 	mm2mils100(PinSpace), \
	mm2mils100(PinSpace/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(PinDiam), \
	'"pin6" "6" 0x0001]'

print '   Pin[',\
 	mm2mils100(0), \
	mm2mils100(PinSpace/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(PinDiam), \
	'"pin5" "5" 0x0001]'

print '   Pin[',\
 	mm2mils100(-PinSpace), \
	mm2mils100(PinSpace/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(PinDiam), \
	'"pin4" "4" 0x0001]'

print '   Pin[',\
 	mm2mils100(-MntWidth/2), \
	mm2mils100(MntHeight/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(MntDiam), \
	'"pin7" "G" 0x0001]'

print '   Pin[',\
 	mm2mils100(MntWidth/2), \
	mm2mils100(-MntHeight/2), \
 	mm2mils100(2), \
	mm2mils100(1), \
	mm2mils100(2.2), \
	mm2mils100(MntDiam), \
	'"pin8" "G" 0x0001]'

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

print ")"
