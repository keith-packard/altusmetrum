#!/usr/bin/python
# Copyright 2011 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Hirose Micro USB B SMD R/A connector ZX62-B-5PA(11), DigiKey H11634CT-ND
#

# dimensions in mm from e24200011.pdf page 4
PinWidth = 0.4
PinHeight = 1.35
PinSpacing = 0.65

TabWidth = 2.1
TabHeight = 1.6
TabInner = 2.05

PadWidth = 1.9
PadHeight = 1.9
PadInner = 0.25
PadCenter = 3.35

WingWidth = 1.8
WingHeight = 1.9
WingInner = 3.1

# draw a box around the actual connector, and a line a the PCB edge
# connector is 7.9mm wide and 5.6mm deep overall, but wants to stick over
# the board edge due to flare around opening.  The flare should be only 0.6mm
# deep, but the recommendation is that the connector face be 1.3mm out...
BoxHeight = 6.1
BoxWidth = 7.9
EdgeHeight = 4.8
EdgeWidth = 2 * (WingInner + WingWidth)

# freedfm.com round-off error bites us if we make this 700...
MinAnnular = 725
MinClearance = 600
MaskDelta = 300

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "USBmicroB" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
print '   Pad[', \
 	mm2mils100(0), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(0), \
	mm2mils100(PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
  	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"D+" "3" 0x0100]'

print '   Pad[', \
 	mm2mils100(-PinSpacing), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(-PinSpacing), \
	mm2mils100(PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
  	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"D-" "2" 0x0100]'

print '   Pad[', \
 	mm2mils100(PinSpacing), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(PinSpacing), \
	mm2mils100(PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
  	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"HS" "4" 0x0100]'

print '   Pad[', \
 	mm2mils100(-PinSpacing*2), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(-PinSpacing*2), \
	mm2mils100(PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
  	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"VBUS" "1" 0x0100]'

print '   Pad[', \
 	mm2mils100(PinSpacing*2), \
	mm2mils100(PinWidth/2), \
 	mm2mils100(PinSpacing*2), \
	mm2mils100(PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	(MinClearance*2), \
  	mm2mils100(PinWidth)+(MaskDelta*2), \
	'"GND" "5" 0x0100]'

# the two ground / mounting tabs in line with signal pins

print '   Pad[', \
  	mm2mils100(TabInner + TabHeight/2), \
	mm2mils100(TabHeight/2), \
	mm2mils100(TabInner + TabWidth - TabHeight/2), \
	mm2mils100(TabHeight/2), \
	mm2mils100(TabHeight), \
	(MinClearance*2), \
  	mm2mils100(TabHeight)+(MaskDelta*2), \
	'"tab1" "G" 0x0100]'

print '   Pad[', \
  	mm2mils100(-TabInner - TabHeight/2), \
	mm2mils100(TabHeight/2), \
	mm2mils100(-TabInner - TabWidth + TabHeight/2), \
	mm2mils100(TabHeight/2), \
	mm2mils100(TabHeight), \
	(MinClearance*2), \
  	mm2mils100(TabHeight)+(MaskDelta*2), \
	'"tab2" "G" 0x0100]'

# the two ground / mounting tabs near the center of area

print '   Pad[', \
  	mm2mils100(PadInner + PadHeight/2), \
	mm2mils100(PadCenter), \
	mm2mils100(PadInner + PadWidth - PadHeight/2), \
	mm2mils100(PadCenter), \
	mm2mils100(PadHeight), \
	(MinClearance*2), \
  	mm2mils100(PadHeight)+(MaskDelta*2), \
	'"tab3" "G" 0x0100]'

print '   Pad[', \
  	mm2mils100(-PadInner - PadHeight/2), \
	mm2mils100(PadCenter), \
	mm2mils100(-PadInner - PadWidth + PadHeight/2), \
	mm2mils100(PadCenter), \
	mm2mils100(PadHeight), \
	(MinClearance*2), \
  	mm2mils100(PadHeight)+(MaskDelta*2), \
	'"tab4" "G" 0x0100]'

# the two "wing tab" ground / mounting pads on the sides

print '   Pad[', \
  	mm2mils100(WingInner + WingWidth/2), \
	mm2mils100(PadCenter - WingHeight/2 + WingWidth/2), \
	mm2mils100(WingInner + WingWidth/2), \
	mm2mils100(PadCenter + WingHeight/2 - WingWidth/2), \
	mm2mils100(WingWidth), \
	(MinClearance*2), \
  	mm2mils100(WingWidth)+(MaskDelta*2), \
	'"tab5" "G" 0x0100]'

print '   Pad[', \
  	mm2mils100(-WingInner - WingWidth/2), \
	mm2mils100(PadCenter - WingHeight/2 + WingWidth/2), \
	mm2mils100(-WingInner - WingWidth/2), \
	mm2mils100(PadCenter + WingHeight/2 - WingWidth/2), \
	mm2mils100(WingWidth), \
	(MinClearance*2), \
  	mm2mils100(WingWidth)+(MaskDelta*2), \
	'"tab6" "G" 0x0100]'

# box around actual connector size, with line at PCB edge
#
#print '   ElementLine[',\
# 	mm2mils100(-BoxWidth/2), \
#	mm2mils100(0), \
#	mm2mils100(-BoxWidth/2), \
#	mm2mils100(BoxHeight), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	mm2mils100(BoxWidth/2), \
#	mm2mils100(0), \
#	mm2mils100(BoxWidth/2), \
#	mm2mils100(BoxHeight), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	mm2mils100(-BoxWidth/2), \
#	mm2mils100(0), \
#	mm2mils100(BoxWidth/2), \
#	mm2mils100(0), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	mm2mils100(-BoxWidth/2), \
#	mm2mils100(BoxHeight), \
#	mm2mils100(BoxWidth/2), \
#	mm2mils100(BoxHeight), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	mm2mils100(-EdgeWidth/2), \
#	mm2mils100(EdgeHeight), \
#	mm2mils100(-BoxWidth/2), \
#	mm2mils100(EdgeHeight), \
#	'1000 ]'
#
#print '   ElementLine[',\
# 	mm2mils100(BoxWidth/2), \
#	mm2mils100(EdgeHeight), \
#	mm2mils100(EdgeWidth/2), \
#	mm2mils100(EdgeHeight), \
#	'1000 ]'
#
print ")"
