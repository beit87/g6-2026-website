---
layout: default
title: "La porta stretta dei poveri, il bivio dei ricchi"
subtitle: "Sessant'anni di Olimpiadi raccontano due storie sul denaro e lo sport — una di apertura, una di privilegio persistente"
---

{% include page-hero.html %}

**Ogni medaglia ha una storia economica alle spalle — ma è una storia che cambia a seconda di dove si guarda.** Questa analisi incrocia sessant'anni di Olimpiadi estive con il PIL pro capite dei paesi per rispondere a due domande diverse: quanto è difficile, oggi, entrare nel medagliere rispetto a sessant'anni fa? E, una volta entrati, il denaro decide anche *come* si vince — da soli o in squadra?

## La soglia che inganna

Nel 1964 il paese più povero a vincere una medaglia olimpica aveva un PIL pro capite di 77 dollari. Nel 2020, di 718 — quasi dieci volte tanto. È una lettura sbagliata. Nello stesso periodo, il PIL pro capite mediano di tutti i paesi del mondo è cresciuto di oltre 23 volte, da 266 a 6.247 dollari. Il pianeta si è arricchito molto più in fretta della soglia di ingresso al medagliere. Confrontare 77 dollari con 718 significa confrontare due epoche economiche diverse, non misurare la stessa barriera in due momenti.

<div style="position: relative; width: 100%; height: 280px; margin: 1.5rem 0;">
<canvas id="sogliaChart" role="img" aria-label="Grafico a barre che confronta, in dollari e scala logaritmica, la soglia di ingresso al medagliere olimpico con la mediana mondiale del PIL pro capite nel 1964 e nel 2020. 1964: soglia 77 dollari, mediana mondiale 266 dollari. 2020: soglia 718 dollari, mediana mondiale 6247 dollari.">Soglia di ingresso vs mediana mondiale del PIL pro capite: 1964 (soglia 77$, mediana 266$) e 2020 (soglia 718$, mediana 6.247$).</canvas>
</div>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">Scala logaritmica. La soglia è cresciuta di circa 9 volte tra il 1964 e il 2020, la mediana mondiale del PIL di oltre 23 volte: il mondo si è arricchito molto più in fretta della barriera di ingresso.</div>

La domanda giusta non è quanti dollari servano, ma dove si colloca il paese più povero capace di vincere, rispetto a tutti gli altri paesi di quello stesso anno. E qui la storia si ribalta: nel 1964 quel paese occupava il decimo percentile della ricchezza mondiale — povero, ma non ultimo. Nel 2004, e di nuovo nel 2016, il paese-soglia era letteralmente all'ultimo posto: il paese più povero del pianeta, quell'anno, ha vinto comunque una medaglia. Il trend è discendente e statisticamente solido: la regressione lineare del percentile sull'anno, su quindici edizioni dal 1964 al 2020, dà p = 0,0008.

<div style="position: relative; width: 100%; height: 280px; margin: 1.5rem 0;">
<canvas id="percentileChart" role="img" aria-label="Grafico a barre del percentile mondiale di ricchezza occupato dal paese-soglia in tre edizioni olimpiche. 1964: decimo percentile. 2004: zero, ultimo posto. 2016: zero, ultimo posto.">Percentile mondiale del paese-soglia: 1964 al decimo percentile, 2004 e 2016 all'ultimo posto (percentile zero).</canvas>
</div>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">Zero = il paese più povero al mondo quell'anno. Nel 2004 e nel 2016 il paese-soglia coincide letteralmente con il paese più povero del pianeta: la barriera di ingresso, misurata correttamente, si è quasi azzerata.</div>

> **Nel 2004 e nel 2016, il paese più povero a vincere una medaglia era, letteralmente, il paese più povero al mondo quell'anno.**

Le Olimpiadi, misurate correttamente, sono diventate più accessibili a chi ha meno risorse. Questo non significa che il denaro non conti: in ogni edizione dal 1964 al 2020 la correlazione tra PIL pro capite e medaglie vinte resta positiva e significativa, anche se modesta (un coefficiente tipicamente tra 0,18 e 0,33). E restare ricchi non basta comunque a garantirsi un posto sul podio — tra il 66% e l'85% dei paesi con PIL sopra la soglia, a seconda dell'edizione, torna comunque a casa senza medaglie.

## Il bivio: vincere insieme o vincere da soli

Partendo da questa analisi, può essere fatto un passo in avanti osservando la struttura dei paesi in un dato momento — si scopre che la stessa ricchezza che rende un'Olimpiade più aperta ai poveri produce, allo stesso tempo, una spaccatura molto netta a seconda dello sport.

Usando il dettaglio di ogni medaglia assegnata dal 1964 al 2016, abbiamo classificato ciascuna vittoria come "individuale" (un solo atleta) o "di squadra" (più atleti della stessa nazione, staffette comprese), e raggruppato 88 paesi con almeno cinque medaglie totali in profili distinti tramite K-Means. Il numero di gruppi non è stato fissato a priori: l'algoritmo lo sceglie automaticamente tra 2 e 6, selezionando quello con il miglior punteggio di silhouette (una misura di quanto i gruppi risultano ben separati). In questo caso la scelta è caduta su tre gruppi.

I "Misti" — grandi potenze sportive con programmi ampi e diversificati — vincono in modo bilanciato in entrambe le categorie e hanno il PIL pro capite medio più alto: 13.077 dollari. Gli "Specialisti squadra" li seguono, a 9.889 dollari. Gli "Specialisti individuale" — la cui intera produzione di medaglie arriva quasi solo da gare individuali, spesso di resistenza — hanno il PIL più basso: appena 6.991 dollari di media, e solo 2.444 dollari di mediana, segno che il gruppo include diverse economie molto povere.

<div style="position: relative; width: 100%; height: 280px; margin: 1.5rem 0;">
<canvas id="clusterChart" role="img" aria-label="Grafico a barre orizzontali del PIL pro capite medio dei tre cluster di paesi per profilo di vittoria olimpica. Misti: 13077 dollari. Specialisti squadra: 9889 dollari. Specialisti individuale: 6991 dollari, con mediana di 2444 dollari.">PIL pro capite medio per cluster: Misti 13.077$, Specialisti squadra 9.889$, Specialisti individuale 6.991$ (mediana 2.444$).</canvas>
</div>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">Ogni barra è un cluster K-Means di paesi con un profilo di vittoria simile. La mediana molto più bassa della media per gli "Specialisti individuale" indica che il gruppo include diverse economie molto povere accanto a qualche caso più ricco.</div>

> **I tre cluster non sono solo diversi nel modo di vincere: sono anche significativamente diversi nel PIL pro capite medio dei paesi che li compongono.**

Un test ANOVA sul PIL pro capite medio (in scala logaritmica, per non far pesare troppo i pochi paesi estremamente ricchi) conferma che questa differenza tra gruppi non è casuale (p = 0,007). E guardando i singoli paesi invece dei gruppi, la correlazione di Spearman tra quota di medaglie individuali e PIL pro capite è negativa e robusta (ρ = −0,422, p = 0,001): più un paese è povero, più le sue medaglie dipendono quasi interamente da singoli fuoriclasse individuali; più è ricco, più riesce a competere anche — e soprattutto — negli sport di squadra.

I tre grafici seguenti mostrano lo stesso risultato a livello di singolo paese, non solo di media di gruppo.
<vegachart schema-url="{{site.baseurl}}/assets/charts/chart_scatter_cluster.json"></vegachart>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">Ogni punto è un paese. L'asse orizzontale è la quota di medaglie individuali, l'asse verticale il volume totale di medaglie (scala log); il colore indica il cluster K-Means.</div>

<vegachart schema-url="{{site.baseurl}}/assets/charts/chart_pil_per_cluster.json"></vegachart>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">Distribuzione completa del PIL pro capite in ciascun cluster (non solo la media): la "scatola" mostra quanto varia la ricchezza dei paesi all'interno dello stesso profilo di vittoria.</div>

<vegachart schema-url="{{site.baseurl}}/assets/charts/chart_quota_vs_pil.json"></vegachart>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">La stessa correlazione di Spearman (ρ = −0,422) vista paese per paese, con la linea tratteggiata a indicare il trend di regressione: più PIL, meno dipendenza dalle medaglie individuali.</div>

## Perché succede: la stessa causa, vista da due angolazioni

Non è un caso che il paese-soglia della prima analisi sia quasi sempre l'Etiopia — mezzofondo, disciplina individuale — e mai un paese che vince ori a calcio o pallavolo. Costruire un programma di squadra competitivo richiede infrastrutture, campionati giovanili, allenatori, decenni di investimento continuo: risorse che solo le economie più solide possono sostenere su larga scala. Una vittoria individuale richiede "solo" un atleta eccezionale, capace di emergere anche in un contesto povero di risorse strutturali.

Ecco perché la soglia economica per entrare nel medagliere si è progressivamente abbassata nel tempo, mentre allo stesso tempo i paesi restano nettamente divisi per PIL a seconda del tipo di sport in cui vincono: sono due facce dello stesso fenomeno. La porta che si è allargata nel tempo è, specificamente, quella dello sport individuale. Quella dello sport di squadra resta socchiusa a chi può permettersi di costruirci sopra un intero sistema.

## In una frase

Il PIL di un paese non decide solo se vincerà una medaglia olimpica. Decide, più silenziosamente, attraverso quale porta ci arriverà — e i dati di sessant'anni di Giochi dicono che quella porta si sta allargando solo per chi gioca da solo.

*Metodologia: analisi su dati World Bank (PIL pro capite, NY.GDP.PCAP.CD) incrociati con il medagliere IOC e il dataset "120 Years of Olympic History" (dettaglio medaglia per atleta, sport ed evento). Olimpiadi estive, 1964–2020 per la soglia di ingresso (calcolata edizione per edizione, con relativizzazione alla distribuzione mondiale del PIL di quell'anno); 1964–2016 per la classificazione squadra/individuale e il clustering K-Means, limitate dalla disponibilità dei dati a livello di singolo evento-medaglia. Paesi inclusi nel clustering: almeno 5 medaglie totali nel periodo. Numero di cluster scelto automaticamente (2-6) col punteggio di silhouette. Soglia di significatività statistica: p<0,05.*

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
(function() {
  new Chart(document.getElementById('sogliaChart'), {
    type: 'bar',
    data: {
      labels: ['1964', '2020'],
      datasets: [
        {
          label: 'Soglia di ingresso (USD)',
          data: [77, 718],
          backgroundColor: '#eb6834',
          borderRadius: 4
        },
        {
          label: 'Mediana mondiale del PIL (USD)',
          data: [266, 6247],
          backgroundColor: '#2a78d6',
          borderRadius: 4
        }
      ]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { position: 'bottom', labels: { boxWidth: 10, font: { size: 11 } } },
        tooltip: {
          callbacks: {
            label: function(ctx) { return ctx.dataset.label + ': ' + ctx.parsed.y + ' USD'; }
          }
        }
      },
      scales: {
        y: {
          type: 'logarithmic',
          title: { display: true, text: 'USD (scala log)' },
          grid: { color: '#e1e0d9' }
        },
        x: { grid: { display: false } }
      }
    }
  });

  new Chart(document.getElementById('percentileChart'), {
    type: 'bar',
    data: {
      labels: ['1964', '2004', '2016'],
      datasets: [{
        label: 'Percentile mondiale del paese-soglia',
        data: [10, 0, 0],
        backgroundColor: ['#2a78d6', '#e34948', '#e34948'],
        borderRadius: 4
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function(ctx) {
              return ctx.parsed.y === 0
                ? 'Ultimo posto al mondo quell\'anno'
                : ctx.parsed.y + 'esimo percentile di ricchezza mondiale';
            }
          }
        }
      },
      scales: {
        y: {
          min: 0,
          max: 20,
          title: { display: true, text: 'Percentile (0 = paese più povero al mondo)' },
          grid: { color: '#e1e0d9' }
        },
        x: { grid: { display: false } }
      }
    }
  });

  new Chart(document.getElementById('clusterChart'), {
    type: 'bar',
    data: {
      labels: ['Misti', 'Specialisti squadra', 'Specialisti individuale'],
      datasets: [{
        label: 'PIL pro capite medio (USD)',
        data: [13077, 9889, 6991],
        backgroundColor: ['#2a78d6', '#eb6834', '#1baf7a'],
        borderRadius: 4
      }]
    },
    options: {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: { display: false },
        tooltip: {
          callbacks: {
            label: function(ctx) {
              var extra = ctx.label === 'Specialisti individuale' ? ' (mediana 2.444 USD)' : '';
              return ctx.parsed.x + ' USD' + extra;
            }
          }
        }
      },
      scales: {
        x: {
          title: { display: true, text: 'PIL pro capite medio (USD)' },
          grid: { color: '#e1e0d9' }
        },
        y: { grid: { display: false } }
      }
    }
  });
})();
</script>
