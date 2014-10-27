# author: Keith Packard
# email: keithp@keithp.com
# dist-license: GPL 2
# use-license: unlimited
Element[0x0 "74x" "" "" 0 0 -10000 -10000 0 100 0x0]
(
#
   Pad[ -5000  2250 -5000  4400 1400 900 2000 "1" "1" 0x100]
   Pad[ -2500  2250 -2500  4400 1400 900 2000 "2" "2" 0x100]
   Pad[     0  2250     0  4400 1400 900 2000 "3" "3" 0x100]
   Pad[  2500  2250  2500  4400 1400 900 2000 "4" "4" 0x100]
   Pad[  5000  2250  5000  4400 1400 900 2000 "C" "C" 0x100]

   Pad[ -5000 -2250 -5000 -4400 1400 900 2000 "C" "C" 0x100]
   Pad[ -2500 -2250 -2500 -4400 1400 900 2000 "9" "9" 0x100]
   Pad[     0 -2250     0 -4400 1400 900 2000 "8" "8" 0x100]
   Pad[  2500 -2250  2500 -4400 1400 900 2000 "7" "7" 0x100]
   Pad[  5000 -2250  5000 -4400 1400 900 2000 "6" "6" 0x100]

   ElementLine [ -6700  6050  6700  6050 1000 ]
   ElementLine [  6700 -6050 -6700 -6050 1000 ]
   ElementLine [  6700  6050  6700 -6050 1000 ]
   ElementLine [ -6700 -6050 -6700  6050 1000 ]
)
