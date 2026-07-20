---
layout: default
title: "Non solo Giochi"
subtitle: "I fattori socio-economici dietro il successo olimpico"
---

{% include page-hero.html %}

**Il medagliere olimpico non racconta solo lo sport.** Ogni quattro anni diventa una classifica tra nazioni. Ma cosa c'è dietro quella classifica? Perché alcuni paesi vincono sistematicamente più di altri, anche a parità di popolazione? E quanto contano ricchezza, istruzione, salute e investimenti pubblici nel produrre campioni?

**"Non solo Giochi"** nasce da queste domande: è un progetto di analisi dati che mette in relazione i risultati delle **Olimpiadi estive dal 1964 al 2020** con gli **indicatori socio-economici** dei paesi partecipanti, per capire quali fattori strutturali accompagnano — e in parte spiegano — il successo sportivo.

## Le domande di ricerca

Il progetto ruota attorno ad alcune domande centrali:

- **Il PIL spiega le medaglie?** Quanto contano la ricchezza e la dimensione demografica di un paese nel determinare il suo medagliere?
- **Esistono "famiglie" di paesi olimpici?** È possibile raggruppare i paesi per profilo socio-economico e sportivo, e capire quali sport dominano in ciascun gruppo?
- **Alcuni sport sono più "democratici" di altri?** Quali discipline restano accessibili ai paesi con meno risorse e quali richiedono infrastrutture costose?
- **Il successo ha un genere?** Come è cresciuto il medagliere femminile e risponde agli stessi fattori di quello maschile?
- **Si può prevedere il futuro?** Con i dati storici e gli indicatori è possibile stimare i medaglieri delle prossime edizioni?

## I dati

La base comune di lavoro unisce due mondi:

- lo **storico dei risultati olimpici** (medaglieri, atleti, eventi e edizioni dal 1964 in poi);
- le **serie storiche della World Bank**: PIL, popolazione, urbanizzazione, aspettativa di vita, istruzione, spesa pubblica e molti altri indicatori, scelti in modo collaborativo dai componenti del gruppo.

Le due fonti sono state integrate in un unico dataset di analisi, in cui ogni riga rappresenta un paese in una specifica edizione olimpica, arricchito con la media degli indicatori nei quattro anni precedenti i Giochi. La costruzione del dataset è descritta in dettaglio nella pagina [Data Preparation]({{site.baseurl}}/data_preparation.html).

## Le analisi del gruppo

Il progetto è il lavoro collettivo del **Gruppo 6** del Master SoBigData. Ogni componente ha esplorato una prospettiva diversa sulla stessa domanda di fondo:

- **Alessia Niotta** ha classificato i paesi in fasce socio-economiche (dai "ricchi avanzati" ai paesi a basso reddito) e ha costruito, sport per sport, modelli di regressione logistica per stimare la probabilità di vincere una medaglia: ne emerge che alcuni sport (vela, scherma, equitazione) sono fortemente legati alla ricchezza, mentre altri (atletica, pugilato, sollevamento pesi) restano aperti al talento dei paesi con meno risorse.

- **Santina Capalbo** ha applicato tecniche di clustering su tre livelli — paesi, sport ed eventi — individuando gruppi di paesi con profili olimpici ben riconoscibili: dalla "potenza assoluta" (gli USA) alle potenze consolidate europee, dagli specialisti di poche discipline (come Kenya e Giamaica nell'atletica) ai giganti a partecipazione discontinua come URSS e Cina.

- **Gianni Coia** ha esplorato il dataset con tecniche di data mining, studiando come i cluster socio-economici dei paesi si riflettono negli sport in cui eccellono: i paesi ricchi dominano le discipline tecniche e costose, quelli emergenti gli sport basati sul talento individuale.

- **Giuseppe Pascuzzi** ha costruito modelli predittivi (dalla regressione ai Random Forest) per stimare i medaglieri, ha analizzato l'effetto causale degli investimenti nello sport d'élite — che risultano un predittore più forte del semplice PIL — e ha misurato il vantaggio del paese ospitante, arrivando a una previsione del medagliere di Los Angeles 2028.

- **Stefano Macchiavelli** ha curato la costruzione del dataset comune (medaglieri + indicatori World Bank) e ha analizzato il medagliere attraverso la lente del genere: la crescita del successo femminile dal 1964 a oggi e il confronto tra risultati maschili e femminili in relazione agli indicatori socio-economici ([leggi l'analisi]({{site.baseurl}}/successo_maschile_femminile3.html)).

- **Alessio Cioli** ha curato il download dei dati e ha aggiunto una prospettiva qualitativa, raccogliendo con tecniche di web scraping gli articoli della stampa italiana sulla scherma olimpica per analizzare come i media raccontano il successo sportivo.

- **Luisa Mancone** ha contribuito alla selezione degli indicatori legati a salute e benessere, una delle dimensioni chiave del dataset comune.

## Cosa abbiamo imparato

Le diverse analisi convergono su un messaggio comune: **il medagliere olimpico non è solo sport**. La ricchezza e la dimensione di un paese sono condizioni abilitanti — il PIL è il singolo indicatore più correlato con le medaglie — ma non bastano a spiegare tutto. Contano le scelte: dove investire, in quali discipline specializzarsi, quanto includere e valorizzare le atlete. È in questo spazio tra struttura e strategia che i Giochi diventano, appunto, *non solo giochi*.
