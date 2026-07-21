---
layout: default
title: "Successo Maschile e Femminile 3"
subtitle: "La crescita dello sport femminile nel medagliere olimpico, 1964-2020"
vega: true
---

{% include page-hero.html title="Successo Maschile e Femminile" %}

In questa analisi raccontiamo come è cambiato il peso dello sport femminile alle Olimpiadi estive dal **1964 al 2020**, rispondendo a tre domande:

1. Come sono cresciuti nel tempo la partecipazione e il peso delle medaglie femminili rispetto a quelli maschili?
2. Quali paesi costruiscono una parte rilevante del proprio medagliere sulle competizioni femminili?
3. I risultati maschili e femminili rispondono agli stessi fattori socio-economici?

I dati provengono dal dataset storico dei risultati olimpici (dettaglio atleta-evento e biografie degli atleti) incrociato con la **versione corretta** del dataset degli indicatori socio-economici World Bank, rigenerato con la mappatura esplicita dei codici NOC↔ISO3 (niente righe duplicate, ogni paese con i propri indicatori). Il genere di ogni evento è ricavato dal nome della gara (eventi *maschili*, *femminili* e *misti*), e negli sport di squadra ogni squadra conta una sola medaglia. La ricostruzione del medagliere coincide **perfettamente** con quello ufficiale (r=1.0, scarto nullo).

## La partecipazione femminile

Nel 1964 le donne erano circa il **13%** dei partecipanti; a Tokyo 2020 quasi il **48%**. La crescita è continua, senza inversioni, e accelera dagli anni '80. Il numero di atleti uomini è più o meno stabile dagli anni '90.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano3/01_partecipazione_e_quota.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

## L'evoluzione del medagliere

La quota di medaglie femminili passa dal **21%** del 1964 a oltre il **48%** del 2020, e la sua curva ricalca quella della partecipazione: quando il programma offre più gare femminili, arrivano più medaglie femminili. Gran parte della crescita del medagliere femminile è quindi la crescita delle **opportunità di gara** decisa dal CIO, più che un cambiamento nel rendimento delle atlete. La flessione intorno al 1976-1984 riflette anche i boicottaggi, di cui parliamo più sotto.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano3/02_medagliere_e_quota.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

## I paesi che dipendono di più dalle medaglie femminili

Aggregando l'intero periodo 1964-2020 e considerando solo i paesi con almeno 30 medaglie di genere, i paesi oltre la linea del 50% hanno vinto **più medaglie con le donne che con gli uomini** in oltre mezzo secolo di Giochi. Il gruppo di testa è eterogeneo: potenze dello sprint come la **Giamaica** (62,5%), paesi con sistemi sportivi statali che hanno investito presto sullo sport femminile (Cina, Romania, ex DDR) e paesi occidentali come Paesi Bassi e Canada. Questa eterogeneità è già un indizio per la terza domanda: non sembra esserci un unico profilo socio-economico che produce un medagliere "femminile".

<div style="height: 460px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano3/03_top15_quota_femminile_paesi.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

### Dove sono USA e Russia?

Un'assenza che colpisce: le due superpotenze del medagliere non compaiono nella Top 15. Il motivo è la **metrica** — la classifica ordina per *quota* femminile, non per numero di medaglie — e le grandi potenze storiche restano appena sotto la soglia di ingresso (43,3%):

| Posizione | NOC | Medaglie M | Medaglie F | Quota femminile |
|-----------|-----|------------|------------|-----------------|
| 10ª | ROC | 35 | 32 | 47,8% |
| 16ª | Russia (RUS) | 245 | 177 | 41,9% |
| 17ª | USA | 832 | 584 | 41,2% |
| 31ª | Squadra Unificata (EUN) | 75 | 37 | 33,0% |
| 40ª | URSS (URS) | 507 | 191 | 27,4% |

Due fattori spiegano il risultato. Il primo è l'**effetto storico del programma gare**: USA e URSS vincono moltissimo fin dal 1964, quando gli eventi femminili valevano solo il 21% delle medaglie, e quel bottino degli anni '60-'80 — strutturalmente sbilanciato sul maschile — abbassa la quota aggregata sull'intero periodo. Non a caso, nel periodo 2000-2020 (grafico successivo) gli USA hanno *più* medaglie femminili che maschili.

Il secondo è la frammentazione dei **NOC storici**: il dataset segue il medagliere ufficiale del CIO, in cui ogni Comitato Olimpico Nazionale è un'entità distinta. La "Russia" è quindi spezzata su quattro sigle: **URS** (l'Unione Sovietica, fino al 1988), **EUN** (la *Squadra Unificata* delle 12 ex repubbliche sovietiche a Barcellona 1992), **RUS** (la Federazione Russa, dal 1996) e **ROC** (il *Russian Olympic Committee* di Tokyo 2020, quando la Russia era squalificata per il doping di stato e i suoi atleti gareggiarono senza bandiera né inno). Un pezzo di "Russia" in Top 15 c'è: ROC, che però rappresenta la sola edizione 2020. Lo stesso vale per la Germania (GER, FRG, GDR, EUA).

## Il medagliere dei principali paesi, 2000-2020

Restringendo lo sguardo al periodo recente (2000-2020, quando il programma femminile è ormai ampio), l'equilibrio di genere tra le grandi potenze sportive non è affatto uniforme. Gli **Stati Uniti**, primo medagliere del periodo, hanno vinto **più medaglie femminili che maschili** (317 contro 300); Cina, Paesi Bassi e Canada superano nettamente il 50% femminile e il Giappone è esattamente alla pari. All'estremo opposto, paesi come Cuba, Italia e Francia costruiscono ancora circa due terzi del medagliere sulle gare maschili. Essere una potenza olimpica, quindi, non implica un medagliere equilibrato.

<div style="height: 500px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano3/06_medagliere_principali_paesi_2000_2020.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

## Uomini e donne rispondono agli stessi fattori socio-economici?

Mettiamo in relazione le medaglie con gli indicatori World Bank su un panel paese-edizione (3.126 righe, una per paese-edizione) che include anche i paesi senza medaglie, usando come misura di successo log(1 + medaglie) per attenuare il peso dei paesi dominanti. Con il dataset corretto anche le squadre russe EUN (1992) e ROC (2020) entrano nell'analisi con medaglie e indicatori insieme, mentre l'URSS resta dichiaratamente senza indicatori (la World Bank non copre l'Unione Sovietica). Gli indicatori di **dimensione** — PIL assoluto e popolazione — sono i più associati al numero di medaglie, e questo vale per entrambi i generi: nel grafico, il punto maschile e quello femminile di ogni indicatore sono quasi sovrapposti (differenza media assoluta di appena 0,02). La crescita del PIL è invece scorrelata: vince chi è grande, non chi cresce in fretta.

<div style="height: 400px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano3/04_correlazioni_indicatori_per_genere.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

Guardando nel dettaglio la relazione più nota — quella con la ricchezza — le due rette di regressione sono quasi parallele e quasi sovrapposte: a parità di PIL pro capite, un paese tende a vincere un numero simile di medaglie maschili e femminili. La risposta qualitativa alla terza domanda è quindi: **sì, i due medaglieri rispondono sostanzialmente agli stessi fattori socio-economici**. Ciò che gli indicatori *non* spiegano è la variabilità tra paesi simili vista sopra: lì contano probabilmente politiche sportive, tradizioni e fattori culturali che il World Bank non misura.

<div style="height: 480px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/stefano3/05_scatter_pil_pro_capite_regressione.json" style="width: 100%; height: 100%"></vegachart>
</div>
<p>------------</p>
<br/>

## I boicottaggi: una perturbazione da tenere presente

Tre edizioni del periodo analizzato sono state segnate da boicottaggi di massa. Il numero esatto di atleti esclusi non è documentato in modo uniforme, quindi riportiamo il numero stimato di paesi coinvolti.

| Anno | Edizione | Motivo | Paesi coinvolti (stima) |
|------|----------|--------|-------------------------|
| 1976 | Montreal 1976 | Boicottaggio africano: protesta contro la presenza della Nuova Zelanda, il cui rugby aveva giocato nel Sudafrica dell'apartheid | ~30 (paesi africani, più Iraq e Guyana) |
| 1980 | Mosca 1980 | Boicottaggio guidato dagli USA in risposta all'invasione sovietica dell'Afghanistan | ~60-65 (tra cui USA, Germania Ovest, Giappone, Canada, Cina) |
| 1984 | Los Angeles 1984 | Boicottaggio del blocco sovietico, ufficialmente per motivi di sicurezza, di fatto in risposta al 1980 | 14 (tra cui URSS, DDR, Cuba) |

I boicottaggi perturbano proprio le serie mostrate in questa pagina: nel 1980 e nel 1984 mancano dal medagliere blocchi interi di paesi, e alcuni di questi (URSS, DDR) erano tra i più forti proprio nello sport femminile. Le oscillazioni intorno al 1980-1984 vanno quindi lette con cautela: in parte non riflettono tendenze reali ma l'assenza forzata di alcuni paesi. È anche per questo che il confronto tra generi privilegia il periodo 2000-2020.

## In sintesi

- Dal 1964 al 2020 la quota femminile dei partecipanti è passata dal **13% al 48%** e quella delle medaglie dal **21% al 48%**: le due curve viaggiano insieme, segno che la crescita del medagliere femminile è soprattutto crescita delle opportunità di gara.
- Un gruppo eterogeneo di paesi (Giamaica, Cina, Romania, Paesi Bassi, Canada) ha vinto **più con le donne che con gli uomini**; tra le potenze recenti anche gli USA 2000-2020 hanno un medagliere a maggioranza femminile.
- Gli indicatori socio-economici — PIL e popolazione in testa — spiegano il successo olimpico **allo stesso modo per uomini e donne**; la composizione di genere del medagliere resta in gran parte non spiegata da questi indicatori, ed è probabilmente legata a scelte di investimento sportivo che i dati disponibili non misurano.

### Nota metodologica

Il genere degli eventi è ricavato dal parsing testuale del nome della gara; gli eventi misti sono tenuti separati e non redistribuiti. Le medaglie di squadra contano una volta per squadra; il medagliere ricostruito coincide esattamente con quello ufficiale del CIO. Gli indicatori provengono dalla versione corretta del dataset di progetto (mappatura NOC↔ISO3 esplicita, nessuna riga duplicata); le correlazioni presentate sono descrittive e non implicano relazioni causali, e alcuni indicatori hanno il 20-40% di valori mancanti (quelli con copertura peggiore sono stati esclusi).
