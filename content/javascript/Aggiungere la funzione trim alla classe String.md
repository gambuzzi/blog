title: Aggiungere la funzione trim alla classe String
lang: it
tags: javascript
Category: Javascript
Date: 2012/01/16 05:24

	:::js
	String.prototype.trim = function () {
	    return this.replace(/^\s*/, "").replace(/\s*$/, "");
	}

è stato preferito fare così, piuttosto che

	:::js
	String.prototype.trim = function () {
	    return this.replace(/^\s*|\s*$/, "");
	}

per motivi di performance.

