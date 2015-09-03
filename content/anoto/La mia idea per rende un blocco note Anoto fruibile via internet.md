title: La mia idea per rende un blocco note Anoto fruibile via internet
tags: python, anoto digital paper
lang: it
Category: Anoto Digital Paper
Date: 2012-11-9

La mia idea per rende il blocco note fruibile via internet sarebbe la seguente, se l’unico dato dinamico del blocco fosse l’indirizzo a cui andare a vederlo.

Calcolare l’indirizzo dal numero di pagina anoto (dato già univoco).

Ad esempio se l’url di base è `http://vostroserver/blocconote/<codicefoglio>`

Il `<codicefoglio>` può essere una qualsiasi sequenza alfanumerica.

L’indirizzo anoto è di 40 bit

`0.169.12.23.234`

`3 bit + 12 bit + 12bit + 5bit +8bit = 40bit`

Possiamo usare 32 simboli su 8 posizioni, dato che 32 simboli sono 5 bit, 5x8 = 40bit. Con 64 simboli sarebbero quindi 6bit*7caratteri = 42 bit, quindi stiamo nei 40bit

L’indirizzo `0.169.12.23.234` diventa quindi

	0 = 000
	169 = 000010101001
	12 = 000000001100
	23 = 10111
	234 = 11101010

- In totale 0000000101010010000000011001011111101010
- Come intero 5’670’803’434

In binario, troppo lungo e difficile da scrivere e correggere se si sbaglia.

Con 32 simboli abbiamo 8 caratteri necessari, facili da scrivere e correggere.

	AFJADF5K

Con 64 diventa
    
	AFSAZfq

Che pero’ è meno facile da scrivere perché mischia maiuscolo e minuscolo, dando come unico vantaggio l’avere 7 caratteri invece di 8.

I file Postscript verrebbero creati in BATCHProcess e il codice aggiunto da un programma python che gira successivamente sui file PS.

In ricezione della pagina e creazione della immagine non è necessario rimettere tale codice a mio avviso, ma si può fare. Il nome dell’immagine può rimanere quello standard di anoto, che contiene l’indirizzo, e questo necessita che la pagina `php` di visualizzazione faccia i conti al contrario rispetto alla codifica, oppure posso salvare l’immagine con il nome calcolato. (nel primo caso non serve postprocesso dell’immagine ricevuta, nel secondo si)

Dato che così si verrebbero a creare dei codici consecutivi (AFJADF5K sarebbe seguito da AFJADF5L) per evitare che si possano indovinare cosi facilmente i codici di pagina si può inserire in coda alla stringa una specie di codice di controllo calcolato in un qualche modo. Ad esempio AFJADF5K diverrebbe AFJADF5KJ e AFJADF5L diverrebbe AFJADF5LO. Abbiamo aggiunto 1 carattere e un po’ di sicurezza. Ovviamente un attacco in brute-force che le provi tutte riuscirebbe ad avere  la meglio su questa piccola protezione.

Per avere una sicurezza maggiore si dovrebbe allungare il codice diluendo quindi i risultati validi e impostando un IP-ban temporaneo se vengono fatte troppe richieste errate di fila.
Per aumentare ulteriormente la sicurezza si potrebbe associare una password casuale ad ogni blocco note, scrivendola sulla copertina.

Nel DB del web server si salva gamma-di-indirizzi e la password

| ADDR | PASSWD |
|------|--------|
| 0.169.12.23.* | xxxxxxxxxx |

Il web server prima di visualizzare la pagina chiede la password e la salva da qualche parte(così se uno controlla più pagine dello stesso blocco note non lo molesta chiedendo la password ogni foglio)

In alternativa si potrebbe (per non avere sempre blocchi da 256 pagine):

| DA | A | PASSWD |
|----|---|--------|
| AFJADFYA | AFJADF55 | xxxxxxxxxx |

I codici sopra riportati sono stati creati così

	:::python
	import string
	
	def int2bin(n, count=24):
	    return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])
	
	def code(n,cifre,ncifre = -1):
	    lc = len(cifre)
	    ret = ''
	    while n>0 if ncifre<0 else ncifre>0:
	        ret= cifre[n % lc]+ret
	        n = int(n/lc)
	        ncifre -= 1
	    return ret
	
	def crc(s, cifre):
	    ret = 0
	    for i in s:
	        ret <<= 1
	        ret ^= ord(i)
	    return cifre[ret % len(cifre)]
	   
	bits = (8,5,12,12,3)
	indirizzo = '0.169.12.23.234'.split('.')[::-1]
	
	n = 0
	for i, c in enumerate(indirizzo):
	    n += ((int(c) & (2**bits[i]))<<sum(bits[:i]))
	   
	print n    
	print int2bin(n,40)
	
	cod = code(n, string.ascii_uppercase + string.digits[:6], 8)
	print cod
	print code(n, string.ascii_uppercase + string.ascii_lowercase + string.digits + '+/', 7)
	print crc( cod, string.ascii_uppercase + string.digits[:6])
