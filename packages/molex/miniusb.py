#!/usr/bin/python
# Copyright 2007 by Bdale Garbee <bdale@gag.com>.  GPLv2
#
# Program to emit PCB footprint for
#   Molex MiniUSB R/A 5 pos SMD connector 54819-0572, DigiKey WM17116CT-ND
#

# dimensions in mm from 548190572_sd.pdf datasheet
TabWidth = 2.05
Tab1Height = 4.0
Tab2Height = 3.5
TabCenters = 4.25
BetweenTabs = 7.8

PinWidth = 0.5
PinHeight = 2.25
PinSpacing = 0.8
PinStart = 3.1 + Tab1Height/2

CenterLine = TabWidth + BetweenTabs/2

import sys

# we're going to use the 1/100 of a mil fundamental unit form
def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

print '# author: Bdale Garbee'
print '# email: bdale@gag.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element[0x0 "MiniUSB" "" "" 0 0 -10161 -12011 0 100 0x0]'
print "("
print '   Pad[', \
 	mm2mils100(CenterLine), \
	mm2mils100(PinStart + PinWidth/2), \
 	mm2mils100(CenterLine), \
	mm2mils100(PinStart + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.2), \
	'"D+" "3" 0x0100]'

print '   Pad[', \
 	mm2mils100(CenterLine + PinSpacing), \
	mm2mils100(PinStart + PinWidth/2), \
 	mm2mils100(CenterLine + PinSpacing), \
	mm2mils100(PinStart + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.2), \
	'"D-" "2" 0x0100]'

print '   Pad[', \
 	mm2mils100(CenterLine - PinSpacing), \
	mm2mils100(PinStart + PinWidth/2), \
 	mm2mils100(CenterLine - PinSpacing), \
	mm2mils100(PinStart + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.2), \
	'"HS" "4" 0x0100]'

print '   Pad[', \
 	mm2mils100(CenterLine + PinSpacing*2), \
	mm2mils100(PinStart + PinWidth/2), \
 	mm2mils100(CenterLine + PinSpacing*2), \
	mm2mils100(PinStart + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.2), \
	'"VBUS" "1" 0x0100]'

print '   Pad[', \
 	mm2mils100(CenterLine - PinSpacing*2), \
	mm2mils100(PinStart + PinWidth/2), \
 	mm2mils100(CenterLine - PinSpacing*2), \
	mm2mils100(PinStart + PinHeight - PinWidth/2), \
	mm2mils100(PinWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(PinWidth + 0.2), \
	'"GND" "5" 0x0100]'

TabRowTwo = Tab1Height/2 + TabCenters - Tab2Height/2
TabColTwo = TabWidth + BetweenTabs

print '   Pad[', \
  	mm2mils100(TabWidth/2), \
	mm2mils100(TabWidth/2), \
	mm2mils100(TabWidth/2), \
	mm2mils100(Tab1Height - TabWidth/2), \
	mm2mils100(TabWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(TabWidth + 0.2), \
	'"tab1" "G" 0x0100]'

print '   Pad[', \
	mm2mils100(TabWidth/2), \
  	mm2mils100(TabRowTwo + TabWidth/2), \
	mm2mils100(TabWidth/2), \
  	mm2mils100(TabRowTwo + Tab2Height - TabWidth/2), \
	mm2mils100(TabWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(TabWidth + 0.2), \
	'"tab2" "G" 0x0100]'

print '   Pad[', \
  	mm2mils100(TabColTwo + TabWidth/2), \
	mm2mils100(TabWidth/2), \
	mm2mils100(TabColTwo + TabWidth/2), \
	mm2mils100(Tab1Height - TabWidth/2), \
	mm2mils100(TabWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(TabWidth + 0.2), \
	'"tab3" "G" 0x0100]'

print '   Pad[', \
  	mm2mils100(TabColTwo + TabWidth/2), \
  	mm2mils100(TabRowTwo + TabWidth/2), \
  	mm2mils100(TabColTwo + TabWidth/2), \
  	mm2mils100(TabRowTwo + Tab2Height - TabWidth/2), \
	mm2mils100(TabWidth), \
	mm2mils100(PinSpacing - PinWidth), \
  	mm2mils100(TabWidth + 0.2), \
	'"tab4" "G" 0x0100]'

print ")"
