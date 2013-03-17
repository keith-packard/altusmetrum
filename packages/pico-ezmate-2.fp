# author: Keith Packard
# email: keithp@keithp.com
# dist-license: GPL 2
# use-license: unlimited


Element["" "pico-ezmate-2" "" "" 10885 1927 -10161 -12011 0 100 ""]
(
	Pad[-2362 -492 -2362 492 2362 2500 2962 "1" "1" "square"]
	Pad[2362 -492 2362 492 2362 2500 2962 "2" "2" "square"]
	Pad[9252 14567 9252 14961 2756 2500 3356 "GND" "GND" "square,edge2"]
	Pad[-9252 14567 -9252 14961 2756 2500 3356 "GND" "GND" "square,edge2"]

	# 11000 2000
	ElementLine[-11000 -1000 -3600 -1000 100]
	ElementLine[  3600 -1000 11000 -1000 100]

	ElementLine[11000 -1000 11000 17000 100]
	ElementLine[11000 17000 6000 17000 100]
	ElementLine[ 6000 17000 4000 15000 100]
	ElementLine[ 4000 15000 -4000 15000 100]
	ElementLine[-4000 15000 -6000 17000 100]
	ElementLine[-6000 17000 -11000 17000 100]
	ElementLine[-11000 17000 -11000 -1000 100]
	)
