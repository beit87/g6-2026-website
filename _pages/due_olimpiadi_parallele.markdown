---
layout: default
title: "Due Olimpiadi parallele"
subtitle: "Olimpiadi e ricchezza - un'analisi di 60 anni di medaglie (1964-2020)"
---



*Perché i Giochi Olimpici non sono mai stati un campo da gioco equo — e ce lo dice il profilo economico di lungo periodo di 208 paesi.*

Ogni quattro anni raccontiamo le Olimpiadi come la più grande gara di merito del pianeta: atleti che si allenano, sudano, vincono. Ma dietro il podio c'è un'altra classifica, molto più silenziosa e molto più prevedibile: quella della **ricchezza dei paesi**. Analizzando 36mila medaglie assegnate dal 1964 al 2024 e incrociandole con il profilo socioeconomico di lungo periodo di ogni nazione, emerge una tesi netta: **più un paese è ricco, in media, su sei decenni, più medaglie vince per abitante — e vince in sport diversi da quelli in cui vincono i paesi poveri.**

> **IL NUMERO CHIAVE**
>
> ### ~96 volte
>
> *Le medaglie vinte per milione di abitanti dai paesi "ricchi avanzati" rispetto ai "poveri estremi", nella media 1964-2024*

## La domanda di fondo

Le classifiche olimpiche per numero assoluto di medaglie premiano quasi sempre le stesse nazioni: Stati Uniti, Cina, Russia, Germania, Regno Unito. Ma è un confronto onesto? Un paese con 1,4 miliardi di abitanti come la Cina ha, semplicemente, più atleti tra cui scegliere di un paese con 5 milioni di abitanti. Per capire se esiste un vero "vantaggio da ricchezza", occorre guardare le medaglie per abitante — e occorre farlo confrontando paesi con un profilo economico realmente comparabile.

Questa pagina racconta i risultati ottenuti con il cosiddetto "cluster statico": un'unica fotografia socioeconomica per ciascun paese, costruita sulla media di tutti gli indicatori disponibili lungo l'intero periodo 1964-2024 (non solo l'ultimo anno, non un singolo anno di gara). È il modo più conservativo e più stabile di chiedersi: indipendentemente dalle fluttuazioni economiche di una singola edizione, qual è il profilo di lungo periodo di questo paese — e che ruolo gioca nello sport olimpico?

## Il metodo, in breve

Per ciascuno dei 208 paesi con dati sufficienti, sono stati calcolati i valori medi 1964-2024 di cinque indicatori socioeconomici: PIL pro capite, aspettativa di vita, tasso di urbanizzazione, mortalità infantile e iscrizione alla scuola primaria. Un algoritmo di clustering (k-means) ha poi raggruppato questi 208 profili-paese in quattro classi omogenee, ordinate per ricchezza media dalla più alta alla più bassa.

Il risultato sono quattro "mondi" socioeconomici, ciascuno associato in modo permanente a un gruppo di paesi: ogni medaglia vinta da un paese, in qualunque anno, viene attribuita al profilo economico di lungo periodo di quel paese.

### I quattro mondi olimpici

| Cluster | N. paesi | Esempi rappresentativi |
|---|---|---|
| **Ricchi avanzati** | 36 | Monaco, Isole Cayman, Liechtenstein, San Marino, Lussemburgo, Bermuda, Svizzera, Norvegia, Qatar, Bahrein |
| **Reddito medio-alto** | 70 | Antigua e Barbuda, Belize — il cluster più numeroso: economie di reddito intermedio in fase di industrializzazione o urbanizzazione avanzata |
| **Reddito basso-medio** | 64 | Algeria, Azerbaigian |
| **Poveri estremi** | 38 | Afghanistan, Angola, Bangladesh, Burundi, Benin, Bhutan |

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json1.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>


## Il risultato centrale: chi vince, per abitante

Guardando alle medaglie vinte in rapporto alla popolazione di ciascun paese, il divario tra i quattro cluster è netto e monotono: si scende a gradini da un mondo all'altro, senza eccezioni. I paesi "ricchi avanzati" vincono in media 0,679 medaglie ogni milione di abitanti; i paesi a "reddito medio-alto" ne vincono 0,402; il "reddito basso-medio" crolla a 0,068; i "poveri estremi" si fermano a 0,007 — meno di un decimo del gruppo appena sopra, e circa un novantaseiesimo dei paesi più ricchi.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json2.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Medaglie per milione di abitanti, media dei paesi di ciascun cluster socioeconomico statico (1964-2024).*

Il divario non è un artefatto del metodo: la stessa gerarchia — con valori assoluti diversi ma lo stesso ordine e proporzioni altrettanto marcate — emerge anche usando il cluster "dinamico", che etichetta ogni paese anno per anno invece che con una media di lungo periodo. È un secondo segnale di robustezza: la relazione tra ricchezza e successo olimpico pro capite non dipende dalla scelta tecnica di come si misura la ricchezza nel tempo.

### Il divario nel tempo

Il vantaggio dei paesi ricchi non è un fenomeno recente né in via di esaurimento. Tracciando, edizione dopo edizione, il tasso medio di medaglie pro capite di ciascun cluster, il gruppo dei paesi "ricchi avanzati" resta stabilmente sopra a tutti gli altri lungo l'intero arco 1964-2024, con oscillazioni legate soprattutto ai boicottaggi della Guerra Fredda e all'espansione del programma olimpico, ma senza mai un vero riavvicinamento verso gli altri cluster.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json3.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Medaglie per milione di abitanti nel tempo, per cluster socioeconomico statico (1964-2024).*

## Non solo quante, ma quali medaglie

La ricchezza non predice soltanto quante medaglie vince un paese, ma anche in quali sport le vince. Un test statistico chi-quadro sulla distribuzione delle medaglie tra sport e cluster restituisce un risultato inequivocabile (χ² = 3.327,9; gradi di libertà = 87; p < 0,001): la probabilità che questa distribuzione sia dovuta al caso è, a tutti gli effetti, nulla.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json4.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Distribuzione percentuale delle medaglie per sport all'interno di ciascun cluster (ogni riga somma al 100%).*

Il quadro che emerge è coerente con l'intuizione: gli sport "ricchi avanzati" sono quelli che richiedono attrezzature costose, infrastrutture dedicate o animali — equitazione (indice di specializzazione 1,46x rispetto alla media), nuoto (1,44x), vela (1,41x), ciclismo (1,37x), canottaggio (1,25x). All'estremo opposto, i paesi a "reddito basso-medio" e "poveri estremi" si concentrano su sport che richiedono soprattutto un corpo allenato e poco altro: hockey su prato, taekwondo, calcio, atletica, pugilato — in alcuni casi (come l'hockey su prato nei "poveri estremi") con indici di specializzazione vicini a 9 volte la media globale.

### Chi domina davvero ogni sport?

Ribaltando la prospettiva — e chiedendosi non "di cosa vive ogni cluster" ma "chi vince davvero in ogni disciplina" — il quadro si conferma. In sport come equitazione, nuoto, vela e ciclismo, tra il 73% e il 78% delle medaglie va ai paesi del cluster "ricchi avanzati". In altri sport, come sollevamento pesi, tennistavolo, badminton e taekwondo, la maggioranza assoluta delle medaglie viene invece vinta da paesi non ricchi.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json5.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Quota percentuale di medaglie per cluster in ciascuno sport (ogni colonna somma al 100%).*

### Gli sport più (e meno) "democratici"

Ordinando gli sport in base alla quota di medaglie vinte da paesi non appartenenti al cluster "ricchi avanzati", si ottiene una classifica di accessibilità economica. In testa, la ginnastica ritmica (93,0% delle medaglie a paesi non ricchi), il badminton (84,8%), il taekwondo (77,9%), il sollevamento pesi (76,5%) e il tennistavolo (71,4%). In fondo, l'equitazione, dove appena il 21,8% delle medaglie sfugge ai paesi ricchi, seguita da nuoto (23,3%), vela (24,4%) e ciclismo (26,9%).

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json6.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Quota % di medaglie vinte da paesi non appartenenti al cluster "ricchi avanzati", per sport.*

La stessa storia, letta come composizione interna di ogni disciplina, mostra visivamente quanto ogni sport sia "colorato" da un profilo economico dominante: alcuni sport sono quasi interamente di un colore (i "ricchi avanzati" in equitazione e vela), altri sono un mosaico più equilibrato di tutti e quattro i cluster.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json7.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Composizione percentuale di ciascuno sport per cluster socioeconomico statico, ordinati dal più accessibile al più esclusivo.*

## Un test predittivo: si può indovinare chi vince?

I risultati fin qui descritti sono "descrittivi": misurano associazioni tra ricchezza e medaglie osservate nel passato. Per irrobustire la tesi, l'analisi va oltre e si chiede: conoscendo soltanto il profilo socioeconomico di un paese in un dato anno (PIL pro capite, aspettativa di vita, urbanizzazione, mortalità infantile, popolazione, più un indicatore per il vantaggio di giocare in casa), quanto è possibile prevedere se quel paese vincerà almeno una medaglia in ciascuno sport?

Per rispondere, è stato addestrato un modello di regressione logistica indipendente per ciascuno dei 27 sport con almeno 50 medaglie storiche, su 2.423 osservazioni paese-edizione, validato con cross-validation a 5 gruppi e misurato con l'AUC-ROC — un punteggio da 0,5 (previsioni casuali) a 1,0 (previsioni perfette).

> **CAPACITÀ PREDITTIVA DEL SOLO PROFILO ECONOMICO**
>
> ### 0,74 – 0,97 AUC
>
> *Intervallo di AUC-ROC ottenuto nei 27 sport analizzati, usando solo indicatori socioeconomici e vantaggio di ospitare i Giochi*

Il risultato è sorprendentemente forte: conoscere solo il profilo economico di un paese permette già di prevedere con ottima accuratezza chi vincerà medaglie in nuoto sincronizzato, tennistavolo, tiro con l'arco, tuffi e badminton (AUC tra 0,93 e 0,97), mentre la previsione è più incerta — ma comunque nettamente sopra il caso — per pugilato, atletica e lotta (AUC tra 0,74 e 0,81): sport dove il talento individuale e altri fattori non economici contano visibilmente di più.

Tradotto in probabilità concrete: un paese-tipo del cluster "ricchi avanzati" ha una probabilità stimata del 77% di salire sul podio in canottaggio in una data edizione, contro una probabilità sostanzialmente nulla (circa lo 0%) per un paese-tipo del cluster "poveri estremi". Il divario si restringe, ma non si annulla mai, negli sport più accessibili.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json8.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Probabilità predetta di vincere almeno una medaglia, per profilo-paese, negli sport più "polarizzati" (sinistra) e in quelli più "equi" (destra).*

### Il modello lineare tiene testa a quelli più sofisticati

Per verificare che la relazione non nasconda soglie o interazioni complesse che un modello semplice come la regressione logistica non riuscirebbe a cogliere, gli stessi dati sono stati rielaborati anche con due modelli non lineari più flessibili, Random Forest e Gradient Boosting, con impostazioni volutamente prudenti per non favorirli artificialmente. Il miglioramento è quasi sempre presente (il Random Forest supera la logistica in 25 sport su 27, il Gradient Boosting in 24 su 27) ma resta contenuto per la maggior parte degli sport, tipicamente tra i 2 e i 6 punti percentuali di AUC: un segnale che il legame tra ricchezza di un paese e probabilità di medaglia è in gran parte lineare e non richiede spiegazioni più complesse.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json9.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>



I pochi sport in cui i modelli non lineari guadagnano di più — pugilato e lotta in testa (oltre 9-10 punti di AUC in più), seguiti da atletica, hockey su prato ed equitazione — sono anche, non a caso, in gran parte gli stessi sport in cui i paesi non ricchi hanno mostrato la maggiore capacità di competere: qui la relazione tra reddito e successo sportivo è probabilmente meno una linea retta e più una soglia, oltre la quale contano fattori diversi dal PIL.

## La tesi: due Olimpiadi parallele

Mettendo insieme i due risultati — quante medaglie e quali medaglie — la conclusione a cui porta l'analisi è che, di fatto, esistono due Olimpiadi parallele. C'è un'Olimpiade delle infrastrutture: quella dei centri sportivi, dei circoli velici, delle scuderie e delle piscine olimpioniche, dominata quasi per intero dai paesi più ricchi in modo stabile da sei decenni. E c'è un'Olimpiade del corpo: quella degli sport da combattimento, dell'atletica e degli sport di squadra a basso costo infrastrutturale, dove i paesi a reddito medio e basso riescono a competere e spesso a dominare, pur restando enormemente svantaggiati sul totale complessivo delle medaglie pro capite.

Il profilo economico di lungo periodo di un paese, quindi, non si limita a determinare se un paese vincerà molte o poche medaglie: plasma letteralmente il tipo di eroe sportivo che quel paese può produrre. Ed è un pattern che resiste al cambio del metodo statistico usato per misurarlo — segno che non è un artefatto tecnico, ma una regolarità strutturale dello sport olimpico moderno.

## Nota metodologica

Il cluster "statico" qui presentato è complementare — non alternativo — a un cluster "dinamico", che assegna a ogni combinazione paese-edizione il profilo socioeconomico specifico di quell'anno. Il cluster dinamico risponde alla domanda "qual era il profilo del paese nell'anno in cui ha vinto quella medaglia?", utile per cogliere la mobilità economica nel tempo (ad esempio la trasformazione di Corea del Sud e Cina). Il cluster statico risponde invece a "qual è il profilo medio di lungo periodo di questo paese?": un'unica fotografia, utile per confronti strutturali che non dipendano dalle fluttuazioni economiche di una singola edizione.

Entrambi gli approcci usano la stessa pipeline (imputazione dei valori mancanti con la mediana, standardizzazione, k-means con k=4) e restituiscono risultati ampiamente coerenti tra loro — un ulteriore elemento a sostegno della robustezza della relazione tra profilo socioeconomico e performance olimpica.

## Un'ultima prospettiva: cosa racconta (e cosa non racconta) il cluster dinamico

Il cluster statico, su cui si basa tutta l'analisi precedente, fotografa la posizione economica di lungo periodo di ciascun paese: è la scelta più adatta per confrontare, in modo stabile, profili diversi. Ma proprio perché fissa un'unica etichetta per paese, non può raccontare una storia altrettanto importante: quella della mobilità economica. Per questo il progetto include anche un secondo modello, il cluster "dinamico", che ricalcola il raggruppamento in quattro classi separatamente per ogni edizione olimpica, sugli indicatori specifici di quell'anno — così un paese può cambiare cluster nel tempo, seguendo la propria traiettoria di sviluppo reale.

Il quadro che emerge è coerente con la storia economica: su 208 paesi analizzati, 146 hanno cambiato fascia di reddito almeno una volta tra il 1964 e il 2024. I casi più istruttivi sono le due economie asiatiche protagoniste del "miracolo" del dopoguerra.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json10.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>
*Medaglie vinte per edizione (barre) e PIL pro capite (linea) per Corea del Sud e Cina, con i punti di passaggio da un cluster all'altro (cluster dinamico).*

La Corea del Sud parte nel 1964 nel gruppo dei "poveri estremi", esce da quella fascia già nel 1972 ("reddito basso-medio"), sale a "reddito medio-alto" a metà anni '80 e raggiunge il cluster dei "ricchi avanzati" solo intorno al 2016 — più di cinquant'anni e diverse generazioni di atleti dopo il suo ingresso nei Giochi. Nello stesso periodo le sue medaglie pro capite sono più che quadruplicate (+403,8% tra il periodo precedente e quello successivo alla prima uscita dalla fascia più povera). La Cina segue una traiettoria simile ma più lenta a completarsi: entra nella fascia "reddito medio-alto" solo nel 2008, in concomitanza (non a caso) con le Olimpiadi di Pechino, e alla fine della serie storica disponibile (2020) non ha ancora raggiunto la fascia dei "ricchi avanzati".

Questi due casi mostrano bene il valore aggiunto del cluster dinamico — e insieme il suo limite più importante. Poiché ogni edizione viene reclusterizzata da zero sui soli paesi con dati disponibili quell'anno, la composizione e le soglie di ciascuna fascia (in particolare quella dei "ricchi avanzati") non sono fisse nel tempo: lo stesso livello di PIL pro capite può ricadere in cluster diversi a seconda di come si posizionano, quell'anno, tutti gli altri paesi. Questo rende il confronto tra decenni lontani meno diretto rispetto al cluster statico, ed è anche il motivo per cui il passaggio di un paese al gruppo dei "ricchi avanzati" tende visibilmente a concentrarsi nelle edizioni più recenti: ci vogliono decenni di crescita sostenuta perché un'economia emergente scavalchi il resto del mondo, non solo se stessa nel tempo. A ciò si aggiunge un limite più tecnico: gli indicatori socioeconomici delle edizioni più lontane nel tempo (anni '60 e '70) sono spesso più incompleti di quelli recenti, il che rende le etichette di cluster di quelle prime edizioni potenzialmente meno affidabili di quelle più vicine a noi.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/alessia/chart_json11.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>

Per questo, nel resto di questa analisi, il cluster statico resta il riferimento principale: il cluster dinamico va letto come una lente complementare, utile per raccontare le traiettorie di singoli paesi, non come sostituto del confronto strutturale tra profili economici.