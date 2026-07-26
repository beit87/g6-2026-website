---
layout: default
title: "Chi salirà sul podio a Los Angeles?"
subtitle: "Machine Learning, causalità e previsioni per i Giochi Olimpici del 2028"
vega: true
custom_css: /assets/css/g6-charts.css
---

{% include page-hero.html title="Chi salirà sul podio a Los Angeles?" %}

Costruiamo un modello predittivo, verifichiamo che funzioni davvero su dati mai visti, testiamo se investire nello sport causa davvero più medaglie, e infine stimiamo il medagliere di Los Angeles 2028.
{: .lead}

---

<h3>Il modello funziona davvero? Test su Tokyo 2020</h3>
<p>Abbiamo allenato un Random Forest sulle edizioni 1968-2016 (R² = 0.75 in cross-validation su cinque modelli testati) e verificato le sue previsioni su <strong>Tokyo 2020</strong>, un intero ciclo olimpico mai visto durante l'allenamento. Il risultato: <strong>R² = 0.86, MAE = 4.2 medaglie</strong> per paese. Per i grandi paesi come USA e Cina l'errore è nell'ordine di poche unità, mentre per i paesi con 3-10 medaglie l'incertezza è naturalmente più alta in proporzione.</p>
<p>Nel grafico, la linea tratteggiata rappresenta la previsione perfetta (previsto = reale). L'outlier principale è il Giappone, dove l'effetto host non è completamente catturato dal modello: il paese ha vinto più medaglie di quante il sistema si aspettasse, proprio per il vantaggio di giocare in casa.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb3_predicted_vs_actual.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>L'investimento causa le medaglie? Il test di causalità</h3>
<p>Le correlazioni mostrano relazioni, ma non causalità: i paesi che vincono ricevono più fondi, il che potrebbe far sembrare che i fondi producano successo anche quando la direzione causale è opposta. Con un'analisi <strong>Difference-in-Differences</strong> confrontiamo le nazioni che hanno cambiato la spesa sportiva in modo diverso tra Tokyo 2020 e Paris 2024.</p>
<p>Il pattern è chiaro e monotono: chi ha <strong>aumentato la spesa oltre il 40%</strong> ha guadagnato in media +12.8 medaglie, chi l'ha mantenuta stabile è rimasto sostanzialmente invariato, e chi l'ha tagliata ne ha perse in media 8.5. Questa progressione ordinata tra i gruppi è la firma di un effetto causale, non solo di una correlazione casuale. Il caso UK Sport Atene→Pechino resta l'esempio più citato: +17 medaglie rispetto al trend degli altri paesi dopo aver triplicato i fondi.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb3_did.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>Le previsioni per Los Angeles 2028</h3>
<p>Applicando il modello con le medaglie di Paris 2024 come base e proiezioni economiche sui trend recenti: <strong>USA 101 medaglie</strong> (meno delle 126 di Paris 2024, ma con un effetto host stimato di circa +15 rispetto a quello che avrebbero senza i Giochi in casa), <strong>Cina 91</strong> (stabile), <strong>Gran Bretagna 66</strong>, <strong>Francia 62</strong> (in calo dopo aver beneficiato dell'effetto host a Paris), <strong>Italia 39</strong> (sostanzialmente stabile rispetto alle 40 di Tokyo 2020).</p>
<p>Gli intervalli di confidenza al 10-90%, calcolati dalla dispersione delle previsioni dei 300 alberi del Random Forest, sono più ampi per le nazioni medie (±10-15 medaglie per Olanda, Canada, Corea del Sud) e più stretti per USA e Cina (±10-12), riflettendo l'incertezza genuina su chi ha una traiettoria meno consolidata.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb3_predictions_ci.json" style="width: 100%; height: 100%"></vegachart>
</div>

---

## Risposta alla Domanda di Ricerca

**Si, gli investimenti in infrastrutture sportive producono medaglie olimpiche.** Il modello prevede con buona precisione anche su dati mai visti (R² = 0.86 su Tokyo 2020). Il test di causalità conferma che aumentare la spesa produce risultati misurabili nel ciclo successivo. Le previsioni per Los Angeles 2028 riflettono sia la storia recente di ogni nazione che l'effetto host per gli Stati Uniti.

### Nota metodologica

Le previsioni assumono trend economici stabili e nessun evento geopolitico straordinario. Il modello non include la spesa élite come feature perché i dati SPLISS coprono troppo poche nazioni per il training. L'endogeneità non è completamente risolta (servirebbe una variabile strumentale formale): il DiD riduce il problema senza eliminarlo del tutto.
