title: Ridurre un disco dinamico Vdi di VirtualBox
lang: it
tags: mix, vdi, virtualbox
Category: Mix
Date: 2014-09-07

Si possono ridurre le immagini vdi dei dischi dinamici di VirtualBox. Questo è utile quando avete disintallato dei programmi o eliminato dei file di grosse dimensioni, dato che di suo il formato _vdi_ per dischi dinamici non cala mai di dimensione, anche alla cancellazione dei file che contiene. Si espande e basta.

Il processo è semplice.

1. installate sulla macchina **guest** `zerofree` o un programma equivalente per il vostro sistema operativo, questo articolo copre un sistema **guest** di tipo linux.
1. avviate in **recovery mode**, in modo da poter acceder come root a _/dev/sda1_
1. montate _/dev/sda1_ in sola lettura:   `(mount -o ro /dev/sda1 /mnt/tmp)`
1. lanciate "`zerofree /dev/sda1`"
1. spegnete la macchian virtuale
1. lanciate dalla macchina host: "`VBoxManage modifyhd –compact /path/to/virtualboximage.vdi`"

Link di approfondimento:

* [http://maketecheasier.com/shrink-your-virtualbox-vm/2009/04/06](http://maketecheasier.com/shrink-your-virtualbox-vm/2009/04/06)
* [http://www.virtualbox.org/manual/UserManual.html](UserManual)
*   [http://forums.virtualbox.org/viewtopic.php?p=29272#29272](http://forums.virtualbox.org/viewtopic.php?p=29272#29272)

