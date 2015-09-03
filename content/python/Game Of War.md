title: Game Of War
tags: python
lang: it
Category: Python
Date: 2011-10-17 06:15

Questo è il mio primo esperimento di programma con la libreria PyGame.

Non ha interazione con l'utente, è una simulazione di scontro su un campo aperto.

È un prototipo per una possibile evoluzione futura in un giochino di strategia.

Il sorgente è un po' lungo da commentare.

La cosa che più mi ha interessato sono le due classi *Marine* e *Ghost* che ereditano dalla classe *Pawn*, che di per sè non è nulla, ma che gestisce i movimenti ed il fuoco di base.

Il *Ghost* reimplementa la routine di fuoco, il *Marine* no.
Quando queste classi chiamano il costruttore della super-classe, passano anche loro stesse come parametro (*clazz*). 

Non ho trovato un modo più elegante di farlo. Funziona ma mi piace poco.

In testa a file dopo gli *import* ci sono varie costanti, fra qui *FPS* che può limitare il frame al secondo visualizzati e il numero di squadre e di classi per un tipo e per l'altro.

Divertitevi pure a giocare con questo sorgente e fatemi sapere le Vostre opinioni.

![ninjaidecontext]({filename}/images/gameofwar.png)

[allegato]({filename}/extras/GameOfWar.rar)
