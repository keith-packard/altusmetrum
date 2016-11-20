all:	181-all 182-all 189-all

181-all:	181-f-15.fp 181-f-26.fp 181-f-44.fp 181-f-62.fp 

181-f-15.fp:	181-female.py
	./181-female.py 15 > 181-f-15.fp
181-f-26.fp:	181-female.py
	./181-female.py 26 > 181-f-26.fp
181-f-44.fp:	181-female.py
	./181-female.py 44 > 181-f-44.fp
181-f-62.fp:	181-female.py
	./181-female.py 62 > 181-f-62.fp

182-all:	182-f-9.fp 182-f-15.fp 182-f-25.fp 182-f-37.fp \
		182-m-9.fp 182-m-15.fp 182-m-25.fp 182-m-37.fp

182-f-9.fp:	182-female.py
	./182-female.py 9 > 182-f-9.fp
182-f-15.fp:	182-female.py
	./182-female.py 15 > 182-f-15.fp
182-f-25.fp:	182-female.py
	./182-female.py 25 > 182-f-25.fp
182-f-37.fp:	182-female.py
	./182-female.py 37 > 182-f-37.fp

182-m-9.fp:	182-female.py
	./182-male.py 9 > 182-m-9.fp
182-m-15.fp:	182-male.py
	./182-male.py 15 > 182-m-15.fp
182-m-25.fp:	182-male.py
	./182-male.py 25 > 182-m-25.fp
182-m-37.fp:	182-male.py
	./182-male.py 37 > 182-m-37.fp

189-all:	189-9.fp 189-15.fp 189-25.fp 189-37.fp

189-9.fp:	189.py
	./189.py 9 > 189-9.fp
189-15.fp:	189.py
	./189.py 15 > 189-15.fp
189-25.fp:	189.py
	./189.py 25 > 189-25.fp
189-37.fp:	189.py
	./189.py 37 > 189-37.fp

clean:
	rm -f *.fp *-
