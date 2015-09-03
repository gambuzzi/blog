title: Hyperlink a Google maps su tutte gli indirizzi (stradali) di un documento
lang: it
tags: javascript
Category: Javascript
Date: 2010/11/23 01:45

Il codice è simile a quello che metter l'hyperlink alle mail, sempre da eseguire preferibilmente nell'evento OnLoad del BODY.

	:::js	
	document.body.innerHTML=document.body.innerHTML.replace(
		/((Via|viale|piazza|largo)[^+]*?\d+[^+]*?-[^+]*?\d{5}[^+]*?(Modena|Parma))/gi, 
		'<a href="http://maps.google.it/maps?f=q&source=s_q&hl=it&geocode=&q=$1&ie=UTF8&hnear=$1&z=16&iwloc=A" target="_blank">$1</a>'
	);

si aspetta una via ( o viale o piazza o largo o ... ) a modena o parma (altre località come vedete facilemente aggiungibili) nella forma:

	Via ... 17 - 41122 MODENA

Si aspetta quindi un cap di 5 cifre

Se non si volesse il link su alcuni indirizzi basta non metter il - (meno) fra numero e cap, ma una virgola.