all:	532610372.fp 548190572.fp 903259004.fp ufl.fp

903259004.fp:	picoflex picoflex-th-v.py
	./picoflex

532610372.fp:	picoblades picoblade-smt-ra.py picoblade-th-v.py
	./picoblades

548190572.fp:	miniusb.py
	./miniusb.py > 548190572.fp

ufl.fp:	ufl.py
	./ufl.py > ufl.fp

clean:
	rm -f 53261* 53047* 90325* 548190572.fp ufl.fp
