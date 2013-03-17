#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for 16-lead QFN, 6x6mm 
# used by Freescale acceleromters like the MMA6556
#

# dimensions in mm from AN3111.pdf from Freescale, the Wettable Flank variant
PinWidth = 0.50
PinHeight = 0.85
PinSpacing = 1.00
Overall = 6.0
CoreSquare = 4.00
CornerSquare = 0.55
MaskAdd = 0.15

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "AN3111" "" "" 0 0 0 0 0 100 0x0]'
print "("
# pad under the chip, no overall paste so we can control subset that gets paste
print '   Pad[',\
 	mm2mils100(0), \
	mm2mils100(0), \
 	mm2mils100(0), \
	mm2mils100(0), \
	mm2mils100(CoreSquare), \
	mm2mils100(0), \
  	mm2mils100(CoreSquare + MaskAdd), \
	'"17" "17" "square,nopaste"]'

# copper sub-squares in a grid to set paste area
for viarow in range (-1, 2):
  for viacol in range (-1, 2):
      print '   Pad[',\
        mm2mils100(viacol * 1.4), \
        mm2mils100(viarow * 1.4), \
        mm2mils100(viacol * 1.4), \
        mm2mils100(viarow * 1.4), \
	mm2mils100(1.0), \
        0, \
        mm2mils100(1.0), \
        '"17" "17" "square"]'


# corner mounting squares .. tied to Vss on chip, but don't connect on board
print '   Pad[',\
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
	mm2mils100(CornerSquare), \
	mm2mils100(0), \
  	mm2mils100(CornerSquare + MaskAdd), \
	'"NC" "NC" 0x0100]'

print '   Pad[',\
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
	mm2mils100(CornerSquare), \
	mm2mils100(0), \
  	mm2mils100(CornerSquare + MaskAdd), \
	'"NC" "NC" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
 	mm2mils100(CoreSquare/2 + 0.37 + CornerSquare/2), \
	mm2mils100(CornerSquare), \
	mm2mils100(0), \
  	mm2mils100(CornerSquare + MaskAdd), \
	'"NC" "NC" 0x0100]'

print '   Pad[',\
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
 	mm2mils100(-(CoreSquare/2 + 0.37 + CornerSquare/2)), \
	mm2mils100(CornerSquare), \
	mm2mils100(0), \
  	mm2mils100(CornerSquare + MaskAdd), \
	'"NC" "NC" 0x0100]'

for pin in range (1,5):
    print '   Pad[',\
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(-Overall/2 - 0.30 + PinWidth/2), \
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(-Overall/2 + 0.55 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth + MaskAdd), \
	'"pin%i"' % (13-pin), '"%i"' % (13-pin), '0x0100]'

    print '   Pad[',\
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(+Overall/2 - 0.55 + PinWidth/2), \
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(+Overall/2 + 0.30 - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth + MaskAdd), \
	'"pin%i"' % pin, '"%i"' % pin, '0x0100]'

    print '   Pad[',\
	mm2mils100(Overall/2 - 0.55 + PinWidth/2), \
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(Overall/2 + 0.30 - PinWidth/2), \
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth + MaskAdd), \
	'"pin%i"' % (9-pin), '"%i"' % (9-pin), '0x0100]'

    print '   Pad[',\
	mm2mils100(-Overall/2 - 0.30 + PinWidth/2), \
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(-Overall/2 + 0.55 - PinWidth/2), \
 	mm2mils100(-2.5 + pin * PinSpacing), \
	mm2mils100(PinWidth), \
	mm2mils100(0), \
  	mm2mils100(PinWidth + MaskAdd), \
	'"pin%i"' % (12+pin), '"%i"' % (12+pin), '0x0100]'

print '   ElementArc[',\
	mm2mils100(-3.2), \
	mm2mils100(3.2), \
	'500 500 0 360 1000 ]'
print ")"
