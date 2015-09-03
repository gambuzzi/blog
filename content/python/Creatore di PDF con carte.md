title: Creatore di PDF con carte
lang: it
tags: python
Category: Python
Date: 2011-10-17 06:09

Questo progetto nasce per stamparsi le carte di magic per poi ritagliarle.
Trovandosi a giocare fra amici non c'è la necessità di possedere realmente le carte, basta per convenzione avere i mazzi con queste 'copie ed uso personale'.
Altro scopo dei mazzi cosi fatti è non rovinare la propria collezione di carte.

![screenshot]({filename}/images/mazzomaker.png)

Il programma è molto semplice

Richiede le librerie:

- CherryPy
- ReportLab
- PIL (Python Image Library)

Il file config.py contiene il seguente codice

	origine_carte='carte/*.jpg' # percorsi separati da punto e virgola ';'
	matrice = (3,3)
	spaziatura = (0.05, 0.05)
	dimensione = (5.9,8.39)
	rotazione = 0.0
	carta = (21.0,29.7)

in questo file viene specificato dove prendere le carte (1° riga), quante metterne per pagina, distanziate quanto l'una dall'altra, con quale dimensione, se ruotarle (vedremo poi che era stata prevista questa funzionalità ma non è stata mai implementata) e la dimensione del foglio.

Tutte le dimensioni sono in Centimetri.

Passiamo ora al programma vero e proprio

	from reportlab.pdfgen.canvas import Canvas
	from reportlab.lib.units import cm
	from glob import glob
	from PIL import Image
	#from math import sin, cos
	import cherrypy
	from os.path import abspath
	import subprocess
	#from win32com.client import Dispatch
	from sys import argv
	import time
	from random import randint
	
	from config import *
	
	def crea(fs):
	    offset = [(carta[x]-spaziatura[x]*(matrice[x]-1)-matrice[x]*dimensione[x])/2 for x in xrange(2)] #centratura
	    pdf = Canvas('mazzo.pdf', pagesize=[x*cm for x in carta])
	    x = 0
	    y = 0
	    for f in fs:
	        for i in xrange(int(fs[f])):
	            pdf.drawImage(f, (offset[0]+x*(dimensione[0]+spaziatura[0]))*cm , \
	                (offset[1]+(matrice[1]-1-y)*(dimensione[1]+spaziatura[1]))*cm , dimensione[0]*cm , dimensione[1]*cm)
	            x += 1
	            x %= matrice[0]
	            if x==0:
	                y += 1
	                y %= matrice[1]
	            if x==0 and y==0:
	                pdf.showPage()
	    pdf.save()
	
	class MazzoMaker(object):
	    def __init__(self):
	#        IE = Dispatch("InternetExplorer.Application")
	#        IE.Visible = True
	#        IE.Navigate("http://localhost:8080/")
	#        subprocess.Popen(['CMD.EXE','/c',"ping 127.0.0.1 -n 2 & start http://localhost:8080/"])
	        pass
	                               
	    def redir(self):
	        yield "Please Wait..."
	        time.sleep(1)
	        raise cherrypy.HTTPRedirect('/')
	    redir.exposed = True
	        
	    def index(self):    
	        submit = '<p><input type=Submit value="Crea PDF"></p>'
	        ret =  ["<html><head><title>Mazzo Maker</title></head><body><h1>Mazzo Maker</h1>"]
	        ret.append('<form method=post action="creamazzo">')
	        ret.append(submit)
	        for f in glob('temp/*.jpg'):
	            ret.append('<img src="%s" width=200px>Quantita<input name="%s" type=Text lenght=2 value=0>' \
	                        % ( f.replace('\\','/'), f ) )
	        ret.append(submit)
	        ret.append('</form></body></html>')
	        return '\n'.join(ret)
	    index.exposed = True
	    
	    def creamazzo(self, *args, **key):
	        crea(key)
	        return cherrypy.lib.static.serve_file(abspath('mazzo.pdf'),"application/pdf", "attachment")
	    creamazzo.exposed = True
	
	porta = randint(8080,10000)
	
	cfg = """\
	[global]
	server.socket_port = %i
	server.thread_pool = 10
	tools.sessions.on = True
	tools.staticdir.root = "%s"
	
	[/temp]
	tools.staticdir.on = True
	tools.staticdir.dir = "temp"
	""" % (porta,argv[0][:argv[0].rfind('\\')].replace('\\','/'))
	
	open('config.cfg','w').write(cfg)
	
	for gf in origine_carte.split(';'):
	    for f in glob(gf):
	        fdest = 'temp\\' + f[f.replace('\\','/').rfind('/')+1:]
	        fdest = fdest[:fdest.rfind('.')] + '.jpg'
	        Image.open(f).rotate(rotazione, expand=1).save(fdest, quality=100)
	        
	subprocess.Popen(['CMD.EXE','/c',"start http://localhost:%i/redir" % porta])
	cherrypy.quickstart(MazzoMaker(),config='config.cfg')

La funzione *crea* prende una lista di carte (*fs*) e crea un file PDF sul disco.

L'inizializzazione del programma è molto grezza si compone di:

- scelta di una porta a caso del localhost, nessun check, si spera nella fortuna.
- scrittura del file di configurazione del cherrypy
- creazione delle immagini temporanee per la pagina html generata dall'index (vedremo dopo)
- lancia il broswer sul localhost...
- ...sperando che il cherrypy si avvii in tempo ^_^

La classe del cherrypy si compone fondamentalmente di una pagina *index* e di un metodo per il FORM HTML che viene POSTato con le quantità delle carte. Per grandi quantità di carte si è rivelato un po scomodo, ma se uno sa già quali carte servono e mette solo quelle va benissimo.

Un programma molto semplice, realizzato molto in fretta (una pausa pranzo) e che svolge la sua funzione egregiamente direi.

Chiunque abbia idee o migliorie è libero di dirmele e prendere questo codice come spunto per qualsiasi sua idea.

[allegato]({filename}/extras/cartemagic.rar)