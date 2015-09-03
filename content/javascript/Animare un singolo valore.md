title: Animare un singolo valore
lang: it
tags: javascript
Category: Javascript
Date: 2010/11/22 01:49

Con questo script si puo animere un singolo valore di un oggetto preso per id. 

	:::js
	function animateSingleVal(cosa, a, unita, tempo, callback) {
	    if (cosa == null)
	        return;
	        
	    da = parseInt(eval(cosa));
	    if (isNaN(da))
	        da = 0;        
	    
	    if (tempo>40)
	    {        
	        newda = da + ((a-da) * 40 / tempo);  
	        eval(cosa+' = "'+parseInt(newda) + unita+'"');
	        cmd = 'animateSingleVal("'+cosa+'",'+a+",'"+unita+"',"+(tempo-40)+","+callback+");";
	        setTimeout(cmd,40);
	    }
	    else
	    {
	        eval(cosa+' = "'+parseInt(a) + unita+'"');
	        if(callback != null)
	            callback();
	    }
	}

l'utilizzo tipico è 

	:::js
	function imaOver(nome) {
	        animateSingleVal("document.getElementById('"+nome+"').style.width",160,"px",250);
	}

parametri:

- `cosa`: è il valore da modificare
- `a` : è il valore a cui arrivare con l'animazione
- `unita`: è il tipo di unita del valore da impostare
- `tempo`: è il tempo in millisecondi da impiegare per arrivarvi
- `callback`: è una funzione da chiamare ad animazione eseguita