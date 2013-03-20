# author: Keith Packard
# email: keithp@keithp.com
# dist-license: GPL 2
# use-license: unlimited

import sys

def mm2mils100( mm ):
	return int( mm / 25.4 * 1000.0 * 100.0 + 0.5 )

PadWidth = 0.60
PadHeight = 0.85
PadSpacing = 1.20
PadToHoldX = 0.80
PadToHoldY = 3.75
HoldWidth = 0.70
HoldHeight = 0.80
Clearance = 0.6

OutlineX = 1.5
OutlineYPad = - (0.38 / 2)
OutlineYHold = OutlineYPad + 4.5

NumPad=int(sys.argv[1])

print '# author: Keith Packard'
print '# email: keithp@keithp.com'
print '# dist-license: GPL 2'
print '# use-license: unlimited'

print 'Element["" "pico-ezmate-%d" "" "" 0 0 0 0 0 100 ""]' % NumPad
print "("

PadX = PadSpacing * NumPad / 2

# Hold-down pads

HoldY = PadHeight / 2 + PadToHoldY - HoldHeight / 2

def pad(cx, cy, w, h, name, num):
    x1 = 0
    y1 = 0
    x2 = 0
    y2 = 0
    thickness = 0
    if w > h:
        thickness = h
        y1 = cy
        x1 = cx - (w - h) / 2
        y2 = cy
        x2 = cx + (w - h) / 2
    else:
        thickness = w
        x1 = cx
        y1 = cy - (h - w) / 2
        x2 = cx
        y2 = cy + (h - w) / 2
    mask = thickness + Clearance / 2
    print '    Pad[',\
        mm2mils100(x1), \
        mm2mils100(y1), \
        mm2mils100(x2), \
        mm2mils100(y2), \
        mm2mils100(thickness), \
        mm2mils100(Clearance), \
        mm2mils100(mask),\
        '"%s"' % name, '"%s"' % num, '"square"]'
    
def line(x1, y1, x2, y2):
    print '    ElementLine[',\
        mm2mils100(x1), \
        mm2mils100(y1), \
        mm2mils100(x2), \
        mm2mils100(y2), \
        '500]'
    
def rect(x, y, w, h):
    line(x,y,x+w,y)
    line(x+w,y,x+w,y+h)
    line(x+w,y+h,x,y+h)
    line(x,y+h,x,y)

def padx(p):
    return -PadSpacing * (NumPad-1) / 2 + PadSpacing * (p - 1)

def holdx(h):
    return h * (padx(1) - PadToHoldX - HoldWidth / 2)


for p in range(1,NumPad+1):
    pad(padx(p), 0, PadWidth, PadHeight, 'pin%i' % p, '%i' % p)

for h in -1, 1:
    pad(holdx(h), HoldY, HoldWidth, HoldHeight, 'GND', 'GND')

rect(padx(1) - OutlineX, OutlineYPad,
     PadSpacing * (NumPad-1) + OutlineX*2,
     4.5)

print '    )'    
	# 11000 2000
#	ElementLine[-11000 -1000 -3600 -1000 100]
#	ElementLine[  3600 -1000 11000 -1000 100]
#
#	ElementLine[11000 -1000 11000 17000 100]
#	ElementLine[11000 17000 6000 17000 100]
#	ElementLine[ 6000 17000 4000 15000 100]
#	ElementLine[ 4000 15000 -4000 15000 100]
#	ElementLine[-4000 15000 -6000 17000 100]
#	ElementLine[-6000 17000 -11000 17000 100]
#	ElementLine[-11000 17000 -11000 -1000 100]
#	)
#
