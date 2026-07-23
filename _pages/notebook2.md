---
layout: default
title: "Il prezzo dell'oro"
header_title: "Il prezzo dell'oro"
subtitle: "Oltre il PIL: quanto costa davvero vincere una medaglia olimpica?"
header_type: hero
header_img: "assets/images/img_olimpiadi.jpg"
vega: true
scrollama: true
custom_css: /assets/css/g6-charts.css
---

Le analisi esplorative hanno mostrato che il PIL totale correla con le medaglie (r = 0.58), ma lasciano aperta la domanda più importante: è il PIL in sé che produce medaglie, o è quello che ci si fa sopra — cioè quanto si investe direttamente nello sport élite? In questa sezione utilizziamo dati reali di spesa sportiva per rispondere.
{: .lead}

Le domande che guidano questa analisi:

1. La spesa sportiva élite spiega le medaglie meglio del PIL?
2. I paesi che aumentano i finanziamenti migliorano davvero i risultati nel ciclo successivo?
3. Quanto costa in media una medaglia olimpica — e chi è più efficiente?
4. Ospitare le Olimpiadi dà un vantaggio misurabile, e se sì quanto vale?

**Fonti:** SPLISS Tokyo 2020 (De Bosscher & Shibli, 2021) · SPLISS Paris 2024 (De Bosscher et al., 2024) · UK Sport Historical Funding 2000–2024 (dati ufficiali governo britannico).

---

{% include scrollytelling.html
  data_file="scrollama_nb2"
  chart_height="440px"
  desktop_chart_height="58vh"
  sticky_top="12vh"
  desktop_steps_padding_top="5vh"
  step_gap="95vh"
  last_step_gap="5vh"
  only_active_step_visible="false"
%}

---

## In sintesi

- La **spesa élite reale** spiega le medaglie con r = 0.85–0.88 (SPLISS), significativamente meglio del PIL (r = 0.58): misura direttamente il flusso di risorse verso lo sport di alto livello.
- UK Sport mostra la relazione più robusta disponibile: **r = 0.947, R² = 0.90** su sette cicli consecutivi — il 90% della varianza delle medaglie britanniche è spiegata dall'investimento.
- Il **costo per medaglia** varia enormemente: da €2.8M del Belgio a oltre €8M del Brasile. L'efficienza dell'allocazione conta quanto il volume totale di spesa.
- **Ospitare i Giochi** vale circa +16.6 medaglie rispetto alla propria media storica (p = 0.004).

### Nota metodologica

I dati SPLISS coprono solo 14–17 nazioni e due cicli: il campione è troppo piccolo per stime panel formali. L'effetto paese ospitante esclude i boicottaggi del 1980 e 1984 perché il delta riflette l'assenza dei rivali, non il vero vantaggio di campo.
