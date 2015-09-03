title: Dadi e regex
lang: it
tags: python
Category: Python
Date: 2014-09-15


Da giocatore di ruolo ci si trova spesso a dovere tirare dadi. Nonostante non mi siano mai piaciuti i lanciatori di dati software, ho voluto analizzare il problema di parsare una espressione che rappresenta i dadi da tirare.

Alcuni esempi:

- 1d6 - il comune dado a 6 facce
- 2d6 - tira 2 volte il dado da 6
- 2d6-1 - come prima ma poi sottrai 1
- 1d100 - un dado a 100 facce.
- 1d20+2 - un dado da 20 più 2
- 1d6+1-1d4

Quindi dobbiamo match-are ogni singolo blocco ed elaborarlo.

Partiamo da una semplice regex per prendere le espressioni con la "d" in mezzo.

	:::python
	>>> re.findall(r'(\d+)d(\d+)', "1d6+1-1d4")
	[('1', '6'), ('1', '4')]

ok, pero' ci serve anche il segno

	:::python
	>>> re.findall(r'([+-])(\d+)d(\d+)', "1d6+1-1d4")
	[('-', '1', '4')]

ma è opzionale, altrimenti perdiamo il primo dado.

	:::python
	>>> re.findall(r'([+-])?(\d+)d(\d+)', "1d6+1-1d4")
	[('', '1', '6'), ('-', '1', '4')]

prendiamo anche le parti solo intere senza la "d(\d+)"

	:::python
	>>> re.findall(r'([+-])?(\d+)(?:d(\d+))?', "1d6+1-1d4")
	[('', '1', '6'), ('+', '1', ''), ('-', '1', '4')]

Aggiungiamo qualche `"\s*"` per prendere anche stringhe con gli spazi dentro.

	:::python
	>>> re.findall(r'([+-])?\s*(\d+)\s*(?:d\s*(\d+))?', "1 d6 + 1-1d4")
	[('', '1', '6'), ('+', '1', ''), ('-', '1', '4')]

Da qui possiamo scrivere una funzione che prenda la lista di tuple e ci calcoli un valore random del risultato.

	:::python
	# -*- coding: cp1252 -*-
	import re
	from random import randint
	
	def tira_dadi(lista):
	    ret = 0
	    for segno, molt, dado in lista:
	        dado = int(dado) if dado else 1 #se non c'è dado è un dado da 1
	        segno = int(segno+'1') if segno else 1
	        for i in xrange(int(molt)):
	            ret += segno * randint(1,dado) #randint dà anche gli estremi come possibili risultati
	    return ret        
	
	print tira_dadi(re.findall(r'([+-])?\s*(\d+)\s*(?:d\s*(\d+))?', "1 d6 + 1-1d4", re.I))

Adesso possiamo anche sbizzarrirci a fare grafici di curva gaussiane lanciando miriadi di dadi ^_^



