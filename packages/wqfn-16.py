#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
# Copyright 2019 by Keith Packard <keithp@keithp.com>.  GPLv2+
#
# Program to emit PCB footprint for WQFN-16 package used by the DRV8800
#

# dimensions in mm from the DRV8800

PinWidth = 0.3	  # b	
PinHeight = 0.95  # L
PinSpacing = 0.65 # e
Overall = 4.75    # E
GndSquare = 2.1  # D2 & E2
CoreSquare = 2.1
PinClearance = 2 * (PinSpacing - PinWidth)

# ATMEL specifies 120-150 microns between pad and solder mask
# AT88RF1354 Appplication note
#
PinResist = PinWidth + (2 * 0.07)

import sys

# we're going to use the 1/100 of a mil fundamental unit form

def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Keith Packard'
print '# email: keithp@keithp.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "qfn-16" "" "" 0 0 0 0 0 100 0x0]'
print "("

# pad under the chip, must be grounded
print '   Pad[',\
 	mm2mils100(0), \
	mm2mils100(0), \
 	mm2mils100(0), \
	mm2mils100(0), \
	mm2mils100(GndSquare), \
	mm2mils100(PinClearance), \
	mm2mils100(PinResist), \
	'"pin17" "17" "square,nopaste"]'

# vias in the ground pad under the chip
for viarow in range (-1,1):
  for viacol in range (-1,1):
    print '   Pin[',\
	mm2mils100(1.8 * viacol * CoreSquare / 3 + .9 * CoreSquare/3), \
 	mm2mils100(1.8 * viarow * CoreSquare / 3 + .9 * CoreSquare/3), \
	2600, \
	2500, \
  	0, \
  	1300, \
	'"pin17" "17" 0x0002]'

# break pad under chip into a grid to control the resist and paste masks

blocks=3;

for viarow in range (-1, 2):
  for viacol in range (-1, 2):
    if (viarow in (-1, 1)) and (viacol in (-1, 1)):
      # copper sub-square with resist over vias
      print '   Pad[',\
	mm2mils100(viacol * CoreSquare / blocks), \
 	mm2mils100(viarow * CoreSquare / blocks), \
	mm2mils100(viacol * CoreSquare / blocks), \
 	mm2mils100(viarow * CoreSquare / blocks), \
	mm2mils100((CoreSquare)/blocks), \
	0, \
 	0, \
	'"pin17" "17" "square,nopaste"]'
    else:
      # copper sub-square without resist
      print '   Pad[',\
	mm2mils100(viacol * CoreSquare / blocks), \
 	mm2mils100(viarow * CoreSquare / blocks), \
	mm2mils100(viacol * CoreSquare / blocks), \
 	mm2mils100(viarow * CoreSquare / blocks), \
	mm2mils100((CoreSquare)/blocks), \
	0, \
	mm2mils100((CoreSquare)/blocks), \
	'"pin17" "17" "square,nopaste"]'
      # copper spot to control paste mask generation
      print '   Pad[',\
	mm2mils100(viacol * CoreSquare / blocks), \
 	mm2mils100(viarow * CoreSquare / blocks), \
	mm2mils100(viacol * CoreSquare / blocks), \
 	mm2mils100(viarow * CoreSquare / blocks), \
  	1500, \
	0, \
	mm2mils100((CoreSquare)/blocks), \
	'"pin17" "17" "square"]'

# pins
for pin in range (1,5):
    print '   Pad[',\
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinClearance), \
	mm2mils100(PinResist), \
	'"pin%i"' % (13-pin), '"%i"' % (13-pin), '0x0000]'

    print '   Pad[',\
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(+Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(+Overall/2 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinClearance), \
	mm2mils100(PinResist), \
	'"pin%i"' % pin, '"%i"' % pin, '0x0000]'
      
    print '   Pad[',\
	mm2mils100(Overall/2 - PinHeight + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(Overall/2 - PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinClearance), \
	mm2mils100(PinResist), \
	'"pin%i"' % (9-pin), '"%i"' % (9-pin), '0x0000]'

    print '   Pad[',\
	mm2mils100(-Overall/2 + PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(-Overall/2 + PinHeight - PinWidth/2), \
 	mm2mils100((-2.5 + pin) * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(PinClearance), \
	mm2mils100(PinResist), \
	'"pin%i"' % (12+pin), '"%i"' % (12+pin), '0x0000]'

print '   ElementArc[',\
	mm2mils100(-2.0), \
	mm2mils100(2.0), \
	'500 500 0 360 1000 ]'
print ")"
