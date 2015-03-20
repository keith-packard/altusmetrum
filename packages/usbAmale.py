#!/usr/bin/python
# Copyright 2014 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for Keystone model 931 USB A male connector,
# should also work fine for 4ucon 10017 / 10019, and Acon C-UAR70-00-00
#

# dimensions in mm homogenized from Keystone, 4ucon, and Acon  datasheets

				# note that in practice we may not want
				# holes for the tabs in a USB key form factor,
				# in which case just delete the features in
				# the PCB layout and make board width right
TabDiam = 2.50
TabMinor = 1.00
TabSpacing = 11.70

PinDiam = 1.10
PinSpacing = 4.50		# keystone wants 4.6 here .. really?

PadHeight = 2.0			# keystone says 1.99 but is 0.1 closer
PadWidth = 1.20			# keystone says 1.1 but wider will work
Pad14 = 7.0
Pad23 = 2.0
PadRowOffset = 2.60
EdgeOffset = 2.70		# keystone says 2.9, but shorter should be ok

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "usbAmale" "" "" 0 0 0 0 0 100 0x0]'
print "("
print '   Pad[',\
 	mm2mils100(Pad14/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(Pad14/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin4" "4" 0x0100]'

print '   Pad[',\
 	mm2mils100(-Pad14/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(-Pad14/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin1" "1" 0x0100]'

print '   Pad[',\
 	mm2mils100(Pad23/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(Pad23/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin3" "3" 0x0100]'

print '   Pad[',\
 	mm2mils100(-Pad23/2), \
	mm2mils100(PadRowOffset - PadHeight / 2 + PadWidth/2), \
 	mm2mils100(-Pad23/2), \
	mm2mils100(PadRowOffset + PadHeight / 2 - PadWidth/2), \
	mm2mils100(PadWidth), \
	mm2mils100(0), \
  	mm2mils100(PadWidth)+600, \
	'"pin2" "2" 0x0100]'

print '   Pin[',\
        mm2mils100(-PinSpacing/2), \
        mm2mils100(0), \
        mm2mils100(PinDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(PinDiam+0.66), \
        mm2mils100(PinDiam), \
        '"mnt" "G" 0x0000]'

print '   Pin[',\
        mm2mils100(PinSpacing/2), \
        mm2mils100(0), \
        mm2mils100(PinDiam+0.3556), \
        mm2mils100(0.31), \
        mm2mils100(PinDiam+0.66), \
        mm2mils100(PinDiam), \
        '"mnt" "G" 0x0000]'

print '   Pad[',\
        mm2mils100(-TabSpacing/2 + PadWidth/2 + TabMinor/2), \
        mm2mils100(-TabDiam/2), \
        mm2mils100(-TabSpacing/2 + PadWidth/2 + TabMinor/2), \
        mm2mils100(TabDiam/2), \
        mm2mils100(PadWidth), \
        mm2mils100(0.31), \
        mm2mils100(PadWidth + 0.15), \
        '"mnt" "G" "onsolder,nopaste"]'

print '   Pad[',\
        mm2mils100(TabSpacing/2 - PadWidth/2 - TabMinor/2), \
        mm2mils100(-TabDiam/2), \
        mm2mils100(TabSpacing/2 - PadWidth/2 - TabMinor/2), \
        mm2mils100(TabDiam/2), \
        mm2mils100(PadWidth), \
        mm2mils100(0.31), \
        mm2mils100(PadWidth + 0.15), \
        '"mnt" "G" "onsolder,nopaste"]'

print '   ElementLine[',\
       mm2mils100(-TabSpacing/2), \
       mm2mils100(-EdgeOffset)+500, \
       mm2mils100(TabSpacing/2), \
       mm2mils100(-EdgeOffset)+500, \
       '1000 ]'

print '   ElementLine[',\
       mm2mils100(-TabSpacing/2 + TabMinor/2), \
       mm2mils100(-TabDiam/2), \
       mm2mils100(-TabSpacing/2 + TabMinor/2), \
       mm2mils100(TabDiam/2), \
       '1000 ]'

print '   ElementLine[',\
       mm2mils100(TabSpacing/2 - TabMinor/2), \
       mm2mils100(-TabDiam/2), \
       mm2mils100(TabSpacing/2 - TabMinor/2), \
       mm2mils100(TabDiam/2), \
       '1000 ]'

print ")"
