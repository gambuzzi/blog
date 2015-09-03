title: Schema in un db schemaless (come progettare le tabelle di MongoDB)
lang: it
tags: mix, mongodb, db
Category: Mix
Date: 2015-01-21

Nonostante il singolo record( o meglio *documento*) di MongoDB sia schemaless, per comodità applicativa ovviamente si dividono i documenti in collections, più o meno omogenee come tracciato. Il vantaggio dell'essere schemaless si ha quando si vuole aggiungere un campo che non si era previsto o quando si vuolo "embeddare" altri documenti o oggetti come array.

Come strutturare quindi il proprio domino di dati con MongoDB?

Due regole molto generali, ma che vi possono aiutare moltissimo sono:

* se state strutturando le tabelle come fareste su un db relazionale, state sbagliando.
* strutturate i dati in funzione di come li accederete dalla applicazione; esempio: se avete due collections `studenti` e `professori`, la relazione può essere sia dalla studente al professore, sia viceversa. Ha senso mettere il riferimento su una o sull'altra (o su tutte e due) in funzione di come l'applicazione cerca i dati. Se dalla scheda dello studente (in interfaccia) si deve saltare al professore e mai viceversa si metterà la relazione sullo studente.

Vediamo con ordine come _tradurre_ le relazioni che incontriamo in un tradizionale DB relazione in qualcosa di più adatto a MongoDB (e alla vostra applicazione):


Relazioni 1 a 1
---------------
In un db relazione questo tipo di relazione ha già poco senso, nel senso che basterebbe aggiungere colonne ad una tabella già esistente, anziché farne una altra in relazione 1a1.

In MongoDb gli unici due motivi per dividere in pratica un documento/record in 2 diverse collections possono essere:

* Il singolo documento supera i 16MB, limite del BSON usato da MongoDB;
* Parte del documento che si vuole accedere non serve con la stessa frequenza del resto e rischia di appesantire il recupero del documento dal db.
    * Esempio: abbiamo il catalogo di un ecommerce, che nel singolo documento, che rappresenta il singolo prodotto, contiene (in pdf) anche la pagina del catalogo cartaceo in cui compare e magari qualche software (come un driver). *Qui* conviene separare gli attributi del prodotto in 2 categorie; gli attributi (che si spera siano di piccole dimensioni) che servono in galleria prodotto, che saranno sempre caricati e potranno essere usati per gli ordinamenti, e gli attributi *extra*, che renderebbero lento il caricamento in galleria, ma che servono in visualizzazione della scheda dettagli del prodotto.

Anche qui la logica della vostra applicazione influisce sulla struttura dei dati.

A differenza di quanto ci hanno sempre insegnato coi DB relazionali, il db *NON* deve essere agnostico rispetto alla applicazione da implementare, nemmeno alla sua interfaccia. Se 2 diversi dati non vengono mai visualizzati nella stessa pagina/schermata, è inutile tenerli nello stesso documento o, addirittura, metterli in relazione.


Relazioni 1 a N
---------------

Anche qui dobbiamo ragionare in funzione di come i dati verranno visualizzati e aggiornati.
Ipotizziamo un articolo di un blog, commenti e tag.
Sui commenti dei singoli articoli, difficilmente faremo accessi singolarmente; non ci sarà una pagina con l'elenco di tutti i commenti.
I commenti verranno con buona probabilità visualizzati *solo* insieme all'articolo a cui sarebbero in relazione 1 a N. Inoltre difficilmente supereremo i 16MB fra articolo e commenti.

*Quindi* i commenti possono essere embeddati come sottodocumento nell'articolo

    :::js
    articolo = {
        _id : ObjectId("54bc49638379934d5de98d7d"),
        titolo : "Schema in un db schemaless (come progettare le tabelle di MongoDB)",
        corpo : "Nonostante il singolo record di MongoDB ...",
        commenti : [{
            autore: "Anonimo veneziano",
            email : "none@example.com",
            commento: "non sono concorde..."
          }, {
            autore: "Anonimo veneziano",
            email : "none@example.com",
            commento: "continuo a non essere concorde..."
          }],
        tags: ["mix", "mongodb", "db"]
    }

Vedremo poi come comportarci coi *tags* che sono in relazione "N a M"

Riassumendo si può precedere ad "embeddare" i documenti relazionati in "1 a N" quando:
* i documenti non superano 16MB (compreso documento principale).
* i documenti sono acceduti sempre assieme al documento principale.

Negli altri casi si procede, come faremmo con un normale db relazionale, a mettere l'object_id dell'articolo come valore del commento

    :::js
    commento = {
            _id: ObjectId("a4bc49a53279934d5de98231"),
            autore: "Anonimo veneziano",
            email : "none@example.com",
            commento: "non sono concorde..."
            articolo: ObjectId("54bc49638379934d5de98d7d")
          }


Relazioni "N a M"
-----------------

Le relazioni N a M, many-to-many, molti-a-molti, sono spesso delle relazioni pochi-a-pochi.

Prendiamo l'esempio classico della relazione fra libri e autori.

In questo classico esempio avremo libri scritti da pochi autori (di solito 1) e autori che scrivono (in media) pochi libri. Ci sono autori che scrivono molti libri, ma sono statisticamente una minoranza, rispetto a coloro che hanno scritto 1 o 2 libri.

Nel libro possiamo avere un campo per l'array degli autori; nell'autore possiamo avere un campo per l'array dei libri.

    :::js
    libro = {
      _id : 1,
      //....
      autori: [2,3]
    }

    autore = {
      _id: 2,
      //....
      libri: [1,6,19]
    }

Circa come si farebbe in un db relazionale, senza pero' una tabella aggiuntiva con le sole relazioni.

Nella gestione delle array (che spesso non saranno mai molto grosse) ci viene incontro MongoDB con tutta una serie di funzioni.

Inoltre questa struttura è ridondante, ancora una volta per venire incontro alle logiche di visualizzazione della app in sviluppo. Facilmente si vorrà saltare da un libro al suo autore e da un autore al suo elenco di libri.

Altro pro della struttura ridondante è una forma di controllo di errore. In MongoDB non ci sono `constraints`, quindi è l'applicazione a doversi preoccupare dell'integrità dei dati, non il DB.

Prendiamo una relazione fra articoli a catalogo e carrello, senza storicizzazione dell'articolo (che non andrebbe fatta a livello di carrello, ma solo alla conferma dell'ordine). Un carrello può avere più articoli e un articolo può essere in più carrelli (di diversi utenti). Sulla relazione in un relazionale classico, ci sarebbe la relazione come field aggiuntivo.

    :::bash
        +----------+        /\        +----------+
        |          |       /  \       |          |
        |          |  n   /    \   m  |          |
        | articoli |-----<  nm  >-----| carrelli |
        |          |      \    /      |          |
        |          |  qta--\  /       |          |
        +----------+        \/        +----------+

Qui avremo tipicamente un carrello con pochi articoli e gli articoli in molti carrelli (se il nostro ecommerce è un B2C e ha un buon successo).

Sempre tipicamente vorremo avere un elenco del contenuto del carrello e quasi mai un elenco dei carrelli che contengono un determinato prodotto (salvo per motivi statistici, ma per quelli non si fanno query sul db di produzione, ma su una replica statica, magari su una altro motore DB).

Quindi

    :::js
    carrello = {
        _id : ObjectId("54bc49638371231231e98d7d"),
        articoli : {
          "SW18-22" : 2,
          "JO350AA" : 3,
        },
        gran_totale: {'EUR': 1000.00}
    }

Avremo 2 articoli con codice `SW18-22` e 3 con codice `JO350AA`, con articoli del tipo:

    :::js
    articolo = {
        _id : ObjectId("231e98d7d54bc49638371231"),
        sku : "SW18-22",
        nome: { "it": "Sturalavandini", "en": "Plunger" },
        //....
    }

e magari un indice sullo `sku` dell'articolo.

Un altro dettaglio per un ecommerce potrebbe essere quello che il carrello attivo di un utente e sempre e solo 1, quindi il carrello non è linkato al customer (o viceversa), ma embeddato in esso.

    :::js
    cliente = {
        //....

        carrello :{
          articoli : {
            "SW18-22" : 2,
            "JO350AA" : 3,
          },
          gran_totale: {'EUR': 1000.00}
        }
    }


Il gran_totale è storicizzato nel carrello e ricalcolato ogni volta che serve, per velocizzare la visualizzazione (anche qui una scelta di _tracciato_ dettata da una esigenza di visualizzazione dell'applicazione)

Tornando ai tags degli articoli di un blog: salvare una array di `_id` che puntano ai tags ha il vantaggio che, se si vuole correggere un typo in un tag o rinominarlo, andremo ad aggiornare in un solo punto. Il principio di non replicare i dati nelle varie collections si applica anche a MongoDB, laddove ovviamente la replica non generi un vantaggio prestazionale tale da giustificare poi una procedura applicativa di sincronia dei dati fra le varie collections.

Silver Bullet
-------------

Non c'è quindi una soluzione magica per modellare le collections, ma come avete visto avere ben chiara in testa ogni parte della propria applicazione aiuta sempre. Un altro vantaggio di MongoDB è senza dubbio che al cambiare delle specifiche del cliente sull'applicazione, possiamo reagire più rapidamente al cambiamento di un DB relazionale (niente migration, salvo casi eccezionali, per intenderci).
