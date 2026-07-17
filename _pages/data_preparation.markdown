---
layout: default
title: "Data Preparation"
subtitle: "Come sono stati costruiti i dataset di analisi"
---

{% include page-hero.html %}

Tutte le analisi del progetto **"Non solo Giochi"** si basano su un dataset comune che unisce i medaglieri delle Olimpiadi estive con gli indicatori socio-economici dei paesi partecipanti. In questa pagina descriviamo come questo dataset è stato costruito: le fonti utilizzate, i passaggi di pulizia e arricchimento e gli output prodotti.

## Fonti dati

Il dataset di analisi nasce dall'integrazione di due famiglie di fonti:

- **Dati olimpici** :
  - `Olympic_Medal_Tally_History_definitivo.csv`: il medagliere per paese e per edizione (ori, argenti, bronzi, totale);
  - `Olympic_Games_Summary.csv`: le informazioni su ogni edizione dei Giochi (anno, paese e città ospitante).
- **Indicatori socio-economici** — le serie storiche della [World Bank (Data360)](https://data360.worldbank.org/en/search), scaricate tramite chiamate API (utilizzando la libreria Python `wbgapi`): PIL, PIL pro capite, popolazione, urbanizzazione, aspettativa di vita, istruzione, spesa militare, indicatori di governance e molti altri.

La lista degli indicatori è stata costruita in modo collaborativo: utilizzando la libreria `wbgapi` è stato creato un file excel con tutti gli indicatori disponibili, nei vari database disponibili su WorldBank. Ogni partecipante al gruppo ha quindi esplorato e proposto un insieme di indicatori coerente con la propria analisi (istruzione, salute, macroeconomia, governance, demografia). Le liste sono state poi unite e deduplicate in un unico catalogo (una sessantina di serie World Bank). Avendo riscontrato una forte presenza di valori nulli, molti indicatori sono stati scartati dal stataset finale

## Download degli indicatori

Abbiamo creato diversi script per interagire con i database di WorldBank

Uno script che occupa di scaricare le serie storiche dalla World Bank:

1. **Selezione dei paesi**: si parte dalla lista dei codici ISO dei paesi e si verifica quali codici esistono effettivamente nella nomenclatura World Bank. I codici validi vengono salvati in cache per evitare di ripetere il controllo a ogni esecuzione.
2. **Download per paese**: per ciascun paese vengono scaricate tutte serie del catalogo per il periodo **1960–2019**, e salvate in un file CSV per paese:  oltre 200 file con una riga per anno e una colonna per indicatore.
3. **Robustezza**: l'API World Bank ha limiti e chiusure di connessione impreviste, quindi lo script introduce ritardi casuali tra le richieste, gestisce gli errori di rete con tentativi ripetuti e, in caso di interruzione, riprende dal primo paese non ancora salvato su disco.

## Pulizia dei dati

IUn secondo script si occupa di validare, aggregare e normalizzare i dati :

- **Validazione degli input**: ogni file CSV viene controllato per la presenza delle colonne obbligatorie (edizione, anno, paese, medaglie), con errori espliciti se manca qualcosa.
- **Normalizzazione**: i codici paese (NOC) e le edizioni vengono normalizzati (spazi, formati) per permettere il matching tra le diverse fonti; gli anni delle serie World Bank (formato `YR1964`) vengono convertiti in interi; tutti i valori degli indicatori vengono forzati a numerici. 


## Costruzione del dataset finale

Il cuore della preparazione dati è l'unione tra medagliere e indicatori. Per ogni riga *paese × edizione olimpica*:

1. si recuperano **paese e città ospitante** dell'edizione (colonne `paese_olimpiade` e `citta_olimpiade`);
2. si associano gli indicatori socio-economici del paese calcolando, per ciascun indicatore, la **media dei 4 anni precedenti** l'edizione (parametro configurabile). Questa scelta riflette l'idea che il successo olimpico dipenda dalle condizioni del paese nel ciclo olimpico che precede i Giochi, e attenua l'effetto di valori mancanti in singoli anni;
3. per ogni edizione vengono inoltre aggiunte **righe a zero medaglie** per tutti i paesi che non compaiono nel medagliere di quell'edizione: in questo modo il dataset non contiene solo i vincitori, e le analisi (regressioni, classificazioni) possono confrontare paesi che vincono e paesi che non vincono.

## Variabili principali

Il dataset finale contiene circa 6.700 righe (una per paese × edizione estiva, dal 1964 al 2020) e una quarantina di colonne:

- **Identificazione**: `edition`, `year`, `country`, `country_noc`;
- **Medagliere**: `gold`, `silver`, `bronze`, `total`;
- **Contesto dell'edizione**: `paese_olimpiade`, `citta_olimpiade`;
- **Indicatori socio-economici** (media dei 4 anni pre-olimpici), tra cui: PIL corrente e pro capite (`NY.GDP.MKTP.CD`, `NY.GDP.PCAP.CD`), crescita del PIL, popolazione totale e in età lavorativa (`SP.POP.TOTL`, `SP.POP.1564.TO.ZS`), urbanizzazione (`SP.URB.TOTL.IN.ZS`), aspettativa di vita (`SP.DYN.LE00.IN`), mortalità infantile, iscrizione scolastica, spesa militare, inflazione e superficie del paese.

## Output prodotti

La pipeline produce un dataset in fomrato CSV, usato come base ion diversi notebook del progetto:


## Note metodologiche

- **Finestra temporale pre-olimpica**: gli indicatori sono aggregati sui 4 anni precedenti ciascuna edizione. Il valore è un parametro dello script e può essere modificato per analisi di sensibilità.
- **Valori mancanti**: la media è calcolata sui soli anni disponibili nella finestra (`skipna`); se nessun anno è disponibile la cella resta vuota. Nessun valore viene imputato in questa fase: le scelte di imputazione sono lasciate alle singole analisi.
- **Paesi non riconosciuti**: alcuni codici ISO non esistono nella nomenclatura World Bank (per esempio comitati olimpici storici o territori particolari); Per questi casi si è proveduto a adeguare e rilanciare manualmente gli script.
