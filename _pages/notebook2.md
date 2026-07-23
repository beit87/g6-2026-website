---
layout: default
title: "Il prezzo dell'oro"
header_title: "Il prezzo dell'oro"
subtitle: "Oltre il PIL: quanto costa davvero vincere una medaglia olimpica?"
header_type: hero
header_img: "assets/images/img_olimpiadi.jpg"
vega: true
custom_css: /assets/css/g6-charts.css
---

Il PIL totale correla con le medaglie olimpiche (r = 0.58), ma non spiega tutto. Cosa succede se guardiamo direttamente quanto ogni paese investe nello sport d'élite, invece che alla sua ricchezza complessiva?
{: .lead}

---

<h3>La spesa élite spiega le medaglie meglio del PIL</h3>
<p>Confrontando il PIL totale con la spesa sportiva élite reale (dati SPLISS su 14-17 nazioni), il risultato è netto: la spesa élite raggiunge <strong>r = 0.85-0.88</strong>, contro <strong>r = 0.58</strong> del PIL. Non conta solo quanto è ricco un paese, ma quanto di quella ricchezza viene effettivamente investita nello sport di alto livello.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb2_spliss_scatter.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>UK Sport: la prova più solida disponibile</h3>
<p>Il caso britannico è il dataset più trasparente al mondo su questo tema: sette cicli olimpici, ogni disciplina finanziata singolarmente e pubblicamente. La correlazione tra investimento e medaglie è <strong>r = 0.947, R² = 0.90</strong>, il 90% della varianza è spiegato dai fondi stanziati. Il salto tra Atene 2004 (£71M, 30 medaglie) e Pechino 2008 (£235M, 47 medaglie) resta il caso di studio più citato in letteratura.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb2_uksport.json" style="width: 100%; height: 100%"></vegachart>
</div>

<h3>Ospitare i Giochi vale +17 medaglie</h3>
<p>Per ogni paese ospitante, il delta tra le medaglie vinte in casa e la propria media storica è in media di <strong>+17.1 medaglie</strong> (escludendo i boicottaggi del 1980/1984), con <strong>p = 0.003</strong>, un risultato statisticamente solido. L'effetto combina investimenti pre-Giochi più alti, vantaggio del pubblico di casa, e assenza di stress da trasferta.</p>

<div class="full-width-chart-wrapper">
  <vegachart schema-url="{{site.baseurl}}/assets/charts/g6/nb2_host_effect.json" style="width: 100%; height: 100%"></vegachart>
</div>

---

## In sintesi

- La **spesa élite reale** spiega le medaglie molto meglio del PIL (r = 0.85-0.88 vs r = 0.58).
- **UK Sport** dimostra la relazione più solida in letteratura: r = 0.947, R² = 0.90 su sette cicli.
- **Ospitare i Giochi** vale in media +17.1 medaglie rispetto alla propria media storica (p = 0.003).
