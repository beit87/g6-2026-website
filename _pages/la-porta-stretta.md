---
layout: default
title: "La porta stretta dei poveri, il bivio dei ricchi"
subtitle: "Sessant'anni di Olimpiadi raccontano due storie sul denaro e lo sport — una di apertura, una di privilegio persistente"
vega: true
---

{% include page-hero.html title="La porta stretta dei poveri, il bivio dei ricchi" %}

## La soglia che inganna

Nel 1964 il paese più povero a vincere una medaglia olimpica aveva un PIL pro capite di 77 dollari. Nel 2020, di 718 — quasi dieci volte tanto. È una lettura sbagliata. Nello stesso periodo, il PIL pro capite mediano di tutti i paesi del mondo è cresciuto di oltre 23 volte, da 266 a 6.247 dollari. Il pianeta si è arricchito molto più in fretta della soglia di ingresso al medagliere. Confrontare 77 dollari con 718 significa confrontare due epoche economiche diverse, non misurare la stessa barriera in due momenti.

La domanda giusta non è quanti dollari servano, ma dove si colloca il paese più povero capace di vincere, rispetto a tutti gli altri paesi di quello stesso anno. E qui la storia si ribalta: nel 1964 quel paese occupava il decimo percentile della ricchezza mondiale — povero, ma non ultimo. Nel 2004, e di nuovo nel 2016, il paese-soglia era letteralmente all'ultimo posto: il paese più povero del pianeta, quell'anno, ha vinto comunque una medaglia. Il trend è discendente e statisticamente solido (p = 0,0008 su quindici edizioni dal 1964 al 2020).

| Anno | Soglia (USD) | Percentile mondiale | % ricchi a secco |
|:----:|-------------:|:--------------------:|------------------:|
| 1964 | 77           | 9,6°                 | 75,0%             |
| 1980 | 173          | 7,2°                 | 85,2%             |
| 1996 | 160          | 1,0°                 | 71,8%             |
| 2004 | 117          | 0,0°                 | 73,9%             |
| 2016 | 243          | 0,0°                 | 71,1%             |
| 2020 | 718          | 5,4°                 | 66,1%             |

<p>------------</p>
<br/>

> **Nel 2004 e nel 2016, il paese più povero a vincere una medaglia era, letteralmente, il paese più povero al mondo quell'anno.**

Le Olimpiadi, misurate correttamente, sono diventate più accessibili a chi ha meno risorse. Questo non significa che il denaro non conti: in ogni edizione dal 1964 al 2020 la correlazione tra PIL pro capite e medaglie vinte resta positiva e significativa, anche se modesta (un coefficiente tipicamente tra 0,18 e 0,33). E restare ricchi non basta comunque a garantirsi un posto sul podio — tra il 66% e l'85% dei paesi con PIL sopra la soglia, a seconda dell'edizione, torna comunque a casa senza medaglie.

## Il bivio: vincere insieme o vincere da soli

Partendo da questa analisi, può essere fatto un passo in avanti osservando la struttura dei paesi in un dato momento — si scopre che la stessa ricchezza che rende un'Olimpiade più aperta ai poveri produce, allo stesso tempo, una spaccatura molto netta a seconda dello sport.

Usando il dettaglio di ogni medaglia assegnata dal 1964 al 2016, abbiamo classificato ciascuna vittoria come "individuale" (un solo atleta) o "di squadra" (più atleti della stessa nazione, staffette comprese), e raggruppato 88 paesi con almeno cinque medaglie in tre profili distinti, tramite un algoritmo di clustering che non impone etichette a priori.

Sono emersi tre gruppi nitidi. I "Misti" — grandi potenze sportive con programmi ampi e diversificati — vincono in modo bilanciato in entrambe le categorie e hanno il PIL pro capite medio più alto: 13.077 dollari. Gli "Specialisti squadra" li seguono, a 9.889 dollari. Gli "Specialisti individuale" — la cui intera produzione di medaglie arriva quasi solo da gare individuali, spesso di resistenza — hanno il PIL più basso: appena 6.991 dollari di media, e solo 2.444 dollari di mediana, segno che il gruppo include diverse economie molto povere.

### Analisi Cluster e Impatto del PIL sulle Vittorie Olimpiche

**Dashboard: profilo squadra/individuale dei paesi e relazione col PIL pro capite**

A sinistra: ogni punto è un paese, posizionato secondo la quota di medaglie vinte in eventi individuali (asse x) e il volume totale di medaglie (asse y, scala log), colorato per cluster K-Means. A destra: la stessa quota individuale confrontata col PIL pro capite medio del paese (scala log); la linea nera è il trend di regressione — la sua pendenza negativa riflette la correlazione di Spearman ρ = −0,422 (p = 0,001).

<div style="height: 520px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Luisa/chart_scatter_cluster.json" style="width: 100%; height: 100%"></vegachart>
</div>
<div style="font-size: 12px; color: #666; margin-top: 2rem; margin-bottom: 1.5rem;">Ogni punto è un paese. L'asse orizzontale è la quota di medaglie individuali, l'asse verticale il volume totale di medaglie (scala log); il colore indica il cluster K-Means.</div>

<div style="height: 520px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Luisa/chart_pil_per_cluster.json" style="width: 100%; height: 100%"></vegachart>
</div>
<div style="font-size: 12px; color: #666; margin-top: 2rem; margin-bottom: 1.5rem;">Distribuzione completa del PIL pro capite in ciascun cluster (non solo la media): la "scatola" mostra quanto varia la ricchezza dei paesi all'interno dello stesso profilo di vittoria.</div>

<div style="height: 520px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Luisa/chart_quota_vs_pil.json" style="width: 100%; height: 100%"></vegachart>
</div>
<div style="font-size: 12px; color: #666; margin-top: 2rem; margin-bottom: 1.5rem;">La stessa correlazione di Spearman (ρ = −0,422) vista paese per paese, con la linea tratteggiata a indicare il trend di regressione: più PIL, meno dipendenza dalle medaglie individuali.</div>
<p>------------</p>
<br/>

> **I tre cluster non sono solo diversi nel modo di vincere: sono anche significativamente diversi nel PIL pro capite medio dei paesi che li compongono.**

Un test ANOVA conferma che questa differenza non è casuale (p = 0,007). E guardando i singoli paesi invece dei gruppi, la correlazione tra quota di medaglie individuali e PIL pro capite è negativa e robusta (ρ = −0,422, p = 0,001): più un paese è povero, più le sue medaglie dipendono quasi interamente da singoli fuoriclasse individuali; più è ricco, più riesce a competere anche — e soprattutto — negli sport di squadra.

## Perché succede: la stessa causa, vista da due angolazioni

Non è un caso che il paese-soglia della prima analisi sia quasi sempre l'Etiopia — mezzofondo, disciplina individuale — e mai un paese che vince ori a calcio o pallavolo. Costruire un programma di squadra competitivo richiede infrastrutture, campionati giovanili, allenatori, decenni di investimento continuo: risorse che solo le economie più solide possono sostenere su larga scala. Una vittoria individuale richiede "solo" un atleta eccezionale, capace di emergere anche in un contesto povero di risorse strutturali.

Ecco perché la soglia economica per entrare nel medagliere si è progressivamente abbassata nel tempo, mentre allo stesso tempo i paesi restano nettamente divisi per PIL a seconda del tipo di sport in cui vincono: sono due facce dello stesso fenomeno. La porta che si è allargata nel tempo è, specificamente, quella dello sport individuale. Quella dello sport di squadra resta socchiusa a chi può permettersi di costruirci sopra un intero sistema.

## In una frase

Il PIL di un paese non decide solo se vincerà una medaglia olimpica. Decide, più silenziosamente, attraverso quale porta ci arriverà — e i dati di sessant'anni di Giochi dicono che quella porta si sta allargando solo per chi gioca da solo.

*Metodologia: analisi su dati World Bank (PIL pro capite, NY.GDP.PCAP.CD) incrociati con il medagliere IOC e il dataset "120 Years of Olympic History" (dettaglio medaglia per atleta, sport ed evento). Olimpiadi estive, 1964–2020 (soglia storica); 1964–2016 (classificazione squadra/individuale e clustering, limitate dalla disponibilità dei dati a livello di singolo evento). Soglia di significatività statistica: p<0,05.*
