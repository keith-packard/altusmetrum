#! /usr/bin/python
# Copyright 2013 by Bdale Garbee <bdale@gag.com>.  GPLv3

# cut the required holes in a Hammond 1551K box to mount TeleBT

# we assume the box is standing on edge, with the bottom of the box to the
# "rear" (away from the front of the mill) against a reference plane, and
# the left edge of the box also up against a reference block.

# the Z reference plane is top surface of the box, X is the left edge of box

import math

Zfree = 0.1000		# height in Z to clear all obstructions
Speed = 10		# cutting speed
Zdepth = 0.125		# how deep we need to cut to go cleanly through the 
			# box wall, where the wall is 0.079 thick

CutterSize = 0.0625	# 1/16" end mill
RunOut = 0.0000		# how much larger slots are than desired 
CutterOD = CutterSize + RunOut

BoxWidth = 3.150	# measured one at 3.145, Hammond says 3.150, matters
			# because most dimensions are relative to center line!

X_Switch = -1.060	# switch distance from center line
Y_Switch = 0.185	# switch centerline above PCB top surface
D_Switch = 0.270	# diameter of switch hole (250 mils plus clearance)

X_USB = 0.935		# USB distance from center line
Y_USB = -0.049		# USB centerline below PCB bottom surface

#X_USB_slot = 0.325	# width of the USB slot
#Y_USB_slot = 0.125	# height of the USB slot
X_USB_slot = 0.350	# width of the USB slot	 (account for plastic melting
Y_USB_slot = 0.150	# height of the USB slot  around end mill)

Y_SMA = -0.025		# SMA centerline below PCB bottom surface
D_SMA = 0.281		# diameter of SMA hole (doc says 0.256)

Y_Box_Bottom = 0.079	# thickness of box bottom wall
Y_Standoff = 0.157	# height of standoff nubs in box
Y_PCB = 0.063		# PCB thickness

def plunge():
	print "(plunge)"
	print "G01 Z",-Zdepth," F",Speed

def retract():
	print "(retract)"
	print "G00 Z",Zfree

def park():
	retract()
	print "(park)"
	print "G00 X0 Y5 Z0.25"

print "%"

print "G17 G20 G90"
print "M3 S5000"

retract()

# cut power switch hole

print
print "(power switch hole)"

X_Pos = (BoxWidth / 2) + X_Switch
Y_Pos = -(Y_Box_Bottom + Y_Standoff + Y_PCB + Y_Switch)
CutLineRadius = (D_Switch / 2) - (CutterOD / 2)

print "G00 X",(X_Pos + CutLineRadius),"Y",Y_Pos
print "G01 Z",-Zdepth," F",Speed
print "G02 X%6.4f" % (X_Pos - CutLineRadius),"Y%6.4f" % Y_Pos,"I%6.4f" % -CutLineRadius,"J0 F",Speed
print "G02 X%6.4f" % (X_Pos + CutLineRadius),"Y%6.4f" % Y_Pos,"I%6.4f" % CutLineRadius,"J0 F",Speed
retract()

print
print "(SMA hole)"

X_Pos = (BoxWidth / 2)
Y_Pos = -(Y_Box_Bottom + Y_Standoff + Y_SMA)
CutLineRadius = (D_SMA / 2) - (CutterOD / 2)

print "G00 X",(X_Pos + CutLineRadius),"Y",Y_Pos
print "G01 Z",-Zdepth," F",Speed
print "G02 X%6.4f" % (X_Pos - CutLineRadius),"Y%6.4f" % Y_Pos,"I%6.4f" % -CutLineRadius,"J0 F",Speed
print "G02 X%6.4f" % (X_Pos + CutLineRadius),"Y%6.4f" % Y_Pos,"I%6.4f" % CutLineRadius,"J0 F",Speed
retract()

print
print "(USB slot)"

print "(first end)"
X_Pos = (BoxWidth / 2) + X_USB + ((X_USB_slot - Y_USB_slot)/2)
Y_Pos = -(Y_Box_Bottom + Y_Standoff + Y_USB)
CutLineRadius = (Y_USB_slot / 2) - (CutterOD / 2)

print "G00 X",X_Pos,"Y",(Y_Pos - CutLineRadius)
print "G01 Z",-Zdepth," F",Speed
print "G03 X%6.4f" % X_Pos, "Y%6.4f" % (Y_Pos + CutLineRadius),"I0 J%6.4f" % CutLineRadius," F",Speed

print "(top and second end)"
X_Pos = (BoxWidth / 2) + X_USB - ((X_USB_slot - Y_USB_slot)/2)
print "G01 X",X_Pos," F",Speed
print "G03 X%6.4f" % X_Pos, "Y%6.4f" % (Y_Pos - CutLineRadius),"I0 J%6.4f" % -CutLineRadius," F",Speed

print "(bottom)"
X_Pos = (BoxWidth / 2) + X_USB + ((X_USB_slot - Y_USB_slot)/2)
print "G01 X",X_Pos," F",Speed

retract()

print "(second pass - first end)"
X_Pos = (BoxWidth / 2) + X_USB + ((X_USB_slot - Y_USB_slot)/2)
Y_Pos = -(Y_Box_Bottom + Y_Standoff + Y_USB)
CutLineRadius = (Y_USB_slot / 2) - (CutterOD / 2)

print "G00 X",X_Pos,"Y",(Y_Pos - CutLineRadius)
print "G01 Z",-Zdepth," F",Speed
print "G03 X%6.4f" % X_Pos, "Y%6.4f" % (Y_Pos + CutLineRadius),"I0 J%6.4f" % CutLineRadius," F",Speed

print "(second pass - top and second end)"
X_Pos = (BoxWidth / 2) + X_USB - ((X_USB_slot - Y_USB_slot)/2)
print "G01 X",X_Pos," F",Speed
print "G03 X%6.4f" % X_Pos, "Y%6.4f" % (Y_Pos - CutLineRadius),"I0 J%6.4f" % -CutLineRadius," F",Speed

print "(second pass - bottom)"
X_Pos = (BoxWidth / 2) + X_USB + ((X_USB_slot - Y_USB_slot)/2)
print "G01 X",X_Pos," F",Speed

retract()

park()

print "M5 M2"
print "%"

