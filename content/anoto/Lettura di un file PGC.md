title: Lettura di un file PGC
slug: lettura-di-un-file-pgc
tags: python, anoto digital paper
lang: it
Category: Anoto Digital Paper
Date: 2011-03-2 04:24

Qui allegato troverete un file che apre tutti i file PGC della cartella in cui si trova e stampa più informazioni possibili su di esso e sui tratti in esso contenuti.

Lo script usa 3 serivizi COM di Anoto

- AnotoUtil.File
- Anoto.ServiceAPI.PenRequest
- AnotoUtil.PenID

La struttura che legge i tratti dalla penna viene inizializzata dalla riga

    pr.Initialize(bin)

Dopodichè sono tutte chiamate all'oggetto PenRequest

[allegato]({filename}/extras/proveanotopenna.py)
