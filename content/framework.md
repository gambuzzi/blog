title: La scelta di un framework di sviluppo
lang: it
tags: mix, framework
Category: Mix
Date: 2014-09-22

Introduzione: quando reinventare la ruota?
---------------------------------------------
Parlare di confronto fra Framework è un po’ come comparare diversi kit per trovare gli strumenti perfetti per edificare una casa. Verrebbe da dire che questi siano mattoni, cemento e cazzuola, ma questo “kit” non va bene per tutte le case. Pensiamo ad esempio agli strumenti che servono per una casa in legno.

Il tema dei Framework si riaggancia a quello, non nuovo in campo informatico, del riutilizzo del codice. “Non reinventiamo la ruota” ovvero usiamo codice già scritto, provato, testato, debuggato, ottimizzato.

Ma se non avessimo mai reinventato la ruota useremmo ancora le ruote in legno dei romani. Reinventare la ruota è una cosa che gli ingegneri del campo automotive fanno in continuazione; le ruote di una Ferrari sono, letteralmente, continuamente reinventate e migliorate.

Questo non vuole però dire che usare la ruota migliore sul mercato sia la cosa giusta per il nostro progetto. Se stiamo progettando un carrello della spesa la ruota di una Ferrari, per quanto sia una delle migliori ruote del mondo, non andrà bene. Serve una ruota adatta allo scopo.

Allo stesso modo un Framework può andare benissimo per uno scopo, ma essere inutile o dannoso per un altro.

Quando si usa un Framework si incappa sempre in quella che viene chiamata “complessità accidentale” o “debito tecnologico”, ovvero nell’utilizzo di uno strumento per velocizzare il lavoro, che richiede comunque tempo per apprendere lo strumento stesso.

Se invece di andare a piedi guidiamo un’automobile arriviamo più velocemente al lavoro, ma dobbiamo imparare a guidarla, dobbiamo rifornirla, mantenerla, pagare bolli, assicurazioni… se poi lavoriamo a 100 metri da casa, il discorso perde di utilità. Allo stesso modo l’uso di un framework può rallentare lo sviluppo anziché velocizzarlo.

Quando usare un framework e quando non usarlo
---------------------------------------------
Quando è utile usare un Framework? All’interno di progetti che necessitano di sicurezza sui login, l’uso di un Framework o di parti di esso (framework come symfony2 sono modulari e si può usare anche solo il componente di sicurezza), sono raccomandati per non incappare in errori comuni. Trovata una vulnerabilità del componente usato, si è però attaccabili. Non tutti i framework sono perfetti.

Per progetti molto piccoli un framework può essere controproducente: costi di apprendimento e di utilizzo possono cioè superare di gran lunga il tempo di creazione del nostro servizio partendo dal nulla. Per progetti molto grandi un framework può dare un forte sprint iniziale per poi rivelarsi una palla al piede arrivati al punto di dovere sviluppare funzionalità molto particolari o complesse. Non è bello dover dire al cliente: “Scusi non si può fare perché il framework che abbiamo usato non supporta questa modalità di scambio dati”.

Al cliente non importa, o non dovrebbe importare, la tecnologia usata per avere il prodotto richiesto. Se voglio una casa, descrivo la casa, non dico che strumenti usare per farla o come usarli. Mi affido a professionisti il cui lavoro è fare case.

Per progetti di medio respiro i framework sono una grande risorsa.

Mi sento di dare un consiglio: reinventate la ruota e non usate framework per quello che è il vostro core-business. Se state ad esempio fornendo un servizio di invio newsletter via e-mail, usate pure un framework per tutto quello che riguarda ad esempio gestione utenti e pannello di amministrazione. Scrivete però ex novo il vostro sistema di coda delle mail e il motore di template, che sarà il vostro punto forte, quello su cui dovete eccellere. Usando qualcosa di fornito da un framework sarete nella mediocrità e il vostro business rischierà di non svilpparsi al meglio.

Come scegliere il framework
---------------------------------------------
Quale framework è consigliabile usare per il proprio progetto?

Parlare di NET MVC rispetto a Django, PHP o Ruby on Rails per arrivare a stabilire the best of senza avere un’idea del terreno di confronto rischia di originare una risposta non obiettiva.

Ognuno di questi ha proprie peculiarità, che lo avvicinano o allontanano dalle necessità con una serie di aspetti correlati al progetto da realizzare. Giocano a favore di una soluzione piuttosto che di un’altra diverse componenti, a cominciare dal target, dalla tipologia di applicazione da sviluppare e alla piattaforma utilizzata, senza dimenticare la filosofia di programmazione (open source oppure no).

I concetti comuni di questi Framework sono nell’aria. Symfony2 e ZendFramework2 stanno convergendo perché concetti come testabilità, inversion of control e dependency injection, sono ormai buone pratiche da utilizzare e che ogni programmatore dovrebbe conoscere.

Scendendo in dettagli più consoni allo sviluppo, ci sono alcuni parametri che aiutano nel processo di scelta, che sono la qualità e la disponibilità di librerie e strumenti quali ambienti di sviluppo e debugger, oltre alle dimensioni e affidabilità della community legata a quel framework. Altro punto che può fare scegliere un framework piuttosto dell’altro è la disponibilità di sviluppatori per quel framework e linguaggio, legato anche alla realtà del paese in cui ci si trova. In Italia è più  facile trovare un programmatore PHP piuttosto che uno Ruby.

Aspetti di budget
---------------------------------------------
Più marginale, ma comunque degna di nota è la voce budget. I costi dello sviluppo sono

diversi a seconda della tecnologia, ma non sempre chi più spende, meno spende e viceversa. In questo specifico caso, soluzioni come PHP appaiono favorite per il bilanciamento complessivo dei vari aspetti in gioco, specialmente per quanto riguarda progetti di dimensioni medio-piccole, dove ad esempio i costi legate alle licenze per il DB possono risultare troppo onerose, mentre su applicazioni di più ampia scala è preferibile la soluzione di Microsoft, grazie al supporto che l’azienda offre ed alla superiore qualità, ma a questo punto, su un progetto grosso e con budget, ha ancora senso usare un framework? Dipende dal progetto. Sono decisioni che purtroppo vanno anticipate e quando si anticipa una decisione non basta tutta la analisi del mondo per essere sicuri che si sia fatta la scelta corretta.

Diffidate dalle soluzioni "all inclusive"
---------------------------------------------
Diffidate dai framework che vi promettono di essere ottimizzati per qualunque esigenza: Ottimizzato per tutto è uguale a ottimizzato per nulla. Prendiamo ad esempio le array PHP: sono comode, ma quando dichiarano di essere ottimizzate per contenere qualunque tipo di dato stanno dicendo solo che memorizzare una array di due interi usa 1kB di ram. Come l’XML; può rappresentare qualunque documento, ma nessuno in modo efficiente.

Non usate framework che vi sembrano troppo complessi o che non sono alla portata dei vostri sviluppatori. Non siamo tutti uguali e percepiamo la complessità in maniera differente, ma se per apprendere un framework servono più di 6 mesi c’è un problema di base. I concetti e le buone pratiche informatiche si rinnovano in continuazione, un framework si rinnova in media ogni 2 anni. Non possiamo passare il tempo a correre dietro al framework e a riapprenderlo in continuazione. Come sviluppatori si è pagati per risolvere problemi, non per conoscere framework.

Conclusione
---------------------------------------------
Tirando le somme, proprio in virtù del fatto che nessun framework può fregiarsi del titolo di “migliore in assoluto”, nel corso dello sviluppo del vostro progetto, specie se complesso, potreste anche arrivare alla conclusione che sia necessario realizzare la persistenza di dati in Java, il front-end in PHP e la business logic in tecnologia Microsoft. Non abbiate paura durante il progetto di tornare indietro anche su una decisione di piattaforma o framework, potrebbe farvi risparmiare giorni di lavoro in futuro. In ogni caso finito il progetto, guardatevi indietro e rispondete a una domanda: “Quanta percentuale del framework che ho scelto, ho effettivamente usato?”
