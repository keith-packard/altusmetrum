#!/usr/bin/python
# Copyright 2014 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for PowerPAD 32-pin package used by TPA3118
#

# dimensions in mm from the TI tpa3116d2.pdf datasheet
PinWidth = 0.3
PinResist = 0.44 		# width of gap in solder resist over pad
PinHeight = 1.80
PinSpacing = 0.65
PinRow = 7.4			# center to center of pin rows

PadWidth = 11.0			# ground pad under part
PadHeight = 5.2

MaskWidth = 4.36		# opening in solder mask for ground pad
MaskHeight = 4.11		

ViaGrid = 1.3			# spacing between vias in ground pad

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "PowerPAD32" "" "" 0 0 0 0 0 100 0x0]'
print "("

# vias in the ground pad under the chip
for viarow in range (-2,2):
  for viacol in range (-4,4):
    print '   Pin[',\
	mm2mils100(viacol * ViaGrid + ViaGrid/2), \
 	mm2mils100(viarow * ViaGrid + ViaGrid/2), \
	2700, \
	2500, \
  	0, \
  	1300, \
	'"pin33" "33" 0x0002]'

# break pad under chip into a grid to control the resist and paste masks
for viarow in range (-3, 4):
  for viacol in range (-8, 9):
    if (viacol in (-3, -2, -1, 0, 1, 2, 3)):
      # copper sub-square without resist, with paste
      print '   Pad[',\
	mm2mils100(viacol * ViaGrid/2), \
	mm2mils100(viarow * ViaGrid/2), \
	mm2mils100(viacol * ViaGrid/2), \
	mm2mils100(viarow * ViaGrid/2), \
	mm2mils100(ViaGrid/2), \
	0, \
	mm2mils100(ViaGrid/2), \
	'"pin33" "33" "square"]'
    else:
      # copper sub-square with resist over vias
      print '   Pad[',\
	mm2mils100(viacol * ViaGrid/2), \
	mm2mils100(viarow * ViaGrid/2), \
	mm2mils100(viacol * ViaGrid/2), \
	mm2mils100(viarow * ViaGrid/2), \
	mm2mils100(ViaGrid/2), \
	0, \
 	0, \
	'"pin33" "33" "square,nopaste"]'

# pins
for pin in range (1,17):
    print '   Pad[',\
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(PinRow/2 - PinHeight/2 + PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(PinRow/2 + PinHeight/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (pin), '"%i"' % (pin), '"square"]'

    print '   Pad[',\
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(-PinRow/2 + PinHeight/2 - PinWidth/2), \
 	mm2mils100((pin - 8.5) * PinSpacing), \
	mm2mils100(-PinRow/2 - PinHeight/2 + PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
	mm2mils100(PinResist), \
	'"pin%i"' % (33-pin), '"%i"' % (33-pin), '"square"]'

#    print '   Pad[',\
# 	mm2mils100(-2.5 + pin * PinSpacing), \
#	mm2mils100(+Overall/2 - PinHeight + PinWidth/2), \
# 	mm2mils100(-2.5 + pin * PinSpacing), \
#	mm2mils100(+Overall/2 - PinWidth/2), \
#	mm2mils100(PinWidth), \
#	mm2mils100(PinSpacing - PinWidth), \
#	mm2mils100(PinResist), \
#	'"pin%i"' % pin, '"%i"' % pin, '0x0000]'
#
#    print '   Pad[',\
#	mm2mils100(Overall/2 - PinHeight + PinWidth/2), \
# 	mm2mils100(-2.5 + pin * PinSpacing), \
#	mm2mils100(Overall/2 - PinWidth/2), \
# 	mm2mils100(-2.5 + pin * PinSpacing), \
#	mm2mils100(PinWidth), \
#	mm2mils100(PinSpacing - PinWidth), \
#	mm2mils100(PinResist), \
#	'"pin%i"' % (19-pin), '"%i"' % (19-pin), '0x0000]'
#
#    print '   Pad[',\
#	mm2mils100(-Overall/2 + PinWidth/2), \
# 	mm2mils100(-2.5 + pin * PinSpacing), \
#	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
# 	mm2mils100(-2.5 + pin * PinSpacing), \
#	mm2mils100(PinWidth), \
#	mm2mils100(PinSpacing - PinWidth), \
#	mm2mils100(PinResist), \
#	'"pin%i"' % (27+pin), '"%i"' % (27+pin), '0x0000]'

print '   ElementArc[',\
	mm2mils100(-7.5 * PinSpacing), \
	mm2mils100(PinRow/2 + PinHeight * 0.75), \
	'500 500 0 360 1000 ]'
print ")"
