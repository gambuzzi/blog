title: Decoratore con parametri procedurale
lang: it
tags: python
Category: Python
Date: 2012-04-21 12:03

Ecco uno stralcio di codice per decorare una funzione. Nello specifico questo decoratore si segna in un dizionario tutte le funzioni decorate con lo stesso parametro. E' stato il prototipo per il decoratore di **route** per un piccolo framework web che stavo sviluppando.

	from collections import defaultdict
	MODELS = defaultdict(list)
	
	def route(_route='.*'):
	    def wrap(f):
	        def wrapped_f(*argt, **argd):
	            return f(*argt, **argd)
	        MODELS[_route].append( wrapped_f )
	        return wrapped_f
	    return wrap
	
	@route('s')
	def gallerie():
	    return 1
	
	print MODELS, gallerie()

In pratica la funzione `route` restituisce la funzione decoratrice `wrap`, la quale a sua volta restituisce una funzione wrappata che non fa nulla se non chiamare la funzione originale. Nel frattempo si segna in un dizionario di liste le funzioni collegate a 's'.
Nella mia idea c'era l'intenzione di decorare tutte le funzioni con una regex da far matchare con l'url richiesta, con tanto di gruppi estratti con un `findall` e passati come parametro alla funzione decorata.