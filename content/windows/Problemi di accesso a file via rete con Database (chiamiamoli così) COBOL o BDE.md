title: Problemi di accesso a file via rete con Database (chiamiamoli così) COBOL o BDE
lang: it
tags: windows, db
Category: Windows
Date:  07/09/2010 07:26

Il problema è altresì noto come *Opportunistic lock*.

E' un problema di accesso al file. Alcune tecniche impiegate per velocizzare questi accessi si rivelano controproduttive con tecniche di accesso ai file di vecchio stampo.

La soluzione sta nel disattivare questi '*miglioramenti*'. Per fare cio inserire nel registro la chiave allegata sia sui Cliente che sul Server dati.

[http://support.microsoft.com/kb/296264](http://support.microsoft.com/kb/296264)

[allegato]({filename}/extras/oplock.reg)
