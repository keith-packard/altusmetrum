all:	532610372.fp 548190572.fp 903259004.fp ufl.fp \
	pico-ezmate-6.fp \
	pico-ezmate-4.fp \
	pico-ezmate-2.fp

903259004.fp:	picoflex picoflex-th-v.py
	./picoflex

532610372.fp:	picoblades picoblade-smt-ra.py picoblade-th-v.py
	./picoblades

548190572.fp:	miniusb.py
	./miniusb.py > 548190572.fp

ufl.fp:	ufl.py
	./ufl.py > ufl.fp

pico-ezmate-6.fp: pico-ezmate.py
	python pico-ezmate.py 6 >$@

pico-ezmate-4.fp: pico-ezmate.py
	python pico-ezmate.py 4 >$@

pico-ezmate-2.fp: pico-ezmate.py
	python pico-ezmate.py 2 >$@

clean:
	rm -f 53261* 53047* 90325* 548190572.fp ufl.fp pico-ezmate-*.fp
