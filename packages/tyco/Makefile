all:	282834-10.fp 0-215079-4.fp tphybrid.fp

282834-10.fp:	buchanan.py buchanan-Series.sh
	./buchanan-Series.sh

0-215079-4.fp:	micromatch micromatch-th-v.py
	./micromatch

tphybrid.fp:	tphybrid.py
	./tphybrid.py > tphybrid.fp

clean:
	rm -f *.fp
