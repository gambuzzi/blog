title: Creare una array con tutte le immagini di una cartella
lang: it
tags: javascript
Category: Javascript
Date: 2010/11/22 02:05

Per fare cio' dobbiamo avere la cartella che contiene le immagini listabile.

Suppioniamo di avere una variabile Array globale chiamate `array_immagini`

	:::js
	function loadImages() {
	    var reimg = /href\=\"(.+?\.(?:jpg|gif|png))\"/gi
	    xmlhttp.open("GET", fld+"?C=N;O=A",true);
	    xmlhttp.onreadystatechange=function() {
	        if (xmlhttp.readyState==4) {            
	            var arr = Array('a','b');
	            while (arr) {
	                var arr = reimg.exec(xmlhttp.responseText);
	                if (arr) {
	                    array_immagini.push(fld+'/'+arr[1]);
	                }    
	            }
	            loadedImg();
	        }
	    }
	    xmlhttp.send(null);
	}

"**C=N;O=A**" ci dà l'elenco in ordine ascendente di nome.

per avere l'oggetto `xmlhttp`

	:::js
	var xmlhttp;
	/*@cc_on @*/
	/*@if (@_jscript_version >= 5)
	  try {
	  xmlhttp=new ActiveXObject("Msxml2.XMLHTTP");
	 } catch (e) {
	  try {
	    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
	  } catch (E) {
	   xmlhttp=false;
	  }
	 }
	@else
	 xmlhttp=false
	 @end @*/
	if (!xmlhttp && typeof XMLHttpRequest!='undefined') {
	    try {
	        xmlhttp = new XMLHttpRequest();
	    } catch (e) {
	        xmlhttp=false;
	    }
	}
	if (!xmlhttp && window.createRequest) {
	    try {
	        xmlhttp = window.createRequest();
	    } catch (e) {
	        xmlhttp=false;
	    }
	}

**Nota** bene che quello in testa non è un commento eliminabile ma di una direttiva di compilazione condizionata ed è quindi da lasciare.

