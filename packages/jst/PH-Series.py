#!/bin/sh

for i in 2 3 4 5 6 7 8 9 10 11 12 13 14 15
do
	# side entry surface mount
	FILE="S"$i"B-PH-SM"
	./PH-smt-ra.py $i > $FILE.fp

	# top entry through hole
	FILE="B"$i"B-PH"
	./PH-th-v.py $i > $FILE.fp

	# side entry through hole
	FILE="S"$i"B-PH"
	./PH-th-ra.py $i > $FILE.fp
done
