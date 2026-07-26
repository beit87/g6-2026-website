---
layout: default
title: "PIL, storico e boicottaggi"
subtitle: "Cosa spiega (e cosa non spiega) il medagliere olimpico"
vega: true
---

{% include page-hero.html %}

**Ogni medaglia ha una storia economica alle spalle — ma non solo.** Questa analisi parte dalla stessa domanda del progetto: quanto contano PIL e popolazione nel determinare quante medaglie vince un paese? La risposta è "molto, ma non nel modo in cui te lo aspetti": il fattore più predittivo di tutti non è la ricchezza di un paese, ma **quanto ha già vinto quattro anni prima**. E quando il modello sbaglia di più, spesso non è colpa sua: sono eventi storici — i boicottaggi olimpici del 1980 e del 1984 — a spiegare le sorprese più grandi.

## Tre famiglie di nazioni olimpiche

Con una tecnica di clustering (K-Means) i 220 paesi del dataset, osservati in ciascuna delle 15 edizioni dal 1964 al 2020, si raggruppano naturalmente in tre profili socio-economici molto riconoscibili:

<div style="height: 820px; margin: 1.5rem 0;">
<vegachart schema-url="{{site.baseurl}}/assets/charts/pil_vs_medaglie.json" style="width: 100%; height: 100%"></vegachart>
</div>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">Ogni punto è una coppia nazione-edizione, colorata per cluster socio-economico. Sotto, le nazioni con lo Score medio più alto (con almeno 3 edizioni disputate) nell'area selezionata sopra — trascina un rettangolo sullo scatter per filtrare la classifica.</div>

**Nota:** due casi non compaiono nella classifica pur avendo punteggi altissimi — Unified Team (le ex repubbliche sovietiche riunite nel 1992) e ROC (la Russia nel 2020, sotto squalifica per doping di stato). Entrambe hanno gareggiato una sola volta: la loro "media" coinciderebbe col picco di quell'unica edizione, scavalcando nazioni come gli Stati Uniti che mediano su 15 edizioni. Per questo la classifica richiede almeno 3 edizioni disputate; restano comunque visibili come singoli punti nello scatter.

- **Le Grandi Potenze Olimpiche** — PIL alto e popolazione ampia (USA, Cina, Germania, Francia, Italia, Australia, ma anche India, Brasile ed Egitto per pura scala economica e demografica). Dominano il medagliere in modo sistematico: possono permettersi infrastrutture sportive su larga scala e hanno un ampio bacino di atleti tra cui scegliere.
- **Le Economie Emergenti** — grandi popolazioni ma reddito pro capite basso. Il potenziale demografico c'è, ma raramente si trasforma in medaglie per mancanza di investimenti strutturati. È il gruppo più interessante: al suo interno si nascondono le storie di maggiore efficienza, come vedremo tra poco.
- **Le Nazioni Minori** — spesso benestanti a livello individuale (pensiamo a Islanda o Lussemburgo), ma con una popolazione troppo piccola per costruire un sistema sportivo competitivo su più discipline.

Il messaggio di fondo: **i dati non dividono il mondo in "ricchi che vincono" e "poveri che perdono".** Dividono il mondo in sistemi sportivi con le risorse per competere su larga scala, e sistemi che devono fare di più con meno — e alcuni, come vedremo, ci riescono benissimo.

## Un modello che prova a prevedere il medagliere

Con un modello di Random Forest — un algoritmo che impara da migliaia di combinazioni storiche di PIL, popolazione e altri indicatori — è possibile stimare quante medaglie un paese vincerà in una data edizione. Il modello spiega circa il **68% della variabilità** dei risultati: un buon punto di partenza, ma lascia intenzionalmente scoperto un 32% che è proprio la parte più interessante da raccontare (ci arriviamo tra poco).

La sorpresa più grande non è quanto il modello riesce a prevedere, ma *cosa* usa per farlo. Ci si aspetterebbe che il PIL sia il fattore principale. Invece, il singolo indicatore più importante — con un peso di quasi il **70%** su tutti gli altri messi insieme — è semplicemente **quante medaglie lo stesso paese aveva vinto nell'edizione precedente**.

<div style="height: 380px; margin: 1.5rem 0;">
<vegachart schema-url="{{site.baseurl}}/assets/charts/feature_importance_shap.json" style="width: 100%; height: 100%"></vegachart>
</div>

Il PIL conta ancora, ma soprattutto nel lungo periodo: apre la porta al potenziale, mentre è lo storico recente a decidere chi la attraversa davvero. I sistemi sportivi nazionali, insomma, cambiano lentissimamente: infrastrutture, allenatori e federazioni non si costruiscono (né si smontano) in quattro anni.

## Quando il modello sbaglia, spesso è la storia a spiegarlo

Qui entra la parte più curiosa dell'analisi. Guardando dove il modello sbaglia di più — le nazioni che vincono molto più o molto meno di quanto le loro risorse economiche farebbero pensare — emergono due tipi di storie molto diverse.

**Storie di efficienza vera.** Alcuni paesi convertono risorse limitate in risultati sproporzionati: Kenya ed Etiopia nell'atletica, la Giamaica nello sprint, Cuba nel pugilato. La spiegazione più plausibile — coerente con quello che si legge nella letteratura sportiva, anche se i nostri dati non permettono di dimostrarlo in modo diretto — è la specializzazione estrema in poche discipline ad alta resa, invece di provare a competere su tutti i fronti.

**Storie di politica, non di sport.** E poi ci sono i casi più estremi in assoluto, che raccontano tutt'altro. Il modello prevede circa **52 medaglie per la Bulgaria nel 1984** e **46 per il Giappone nel 1980** — sulla carta, paesi con le risorse per arrivare a quei numeri. Nella realtà, entrambi i paesi tornarono a casa **a zero medaglie**. Non per un crollo improvviso del loro sistema sportivo, ma perché semplicemente **non parteciparono**: il 1980 e il 1984 sono le due edizioni dei boicottaggi incrociati della Guerra Fredda (Mosca 1980, boicottata dagli USA e alleati; Los Angeles 1984, boicottata dall'URSS e blocco sovietico).

Lo stesso fenomeno si vede, in modo speculare, nel grafico qui sotto: la correlazione tra PIL e medaglie, che in quasi tutte le edizioni resta sopra 0,8, crolla esattamente nel 1980 — l'unico anno in cui la politica, non l'economia, ha deciso chi era sul podio.

<div style="height: 380px; margin: 1.5rem 0;">
<vegachart schema-url="{{site.baseurl}}/assets/charts/correlazione_pil_medaglie_nel_tempo.json" style="width: 100%; height: 100%"></vegachart>
</div>

Un modello economico, per definizione, non può sapere che una squadra è rimasta a casa per un embargo diplomatico. È uno dei limiti più onesti e più interessanti di tutta l'analisi.

## Cosa manca ancora

Due estensioni renderebbero il quadro più completo. La prima: il numero di atleti inviati da ogni paese, che permetterebbe di calcolare un vero "rendimento per atleta" invece di doverlo dedurre indirettamente. La seconda, emersa proprio da questa analisi: un indicatore esplicito di boicottaggio/non partecipazione, che eviterebbe di scambiare un evento politico per un fallimento sportivo.

## In sintesi

Il PIL apre le porte al potenziale olimpico di lungo periodo. Lo storico recente decide chi lo attiva davvero, edizione dopo edizione. E quando i numeri non tornano, a volte la spiegazione non è nei dati economici — è nei libri di storia.
