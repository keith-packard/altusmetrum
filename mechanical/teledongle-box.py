#! /usr/bin/python
# Copyright 2017 by Bdale Garbee <bdale@gag.com>.  GPLv3

# cut the required holes in a Hammond 1551NTBU box to mount TeleDongle

# we assume the box starts out standing on edge, with the bottom of the box 
# to the "rear" (away from the front of the mill) against a reference plane, 
# and the left edge of the box also up against a reference block.  The box
# is then flipped 180 degrees putting the right edge of the box against the
# reference plane to drill the cable hole.

# the Z reference plane is top surface of the box, X is the left edge of box

import math

Zfree = 0.1000		# height in Z to clear all obstructions
Speed = 10		# cutting speed
Zdepth = 0.125		# how deep we need to cut to go cleanly through the 
			# box wall, where the wall is 0.079 thick

CutterSize = 0.0625	# 1/16" end mill
RunOut = 0.0000		# how much larger slots are than desired 
CutterOD = CutterSize + RunOut

BoxWidth = 1.378

D_SMA = 0.281		# diameter of SMA hole (doc says 0.256)

Box_Bottom = 0.472	# how tall the bottom of the box is

D_Cable = 0.180		# cable diameter, as measured
Y_Cable = Box_Bottom - D_Cable/2	# centerline of hole for cable
Y_fudge = 0.025		# fudge factor to ensure top of cable hole open

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

print "(TeleDongle Box using 1/16 end mill)"
print "G17 G20 G90"
print "M3 S5000"

retract()

print
print "(SMA hole)"

X_Pos = (BoxWidth / 2)
#Y_Pos = -(Y_Box_Bottom + Y_Standoff + Y_PCB + Y_SMA)
# above should be correct, but puts the hole too high!
Y_Pos = -(Y_Box_Bottom + Y_Standoff + Y_PCB)
CutLineRadius = (D_SMA / 2) - (CutterOD / 2)

print "G00 X",(X_Pos + CutLineRadius),"Y",Y_Pos
print "G01 Z",-Zdepth," F",Speed
print "G02 X%6.4f" % (X_Pos - CutLineRadius),"Y%6.4f" % Y_Pos,"I%6.4f" % -CutLineRadius,"J0 F",Speed
print "G02 X%6.4f" % (X_Pos + CutLineRadius),"Y%6.4f" % Y_Pos,"I%6.4f" % CutLineRadius,"J0 F",Speed

print "(pausing for box flip)"
retract()
print "M5"
park()
print "M0"

print
print "(cable hole)"
print "M3 S5000"

X_Pos = (BoxWidth / 2)
Y_Pos = -Y_Cable
CutLineRadius = (D_Cable / 2) - (CutterOD / 2)

print "G00 X",(X_Pos - CutLineRadius),"Y",Y_Pos
print "G01 Z",-Zdepth," F",Speed
print "G02 X%6.4f" % (X_Pos + CutLineRadius),"Y%6.4f" % Y_Pos,"I%6.4f" % CutLineRadius,"J0 F",Speed
print "G01 X%6.4f" % (X_Pos + CutLineRadius),"Y%6.4f" % -(Box_Bottom - (CutterOD / 2) + Y_fudge),"F",Speed
print "G01 X%6.4f" % (X_Pos - CutLineRadius),"Y%6.4f" % -(Box_Bottom - (CutterOD / 2) + Y_fudge),"F",Speed
print "G01 X%6.4f" % (X_Pos - CutLineRadius),"Y%6.4f" % Y_Pos,"F",Speed

retract()
print "M5"
park()

print "M2"
print "%"

