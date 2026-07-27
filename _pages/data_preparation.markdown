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
- **Indicatori socio-economici** — le serie storiche della [World Bank (Data360)](https://data360.worldbank.org/en/search), scaricate tramite chiamate API (utilizzando la libreria Python [wbgapi](https://pypi.org/project/wbgapi/)): PIL, PIL pro capite, popolazione, urbanizzazione, aspettativa di vita, istruzione, spesa militare, indicatori di governance e molti altri.

La lista degli indicatori è stata costruita in modo collaborativo: utilizzando la libreria `wbgapi` è stato creato un file excel con tutti gli indicatori disponibili, nei vari database disponibili su WorldBank. Ogni partecipante al gruppo ha quindi esplorato e proposto un insieme di indicatori coerente con la propria analisi (istruzione, salute, macroeconomia, governance, demografia). Le liste sono state poi unite e deduplicate in un unico catalogo (una sessantina di serie World Bank). Avendo riscontrato una forte presenza di valori nulli, molti indicatori sono stati scartati dal stataset finale

## Download degli indicatori

Abbiamo creato diversi script per interagire con i database di WorldBank

Uno script che occupa di scaricare le serie storiche dalla World Bank:

1. **Selezione dei paesi**: si parte dalla lista dei codici ISO dei paesi e si verifica quali codici esistono effettivamente nella nomenclatura World Bank. I codici validi vengono salvati in cache per evitare di ripetere il controllo a ogni esecuzione.
2. **Download per paese**: per ciascun paese vengono scaricate tutte le serie del catalogo per il periodo **1960–2020**, e salvate in un file CSV per paese:  oltre 200 file con una riga per anno e una colonna per indicatore.
3. **Robustezza**: l'API World Bank ha limiti e chiusure di connessione impreviste, quindi lo script introduce ritardi casuali tra le richieste, gestisce gli errori di rete con tentativi ripetuti e, in caso di interruzione, riprende dal primo paese non ancora salvato su disco.

## Pulizia dei dati

Un secondo script si occupa di validare, aggregare e normalizzare i dati :

- **Validazione degli input**: ogni file CSV viene controllato per la presenza delle colonne obbligatorie (edizione, anno, paese, medaglie), con errori espliciti se manca qualcosa.
- **Normalizzazione**: i codici paese (NOC) e le edizioni vengono normalizzati (spazi, formati) per permettere il matching tra le diverse fonti; gli anni delle serie World Bank (formato `YR1964`) vengono convertiti in interi; tutti i valori degli indicatori vengono forzati a numerici. 


## Costruzione del dataset finale

Il cuore della preparazione dati è l'unione tra medagliere e indicatori. Per ogni riga *paese × edizione olimpica*:

1. si recuperano **paese e città ospitante** dell'edizione (colonne `paese_olimpiade` e `citta_olimpiade`);
2. si associano gli indicatori socio-economici del paese calcolando, per ciascun indicatore, la **media dei 4 anni precedenti** l'edizione (parametro configurabile). Questa scelta riflette l'idea che il successo olimpico dipenda dalle condizioni del paese nel ciclo olimpico che precede i Giochi, e attenua l'effetto di valori mancanti in singoli anni;
3. per ogni edizione vengono inoltre aggiunte **righe a zero medaglie** per tutti i paesi che non compaiono nel medagliere di quell'edizione: in questo modo il dataset non contiene solo i vincitori, e le analisi (regressioni, classificazioni) possono confrontare paesi che vincono e paesi che non vincono.

## Variabili principali

Il dataset finale contiene 6.700 righe (una per paese × edizione estiva, dal 1964 al 2020) e una quarantina di colonne:

- **Identificazione**: `edition`, `year`, `country`, `country_noc`;
- **Medagliere**: `gold`, `silver`, `bronze`, `total`;
- **Contesto dell'edizione**: `paese_olimpiade`, `citta_olimpiade`;
- **Indicatori socio-economici** (media dei 4 anni pre-olimpici), tra cui: PIL corrente e pro capite, crescita del PIL, popolazione totale e in età lavorativa, urbanizzazione, aspettativa di vita, mortalità infantile, iscrizione scolastica, spesa militare, inflazione e superficie del paese.

## Output prodotti

La pipeline produce un dataset in formato CSV, usato come base in diversi notebook del progetto.


## Un bug nascosto: le righe fittizie da cambio di bandiera olimpica

Il dataset comune descritto sopra unisce, per ogni riga *paese × edizione*, il medagliere con gli indicatori socio-economici del paese in quel periodo. Questa unione, fatta per nome paese su tutta la serie storica 1964–2020, si è rivelata corretta per la stragrande maggioranza delle nazioni — ma ha generato un problema sistematico per tutti i paesi che, nel tempo, hanno cambiato identità olimpica: si sono divisi, uniti, o hanno gareggiato sotto una sigla diversa dalla propria.

**Come si è scoperto il problema.** Durante un controllo dei duplicati sul dataset, sono emerse due righe per la stessa combinazione *codice NOC × anno* in corrispondenza di Russia 1992 e Russia 2020: una con gli indicatori socio-economici popolati e 0 medaglie, l'altra con gli indicatori nulli e le medaglie reali. La causa: nel 1992 la Russia gareggiò come parte della Squadra Unificata (EUN, le 12 ex repubbliche sovietiche), e nel 2020 come ROC (Russian Olympic Committee, a seguito della squalifica della Russia per doping di stato) — due sigle diverse dalla Federazione Russa vera e propria. Il merge per nome paese aveva agganciato gli indicatori economici alla "Russia" su tutta la serie storica, indipendentemente da quale identità olimpica fosse effettivamente in gara quell'anno, creando così una riga fittizia parallela a quella corretta.

**La correzione.** Il problema è stato risolto costruendo una mappatura esplicita tra codice NOC (usato dal CIO per identificare le delegazioni sportive) e codice ISO (usato dagli indicatori World Bank) — i due standard, nati per scopi diversi, non coincidono sempre per le stesse entità storiche.

**Un audit più esteso.** Verificando lo stesso meccanismo su tutte le nazioni storicamente divise, unite o nate nel periodo 1964–2020, lo stesso tipo di riga fittizia è emerso anche per:

- **Germania**: 6 righe fittizie (1968–1988, periodo della divisione tra Germania Ovest e Germania Est)
- **Cecoslovacchia → Cechia e Slovacchia**: 16 righe fittizie (1964–1992, prima che le due repubbliche esistessero come Comitati Olimpici indipendenti)
- **Jugoslavia → Bosnia-Erzegovina, Croazia, Macedonia del Nord, Montenegro, Slovenia, Serbia**: 46 righe fittizie (1964–1992)
- **Serbia e Montenegro → Serbia e Montenegro separate**: 6 righe fittizie (1996–2004)

In tutti questi casi il pattern era identico: una riga a zero medaglie, con indicatori economici popolati, per un'entità che in quell'anno non esisteva ancora come Comitato Olimpico indipendente — duplicata rispetto alla riga reale della federazione che allora esisteva davvero (URSS, Cecoslovacchia, Jugoslavia). In totale, oltre alle correzioni su Germania e Russia, sono state rimosse **68 righe fittizie aggiuntive**.

**Un problema diverso: codici incoerenti nel tempo.** Due nazioni — Trinidad and Tobago ed Egitto — non presentavano righe duplicate, ma un codice NOC che cambiava a metà della serie storica (per esempio Egitto: UAR fino al 1968, poi EGY dal 1972). Non essendoci sovrapposizione di anni non si trattava di un duplicato da rimuovere, ma di una serie storica "spezzata" in due tronconi con codici diversi — un problema comunque rilevante per le analisi che usano lo storico recente di un paese (come le feature di lag), risolto unificando i due codici in uno solo.

## Verifica finale

Dopo tutte le correzioni, il dataset è stato controllato sistematicamente per:

- **Nomi doppi sotto lo stesso codice NOC**: nessuno residuo
- **Righe fittizie a zero medaglie per le entità storiche corrette**: nessuna residua, per tutti i casi elencati sopra
- **Duplicati sulla coppia codice NOC + anno**: zero
- **Somma totale delle medaglie**: invariata rispetto alla versione precedente alla correzione (11.782) — a conferma che nessuna medaglia reale è stata toccata, solo righe fittizie e codici incoerenti

Il dataset finale parte da 3.126 righe grezze e arriva a **3.058 righe** dopo la rimozione delle righe fittizie residue; dopo la successiva pulizia dei valori mancanti applicata dalle singole analisi (interpolazione limitata a 3 anni di gap + imputazione con mediana per nazione + eliminazione delle sole righe prive dei pilastri fondamentali PIL, popolazione e punteggio medaglie) si arriva a **2.619 osservazioni valide** — l'**85,7%** del dataset di partenza, una quota di conservazione alta proprio perché la base di partenza era già pulita.

## Note metodologiche

- **Finestra temporale pre-olimpica**: gli indicatori sono aggregati sui 4 anni precedenti ciascuna edizione. Il valore è un parametro dello script e può essere modificato per analisi di sensibilità.
- **Valori mancanti**: la media è calcolata sui soli anni disponibili nella finestra (`skipna`); se nessun anno è disponibile la cella resta vuota. Nessun valore viene imputato in questa fase: le scelte di imputazione sono lasciate alle singole analisi.
- **Paesi non riconosciuti**: alcuni codici ISO non esistono nella nomenclatura World Bank (per esempio comitati olimpici storici o territori particolari); Per questi casi si è proveduto ad adeguare il dataset "manualmente" attraverso Jupyter Notebook e pandas.
