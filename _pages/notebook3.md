---
layout: default
title: "Chi salirà sul podio a Los Angeles?"
header_title: "Chi salirà sul podio a Los Angeles?"
subtitle: "Machine Learning, causalità e previsioni per i Giochi Olimpici del 2028"
header_type: hero
header_img: "assets/images/img_olimpiadi.jpg"
vega: true
custom_css: /assets/css/g6-charts.css
---

Costruiamo un modello predittivo, testiamo se investire nello sport causa davvero più medaglie, e stimiamo il medagliere di Los Angeles 2028.
{: .lead}

---

<h3>Cosa conta davvero, la risposta sorprende</h3>
<p>Il Random Forest (R² = 0.75 in cross-validation) rivela che il predittore più forte non è il PIL, ma le <strong>medaglie del ciclo precedente</strong>, che pesano il 46% dell'intera capacità predittiva del modello. I sistemi sportivi d'élite sono inerti: infrastrutture, coach e atleti in sviluppo si costruiscono su cicli pluriennali, non da un'edizione all'altra.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb3_feature_importance.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>L'investimento causa le medaglie? Il test di causalità</h3>
<p>Con un'analisi Difference-in-Differences confrontiamo le nazioni che hanno cambiato la spesa sportiva in modo diverso tra Tokyo 2020 e Paris 2024. Il pattern è chiaro: chi ha <strong>aumentato la spesa oltre il 40%</strong> ha guadagnato in media +12.8 medaglie, chi l'ha tagliata ne ha perse 8.5. La monotonia del risultato è la firma di un effetto causale, non solo di una correlazione.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb3_did.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>Le previsioni per Los Angeles 2028</h3>
<p>Applicando il modello con le medaglie di Paris 2024 come base: <strong>USA 101</strong> (effetto host stimato +15), <strong>Cina 91</strong> (stabile), <strong>Gran Bretagna 66</strong>, <strong>Francia 62</strong> (in calo dopo l'effetto host di Paris), <strong>Italia 39</strong> (stabile rispetto a Tokyo 2020). Gli intervalli di confidenza al 10-90% riflettono l'incertezza genuina, più ampia per le nazioni medie.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb3_predictions_ci.json" style="width: 100%; height: 100%"></vegachart>
</div>

---

## Risposta alla Domanda di Ricerca

**Si, gli investimenti in infrastrutture sportive producono medaglie olimpiche.** Le medaglie del ciclo precedente sono il predittore più forte (inerzia dei sistemi sportivi), il test di causalità conferma che aumentare la spesa produce risultati misurabili, e le previsioni per Los Angeles 2028 riflettono sia la storia recente che l'effetto host per gli USA.
