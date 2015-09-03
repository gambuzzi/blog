title: Posizione in pixel di un oggetto
lang: it
tags: javascript
Category: Javascript
Date: 2010/11/22 01:45

	:::js
	function findPos(obj) {
	    var curleft = curtop = 0;
	    if (obj.offsetParent) {
	        do {
	            curleft += obj.offsetLeft;
	            curtop += obj.offsetTop;
	        } while (obj = obj.offsetParent); // l'=' non è un errore, serve ad aggiornare obj e testarlo in un unico colpo
	        return [curleft,curtop];
	    }
	}