---
layout: default
title: "Successo Maschile e Femminile"
subtitle: "Il medagliere olimpico letto attraverso il genere"
vega: true
---

{% include page-hero.html title="Successo maschile e femminile alle Olimpiadi" %}

In questa analisi scomponiamo il medagliere **per genere**, confrontando i risultati negli eventi maschili e femminili delle Olimpiadi estive dal 1964 al 2020. Le domande a cui vogliamo rispondere sono tre:

1. Come è cresciuto nel tempo il peso delle medaglie femminili?
2. Quali paesi costruiscono una parte rilevante del proprio medagliere sulle competizioni femminili?
3. I risultati maschili e femminili rispondono agli stessi fattori socio-economici?

I dati provengono dal dataset storico dei risultati olimpici (dettaglio atleta-evento e biografie degli atleti) incrociato con gli indicatori socio-economici della World Bank descritti nella pagina [Data Preparation]({{site.baseurl}}/data_preparation.html). Il genere di ogni evento è stato ricavato dal nome della gara (eventi *maschili*, *femminili* e *misti*), e per gli sport di squadra ogni squadra conta una sola medaglia.

## La crescita del medagliere femminile

Nel 1964 gli eventi femminili valevano circa il **21%** delle medaglie assegnate; a Tokyo 2020 la quota è arrivata al **48%**, con un programma ormai quasi paritario. In valore assoluto le medaglie femminili passano da 99 a 495 per edizione (+400%), mentre quelle maschili restano sostanzialmente stabili: la crescita complessiva dei Giochi è avvenuta soprattutto attraverso l'espansione del programma femminile.

<div style="height: 450px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/01_medaglie_per_genere_assolute.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

La stessa evoluzione, letta in percentuale, mostra un riequilibrio costante e regolare tra i due programmi: un cambiamento strutturale e programmatico, non un episodio legato a singole edizioni.

<div style="height: 450px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/02_medaglie_per_genere_percentuale.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

Isolando la quota femminile sul totale delle medaglie maschili e femminili, il percorso verso la parità è ancora più evidente, con un'accelerazione tra la fine degli anni '80 e il 2000.

<div style="height: 420px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/03_quota_femminile_tempo.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

## Il successo femminile paese per paese

Concentrandoci sul periodo 2000–2020, quando il programma femminile è ormai maturo, emerge che gli **Stati Uniti** dominano entrambi i medaglieri — e sono anzi il paese con più medaglie femminili in assoluto (317, più delle 300 maschili). Ma l'equilibrio tra i due generi varia molto da paese a paese: alcuni medaglieri sono trainati dagli uomini, altri dalle donne.

<div style="height: 550px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/04_medagliere_paesi_genere_2000_2020.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

Il confronto diretto tra medaglie maschili e femminili rende visibile questa diversità. Nel grafico ogni punto è un paese: la diagonale tratteggiata rappresenta la parità perfetta. I paesi **sopra la diagonale** vincono più negli eventi femminili che in quelli maschili — è il caso di Paesi Bassi, Romania e Giamaica, dove la quota femminile supera il 60% — mentre grandi potenze come Cina e Russia restano più spostate sul versante maschile.

<div style="height: 500px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/05_scatter_paesi_maschile_femminile.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

<p>Questi casi raccontano qualcosa che il PIL da solo non spiega: paesi con risorse limitate possono costruire un medagliere importante **specializzandosi in discipline femminili** in cui hanno tradizione e sistema sportivo (l'atletica giamaicana, la ginnastica rumena, il nuoto e il ciclismo olandesi). Il successo femminile appare quindi anche come una **scelta strategica di investimento**, non solo come conseguenza automatica della ricchezza di un paese.</p>

## Medaglie e indicatori socio-economici: uomini e donne rispondono agli stessi fattori?

<p> L'ultima parte dell'analisi mette in relazione le medaglie maschili e femminili con gli indicatori socio-economici del dataset di progetto (PIL, popolazione, urbanizzazione, aspettativa di vita, istruzione…), calcolando la correlazione di ciascun indicatore con quattro esiti: medaglie maschili, femminili, totali e quota femminile.</p>

<div style="height: 500px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/06_correlazioni_indicatori_heatmap.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>

<div>
<p> Il risultato più interessante è la **somiglianza** tra i due generi: il PIL assoluto (in scala logaritmica) è il predittore più forte per entrambi, con correlazioni quasi identiche (r ≈ 0,55 per il maschile, r ≈ 0,53 per il femminile), seguito dalla popolazione. Nessun indicatore mostra un comportamento radicalmente diverso tra i due medaglieri.</p>
</div>
<div style="height: 500px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/07_correlazioni_indicatori_barre.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

<p> Guardando la relazione nel dettaglio, la nuvola di punti PIL–medaglie ha la stessa forma per uomini e donne: i paesi poveri vincono poco in entrambi i programmi, mentre tra i paesi ricchi la variabilità è ampia — segno che la ricchezza è una condizione abilitante ma non sufficiente.</p>

<div style="height: 480px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/08_scatter_pil_medaglie_genere.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

<p> Lo stesso vale per la popolazione, che correla con il medagliere meno del PIL (r ≈ 0,4) ma sempre in modo simile per i due generi.</p>

<div style="height: 480px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano/09_scatter_popolazione_medaglie_genere.json" style="width: 100%; height: 100%"></vegachart>
</div>

<br/>

## In sintesi

- Dal 1964 al 2020 la quota femminile del medagliere è passata dal **21% al 48%**, di pari passo con la crescita della partecipazione delle atlete (dal 13% al 48% delle delegazioni).
- Gli **USA** dominano entrambi i medaglieri, ma diversi paesi (Paesi Bassi, Romania, Giamaica) costruiscono la maggioranza del proprio successo sugli eventi femminili.
- Gli indicatori socio-economici — PIL in testa — spiegano il successo olimpico **allo stesso modo per uomini e donne**: il genere non appare come un fattore limitante strutturale, quanto piuttosto una dimensione su cui i paesi scelgono (o meno) di investire.

### Nota metodologica

Il genere degli eventi è ricavato dal parsing testuale del nome della gara, con possibili imprecisioni sui casi ambigui; gli eventi misti sono tenuti separati e non redistribuiti. Le correlazioni presentate sono descrittive e non implicano relazioni causali.
