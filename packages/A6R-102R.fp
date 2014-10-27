# retain backwards compatibility to older versions of PKG_DIL 
# which did not have 100,60,28 args
Element(0x00 "A6R Rotary Switches" "" "A6R-102R" 220 100 3 100 0x00)
(
	Pin(50 50 68 36 "1" 0x101)
	Pin(50 150 68 36 "2" 0x01)
	Pin(50 250 68 36 "3" 0x01)
	Pin(350 250 68 36 "4" 0x01)
	Pin(350 150 68 36 "5" 0x01)
	Pin(350 50 68 36 "6" 0x01)
	ElementLine(0 0 0 300 10)
	ElementLine(0 300 400 300 10)
	ElementLine(400 300 400 0 10)
	ElementLine(0 0 150 0 10)
	ElementLine(250 0 400 0 10)
	ElementArc(200 0 50 50 0 180 10)
	Mark(200 150)
)
