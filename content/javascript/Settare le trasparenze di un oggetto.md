title: Settare le trasparenze di un oggetto
lang: it
tags: javascript
Category: Javascript
Date: 2010/11/22 01:58

Questo è incredibilmente supportato anche da IE6.

`b` contiene la trasparenza nella scala 0->100

Il seguente metodo conviene se si vogliono settare anche altri paramentri di stile nel contempo

	:::js
	text = " filter: alpha(opacity="+b+"); opacity: "+(b/100.0)+"; -ms-filter: 'alpha(opacity="+b+")';";
	element.setAttribute("style", text);
	element.style.cssText = text;

Questo altro opera sulle singole proprietà

	:::js
	element.style.opacity = b/100.0;
	element.style.MozOpacity = b/100.0;
	element.style.filter = "filter: alpha(opacity="+b+")";
