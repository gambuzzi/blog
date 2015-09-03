title: Fattoriale
lang: it
tags: python
Category: Python
Date: 2012-04-29 14:04


Fattoriale minimale!

	fattoriale = lambda z: reduce(lambda x,y: x*(y+1), xrange(z), 1)