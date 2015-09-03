title: Hyperlink su tutte le email di un documento
lang: it
tags: javascript
Category: Javascript
Date: 2010/11/23 08:52

	:::js
	document.body.innerHTML=document.body.innerHTML.replace(/([a-zA-Z0-9_.-]+@[a-zA-Z0-9-.]+\.[a-zA-Z0-9]{2,4})/gi, '<a href="mailto:$1">$1</a>');

Con questo codice si sostituisce ogni mail trovata nel documento con un link cliccabile ad essa. Si potrebbe raffinare la regular expression per il match di email che non abbiano già un hyperlink intorno ad esse.