title: Parser di espressioni aritmetiche
lang: it
tags: python
Category: Python
Date: 2012-07-12

Che bisogno c'è di scrivere un parse per qualcosa che può essere valutata più efficientemente da un `eval`? Direi nessuna, ma questo esercizio è stato il preludio (2005) ad un parser più complicato che pubblicherò in futuro.

Data una stringa

	:::python
	"((1+2)*4+1)*6/(2+1)"

Le regex non ci possono venire in aiuto più di tanto per la mancanza di un sistema di bilanciamento dei match multipli. Alcuni altri motori regex (credo quello del C#) hanno questa funzione, ma (almeno nel 2005) python non lo ha.

L'idea è quella di elaborare le parentesi più interne e poi sostituirne il valore (togliendo quindi le parentesi), procedendo così fino a non avere più parentesi. Alla fine si valuta l'espressione risultante.

Per processare prima le espressioni più interne si parte cercando la prima parentesi chiusa, con un `stringa.find(')')`, poi da questo punto si cerca la parentesi aperta più a destra nella stringa con un `stringa.rfind('(',0,posizione_parentesi_chiusa)`

Una altra cosa da fare è valutare la precedenza degli operatori, per rendere vere le asserzioni:
	
	:::python
	assert splitta('1+2*3')==['+', '1', ['*', '2', '3']]
	assert splitta('1+2+3+4*4')==['+', '1', '2', '3',['*', '4', '4']]

Partiamo da qui. Dividiamo la stringa con lo split delle stringhe python.

	:::python
	>>> stringa.split('+')
	['1', '2*3']

per ogni elemento della lista applico lo split per `'-'`, poi per `'*'` e per `'/'`. Abbiamo di fatto implementato la precedenza degli operatori. Dobbiamo però segnarci quale operatore ha dato origine allo split. Quindi la funzione risultante è:

	:::python
	def splitta(s):
	    if type(s) == list:
	        for k in xrange(1,len(s)):
	            s[k] = splitta(s[k])
	        return s
	    elif type(s) == str:
	        for op in '+-/*':
	            t = s.split(op)
	            if len(t)>1:
	                t[0:0] = op
	                return splitta (t)
	        return s
	

La funzione fa uso della ricorsione per splittare gli elementi successivi, e pone l'operatore in testa alla lista che si ottiene dallo split.

Per ottenere un valore numerico da questa lista si deve quindi partire dalle liste più interne. 

Vediamo ora come fare una funzione che ci dia un risultato.

	:::python	
	assert parse(['+', '1', ['*', '2', '3']]) == '7.0'

commentiamo la funzione.
	
	:::python
	def parse (lista):
	    case = {
	        '+':lambda x,y: float(x)+float(y),
	        '-':lambda x,y: float(x)-float(y),
	        '*':lambda x,y: float(x)*float(y),
	        '/':lambda x,y: float(x)/float(y),
	        }
	    #se non ho una lista restituisco il valore
	    if type(lista)==list:
	        #controllo che non ci siano sottoliste
	        term = True
	        for t in lista:
	            if type(t) != str:
	                term = False
	                break
	        if term: #nessuna sottolista
	            return str ( reduce ( case[lista[0]], lista[1:] ) )
	        else: #ci sono sottoliste, ne sostituisco i valori e mi richiamo
	            for i in xrange(len(lista)):
	                lista[i] = parse ( lista[i] )
	            return parse ( lista )
	    else: #l'input non era una lista, lo restituisco dritto.
	        return lista

Spieghiamo più nel dettaglio la riga 
	
	:::python
	return str ( reduce ( case[lista[0]], lista[1:] ) )

Python non ha costrutto switch-case. Le tecniche di programmazione ad oggetti più estreme dicono di non usare più questo costrutto, ma di creare una factory di oggetti che implementano una interfaccia comune, che variano nel comportamento come cambierebbero i vari rami dello switch-case. Estremizzano questo discorso anche all'uso degli else.

Qui più semplicemente uso il dizionario case, per avere una funzione per ogni operatore. Le stringhe vengono considerate convertite in float.

Quindi:

- `lista[0]` è l'operatore
- `case[lista[0]]` è una funzione che il reduce chiamerà
- `lista[1:]` è l'insieme dei valori su cui operare
- `reduce` chiama la funzione su tutta la lista, una coppia alla volta.
- `str` mi serve per potere poi rimettere il valore nella stringa partenza, se la lista che sto processando veniva da un blocco fra parentesi tonde.

Mettiamo ora insieme le due funzioni per elaborare espressioni con le parentesi.

	:::python
	def esegui(espressione):
	    #mentre ho ancora parentesi nella stringa  espressione 
	    while espressione.find(')')>-1:
	        _end = espressione.find(')')
	        _begin = espressione.rfind('(',0,_end)
	        #sostituisco il blocco di parentesi col suo valore
	        espressione = espressione[:_begin] + esegui (espressione[_begin+1:_end]) + espressione[_end+1:]
	    #qui non avrò parentesi
	    ops = splitta(espressione)
	    return parse(ops)

Ammetto che bastava un `eval` per tutto questo, ma come dicevo prima, questo esercizio aiuta a pensare a come si possono parsare espressioni, senza usare librerie di parsing python che richiedono l'uso pesante di regex, perché ricordiamoci:

> "Quando hai un problema ed usi una regex per risolverlo... ti troverai con 2 problemi"

E se volessimo avere dei numeri negativi? es: `-1*3`

