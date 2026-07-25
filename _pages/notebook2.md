---
layout: default
title: "Il prezzo dell'oro"
subtitle: "Oltre il PIL: quanto costa davvero vincere una medaglia olimpica?"
vega: true
custom_css: /assets/css/g6-charts.css
---

{% include page-hero.html title="Il prezzo dell'oro" %}

Il PIL totale correla con le medaglie olimpiche (r = 0.58), ma non spiega tutto. Cosa succede se guardiamo direttamente quanto ogni paese investe nello sport d'élite, invece che alla sua ricchezza complessiva? In questa analisi usiamo due fonti di dati reali: il progetto SPLISS, che misura la spesa élite quadriennale di 14-17 nazioni a Tokyo 2020 e Paris 2024, e i dati ufficiali di UK Sport, che dal 2000 al 2024 tracciano ogni sterlina investita dal governo britannico nello sport olimpico.
{: .lead}

---

<h3>La spesa élite spiega le medaglie meglio del PIL</h3>
<p>Confrontando il PIL totale con la spesa sportiva élite reale, il risultato è netto: la spesa élite raggiunge <strong>r = 0.85-0.88</strong>, contro <strong>r = 0.58</strong> del PIL. Non conta solo quanto è ricco un paese, ma quanto di quella ricchezza viene effettivamente investita nello sport di alto livello. Paesi con PIL simile possono avere strategie di investimento radicalmente diverse, e questo si riflette direttamente nel medagliere.</p>
<p>Nel grafico, il paese ospitante di ciascuna edizione è evidenziato in rosso: sia il Giappone a Tokyo che la Francia a Paris mostrano una posizione anomala rispetto al trend generale, spendendo di più e ottenendo più medaglie del previsto grazie all'effetto casa, un fattore che analizziamo separatamente più avanti.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb2_spliss_scatter.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>Non tutte le medaglie costano uguale</h3>
<p>Il costo per medaglia varia enormemente tra le 14 nazioni SPLISS: il <strong>Belgio</strong> è il più efficiente con circa €2.8M per medaglia, ottenuto concentrando i fondi su ciclismo su pista e atletica. Il <strong>Brasile</strong>, all'estremo opposto, spende circa €9M per medaglia, un sistema sportivo ancora in costruzione con investimenti diffusi su molte discipline senza eccellenza in nessuna.</p>
<p>Il <strong>Giappone</strong>, paese ospitante a Tokyo 2020, mostra un costo elevato (€6.9M per medaglia): parte di quell'investimento non produce medaglie direttamente ma costruisce infrastrutture che restano utili per decenni. Il messaggio centrale è che l'efficienza non cresce linearmente con la spesa: conta l'allocazione strategica delle risorse, non il volume totale investito.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb2_costo_medaglia.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>UK Sport: la prova più solida disponibile</h3>
<p>Il caso britannico è il dataset più trasparente al mondo su questo tema: sette cicli olimpici consecutivi, ogni disciplina finanziata singolarmente e pubblicamente. La correlazione tra investimento e medaglie è <strong>r = 0.947, R² = 0.90</strong>, il 90% della varianza è spiegato dai fondi stanziati, senza eccezioni in nessuno dei sette cicli.</p>
<p>Il salto tra Atene 2004 (£71M, 30 medaglie) e Pechino 2008 (£235M, 47 medaglie), un aumento del 231% nei fondi che ha prodotto un +57% nelle medaglie, resta il caso di studio più citato in letteratura sul legame causale investimento-successo olimpico. Quella scelta politica arrivò dopo l'umiliazione di Atlanta 1996, dove il Regno Unito vinse solo 15 medaglie, 36° posto nel medagliere.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb2_uksport.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>Ospitare i Giochi vale in media +117% di medaglie</h3>
<p>Per ogni paese ospitante, calcoliamo la variazione percentuale tra le medaglie vinte in casa e la propria media storica nelle altre edizioni. Il risultato, escludendo i boicottaggi del 1980/1984, è una mediana di <strong>+117%</strong> (praticamente il doppio delle medaglie abituali), con <strong>p = 0.004</strong>, un risultato statisticamente solido. L'85% dei paesi ospitanti (11 su 13, escludendo i boicottaggi) migliora i propri risultati rispetto alla propria media storica.</p>
<p>Usiamo la mediana anziché la media semplice perché alcuni casi come la Grecia 2004 (che partiva da una media storica bassissima, meno di 2 medaglie) generano variazioni percentuali estreme che distorcerebbero il quadro generale.</p>
<p>L'effetto combina tre fattori che si sommano: gli investimenti pre-Giochi aumentano sistematicamente nei quattro anni precedenti l'evento, il pubblico di casa genera un vantaggio misurabile in molte discipline individuali, e l'assenza di stress da trasferta e fuso orario avvantaggia gli atleti locali. I casi più emblematici sono Australia 2000 (+31 medaglie rispetto alla propria media) e Gran Bretagna 2012 (+35), entrambi paesi con sistemi sportivi già maturi che si sono esaltati con il vantaggio di casa.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb2_host_effect.json" style="width: 100%; height: 100%"></vegachart>
</div>

---

## In sintesi

- La **spesa élite reale** spiega le medaglie molto meglio del PIL (r = 0.85-0.88 vs r = 0.58): misura direttamente il flusso di risorse verso lo sport di alto livello.
- Il **costo per medaglia** varia da €2.8M (Belgio) a oltre €9M (Brasile): conta l'efficienza dell'allocazione, non il volume di spesa.
- **UK Sport** dimostra la relazione più solida in letteratura: r = 0.947, R² = 0.90 su sette cicli consecutivi.
- **Ospitare i Giochi** vale in media +117% di medaglie rispetto alla propria media storica (p = 0.004).

### Nota metodologica

I dati SPLISS coprono solo 14-17 nazioni e due cicli olimpici: il campione è troppo piccolo per stime panel formali con effetti fissi. L'effetto paese ospitante esclude i boicottaggi del 1980 e 1984 perché il delta riflette l'assenza dei rivali, non il vero vantaggio di campo.
