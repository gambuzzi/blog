title: Test Driven Development - Rischi
lang: it
tags: mix, tdd, agile
Category: Mix
Date: 2012-09-20


I rischi di un approccio troppo entusiastico al TDD ci sono e sono vari. Alcuni buoni principi da usare sono:


- Mai testare le cose semplici, se sono veramente semplici non si romperanno. Il concetto di semplice si sposta in base all'esperienza del programmatore. Questo è utile per fare maturare tutti. Il TDD cerca di mettere Junior e Senior tutti sullo stesso livello, sbagliando.
- Affidare interamente il design del proprio applicativo al TDD rischia di generare architetture fallimentari, se i test sono troppo invasivi. Avendo programmatori esperti si può fare un buon design senza bisogno del TDD. C'era una volta una ditta che ava benefit in denaro ai programmatori che coprivano più dell'80% del proprio codice con test. Questo generò un proliferare di microfunzioni sparse in mille classsi, che rese l'architettura insostenibile per le macchine stesse; questa pratica fu poi abbandonata ed il codice riscritto da zero con una perdita incalcolabile.
- Se vedete che state perdendo tempo per scrivere un test e questo tempo diventa di più di quello che avete impiegato per il codice stesso, non testatelo, il debug costerà meno del test.
- Se dovete fare modifiche alla architettura sistemistica per rendere testabile il codice, state sbagliando.
- Aggiungere layer di astrazione non risolve i problemi.
- Le persone vanno messe prima delle metodologie, questo lo dice anche il manifesto **AGILE**. Se una persona è brillante, l'essere chiusa e inquadrata in una metodologia, che va bene per una scimmia con problemi di apprendimento, porta ad un malcontento, rischiando di sprecare la risorsa che avete fatto tanto fatica a trovare e formare.
- Un cliente capisce difficilmente perché sarete più lenti di un vostro competitor nel fornire un software, a meno che voi non siate bravissimi a spiegargli che così facendo risparmieranno soldi nel futuro (meno bug e manutenzioni più veloci). *"So from a business standpoint, test driven development sucks as a selling tool."*
- Fate pagare il bugfix da contratto? Se lo fate pagare il TDD non è per voi (e forse nemmeno i test in generale).

I test sono utilissimi, ma il testare prima è sopravvalutato e abusato. Speriamo che questa moda passi.


