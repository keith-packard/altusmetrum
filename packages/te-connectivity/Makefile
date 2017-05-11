all:	284512-4.fp 282834-10.fp 0-215079-4.fp tphybrid.fp bnc-th.fp

bnc-th.fp:	bnc-th.py
	./bnc-th.py > bnc-th.fp

284512-4.fp:	3.5mm-ra.py 3.5mm-series.sh
	./3.5mm-series.sh

282834-10.fp:	buchanan.py buchanan-Series.sh
	./buchanan-Series.sh

0-215079-4.fp:	micromatch micromatch-th-v.py
	./micromatch

tphybrid.fp:	tphybrid.py
	./tphybrid.py > tphybrid.fp

clean:
	rm -f *.fp
