---
layout: default
title: "PIL, storico e boicottaggi"
subtitle: "Cosa spiega (e cosa non spiega) il medagliere olimpico"
vega: true
---

{% include page-hero.html %}

<p style="color:#666;font-size:14px;margin-top:-8px;margin-bottom:1.5rem;">Autore: Gianni Coia</p>

**Ogni medaglia ha una storia economica alle spalle — ma non solo.** Quanto conta davvero la ricchezza di un paese nel determinare il suo medagliere olimpico? Meno di quanto sembri, e in un modo diverso da quello che ci si aspetterebbe. In questa pagina costruiamo un modello predittivo, verifichiamo cosa guarda davvero per prevedere, misuriamo l'effetto di giocare in casa, e isoliamo gli episodi in cui la storia — non l'economia — ha deciso il podio.

## Tre famiglie di nazioni olimpiche

Con una tecnica di clustering (K-Means) i 220 paesi del dataset, osservati in ciascuna delle 15 edizioni dal 1964 al 2020, si raggruppano naturalmente in tre profili socio-economici. Il clustering è costruito su quattro variabili economico-demografiche (PIL, PIL pro capite, popolazione e la loro interazione), trasformate in logaritmo per correggere le forti asimmetrie tipiche di queste grandezze e poi standardizzate. Il numero di gruppi (k=3) è stato scelto confrontando il Silhouette Score su diverse ipotesi: k=3 ottiene 0,378, molto vicino al massimo assoluto (k=2, 0,380), ma offre una lettura socio-economica più ricca, perché distingue le economie emergenti dalle nazioni minori invece di accorparle in un unico blocco "non grandi potenze".

- **Le Grandi Potenze Olimpiche** — PIL alto e popolazione ampia (USA, Cina, Germania, Francia, Italia, Australia, ma anche India, Brasile ed Egitto per pura scala economica e demografica). Dominano il medagliere in modo sistematico: possono permettersi infrastrutture sportive su larga scala e hanno un ampio bacino di atleti tra cui scegliere. PIL medio ~$494 miliardi, Score medio 20,43 su 863 osservazioni.
- **Le Economie Emergenti** — grandi popolazioni ma reddito pro capite basso (~$993 pro capite contro $6,8 miliardi di PIL aggregato). Il potenziale demografico c'è, ma raramente si trasforma in medaglie per mancanza di investimenti strutturati: Score medio 1,58 su 1.062 osservazioni. È il gruppo più interessante: al suo interno si nascondono le storie di maggiore efficienza, come vedremo tra poco.
- **Le Nazioni Minori** — spesso benestanti a livello individuale (pensiamo a Islanda o Lussemburgo: PIL pro capite più alto dei tre gruppi, $11.764), ma con una popolazione media di appena 311mila abitanti — troppo poco per costruire un sistema sportivo competitivo su più discipline. Score medio 0,12 su 694 osservazioni.

Il messaggio di fondo: **i dati non dividono il mondo in "ricchi che vincono" e "poveri che perdono".** Dividono il mondo in sistemi sportivi con le risorse per competere su larga scala, e sistemi che devono fare di più con meno — e alcuni, come vedremo, ci riescono benissimo.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Gianni/pil_vs_medaglie.json" style="width: 100%; height: 100%"></vegachart>
</div>
<div style="font-size: 12px; color: #666; margin-bottom: 1.5rem;">Ogni punto è una coppia nazione-edizione, colorata per cluster e con opacità legata all'anno (più opaco = più recente). A destra, le nazioni con lo Score medio più alto (con almeno 3 edizioni disputate) nell'area selezionata a sinistra — trascina un rettangolo sullo scatter per filtrare la classifica, usa la rotellina per zoomare.</div>

**Nota:** due casi non compaiono nella classifica pur avendo punteggi altissimi — Unified Team (le ex repubbliche sovietiche riunite nel 1992) e ROC (la Russia nel 2020, sotto squalifica per doping di stato, competendo sotto bandiera neutra). Entrambe hanno gareggiato una sola volta: la loro "media" coinciderebbe col picco di quell'unica edizione, scavalcando nazioni come gli Stati Uniti che mediano su 15 edizioni. Non è un errore nei dati — l'entità storica è reale — ma la metrica "media" diventa fuorviante per chi ha pochissime partecipazioni. Per questo la classifica richiede almeno 3 edizioni disputate; Unified Team e ROC restano comunque visibili come singoli punti nello scatter.

## Un modello che prova a prevedere il medagliere

Prima di guardare al risultato, vale la pena farsi una domanda scomoda: perché costruire un modello complesso, se poi il verdetto è "guarda cosa la nazione aveva già vinto"? La risposta è che il modello non parte da questa idea — la mette alla prova insieme a molte altre variabili (PIL, popolazione, aspettativa di vita, urbanizzazione e altre), lasciando ai dati il compito di decidere quale conta di più. Ed è proprio questo confronto rigoroso — non un'intuizione, non una scorciatoia — a rivelare che lo storico recente pesa quasi il **70%** su tutte le altre variabili messe insieme.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Gianni/feature_importance_shap.json" style="width: 100%; height: 100%"></vegachart>
</div>

Il modello non si limita a confermare un'ipotesi ovvia: la misura, la quantifica, e mostra esattamente dove le altre variabili tornano protagoniste — nel restante 32% della varianza (R²=0,68, la stima più robusta), dove entrano in gioco efficienza, scelte politiche ed eventi storici. Il messaggio di fondo non è "bastava guardare l'anno prima": è che **le Olimpiadi non si vincono in quattro anni** — si vincono costruendo, in decenni, un sistema che continua a generare risultati simili edizione dopo edizione. I sistemi sportivi nazionali cambiano lentissimamente: infrastrutture, allenatori e federazioni non si costruiscono (né si smontano) in quattro anni.

### Se è solo storia, perché contano ancora PIL e popolazione?

Togliendo del tutto le feature di lag dal modello, l'R² scende da 0,80 a 0,69 — cala, ma resta comunque alto. Se il modello stesse solo "ripetendo" il passato, senza lag crollerebbe quasi a zero; invece PIL e popolazione da soli spiegano ancora circa il 69% della varianza.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Gianni/lag_vs_senza_lag.json" style="width: 100%; height: 100%"></vegachart>
</div>

Il lag cattura l'**inerzia** del sistema, mentre PIL e indicatori strutturali catturano il **potenziale** che spiega perché quell'inerzia esiste. La differenza si vede soprattutto per una nazione debuttante, o che rientra dopo un'assenza, dove il lag non è disponibile e il modello deve affidarsi al PIL.

## Giocare in casa conta, eccome

Nel Random Forest la variabile "nazione ospitante" pesa pochissimo (0,4%) — il suo effetto è in gran parte già assorbito dal lag, dato che le nazioni ospitanti tendono a essere già forti nelle edizioni precedenti a quella di casa. Ma questo non significa che l'effetto non esista: per verificarlo in modo indipendente dal modello, è stato fatto un confronto diretto, nazione per nazione, tra lo Score ottenuto nell'edizione da host e la media storica della stessa nazione nelle altre edizioni.

Su 12 nazioni che hanno ospitato i Giochi dal 1964 a oggi, **11 fanno meglio da host**, con una differenza media di **+48,5 punti di Score**. La Cina guida la classifica con Pechino 2008 (+136,4 rispetto alla propria media storica), seguita dagli Stati Uniti (+115,0) e dalla Gran Bretagna a Londra 2012 (+83,1). L'unica eccezione è il Canada, leggermente sotto la propria media anche nell'edizione di casa (-11,7).

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Gianni/host_effect.json" style="width: 100%; height: 100%"></vegachart>
</div>

## Quando il modello sbaglia, spesso è la storia a spiegarlo

Qui entra la parte più curiosa dell'analisi. Guardando dove il modello sbaglia di più — le nazioni che vincono molto più o molto meno di quanto le loro risorse economiche farebbero pensare — emergono storie molto diverse tra loro.

**Efficienza vera, a parità di risorse.** Guardando al rapporto tra medaglie e PIL (una misura diversa dai residui del modello, di cui parliamo tra un attimo), alcuni paesi convertono risorse limitate in risultati sproporzionati: Kenya ed Etiopia nell'atletica, la Giamaica nello sprint, Cuba nel pugilato. La spiegazione più plausibile — coerente con quello che si legge nella letteratura sportiva, anche se i nostri dati non permettono di dimostrarlo in modo diretto — è la specializzazione estrema in poche discipline ad alta resa, invece di provare a competere su tutti i fronti.

**Le sorprese più grandi del modello, invece, raccontano un'altra storia.** I residui del Random Forest — la differenza tra medaglie reali e previste — non premiano le piccole nazioni efficienti (restano su numeri troppo piccoli per generare un residuo grande in assoluto), ma le transizioni storiche: sistemi sportivi enormi che cambiano bandiera senza perdere le proprie infrastrutture.

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:13px;">
<tr style="background:#1b2140;color:white;"><th style="padding:6px 8px;text-align:left;">Nazione</th><th style="padding:6px 8px;text-align:left;">Anno</th><th style="padding:6px 8px;text-align:right;">Reali</th><th style="padding:6px 8px;text-align:right;">Previste</th><th style="padding:6px 8px;text-align:right;">Residuo</th></tr>
<tr style="background:#f7f7f7;"><td style="padding:6px 8px;">ROC</td><td style="padding:6px 8px;">2020</td><td style="padding:6px 8px;text-align:right;">139,0</td><td style="padding:6px 8px;text-align:right;">13,7</td><td style="padding:6px 8px;text-align:right;">+125,3</td></tr>
<tr><td style="padding:6px 8px;">Federazione Russa</td><td style="padding:6px 8px;">1996</td><td style="padding:6px 8px;text-align:right;">136,0</td><td style="padding:6px 8px;text-align:right;">23,5</td><td style="padding:6px 8px;text-align:right;">+112,5</td></tr>
<tr style="background:#f7f7f7;"><td style="padding:6px 8px;">Germania</td><td style="padding:6px 8px;">1964</td><td style="padding:6px 8px;text-align:right;">92,0</td><td style="padding:6px 8px;text-align:right;">22,4</td><td style="padding:6px 8px;text-align:right;">+69,6</td></tr>
<tr><td style="padding:6px 8px;">Italia</td><td style="padding:6px 8px;">1984</td><td style="padding:6px 8px;text-align:right;">66,0</td><td style="padding:6px 8px;text-align:right;">16,3</td><td style="padding:6px 8px;text-align:right;">+49,7</td></tr>
<tr style="background:#f7f7f7;"><td style="padding:6px 8px;">Ungheria</td><td style="padding:6px 8px;">1992</td><td style="padding:6px 8px;text-align:right;">64,0</td><td style="padding:6px 8px;text-align:right;">29,5</td><td style="padding:6px 8px;text-align:right;">+34,5</td></tr>
</table>

Il caso più estremo è la Russia ai Giochi di casa del 2020, in gara sotto bandiera neutra (ROC) per la squalifica da doping di stato, ma con l'intero apparato sportivo ereditato dalla Federazione Russa: **+125,3 medaglie** rispetto al previsto. Al secondo posto, la Federazione Russa nel 1996 — la prima Olimpiade dopo la dissoluzione dell'URSS, con poco storico proprio ma un sistema sovietico ereditato integralmente: **+112,5**. Non sono "efficienza" nel senso di Kenya o Cuba: sono transizioni geopolitiche che il modello non ha modo di rappresentare.

**Storie di politica, non di sport.** All'estremo opposto, i residui più negativi in assoluto corrispondono esattamente alle due edizioni boicottate della Guerra Fredda. Il modello prevede circa **54 medaglie per la Bulgaria nel 1984** e **47 per il Giappone nel 1980** — sulla carta, paesi con le risorse per arrivare a quei numeri. Nella realtà, entrambi i paesi tornarono a casa **a zero medaglie**. Non per un crollo improvviso del loro sistema sportivo, ma perché semplicemente **non parteciparono**: il 1980 e il 1984 sono le due edizioni dei boicottaggi incrociati della Guerra Fredda (Mosca 1980, boicottata dagli USA e alleati; Los Angeles 1984, boicottata dall'URSS e blocco sovietico).

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:13px;">
<tr style="background:#1b2140;color:white;"><th style="padding:6px 8px;text-align:left;">Nazione</th><th style="padding:6px 8px;text-align:left;">Anno</th><th style="padding:6px 8px;text-align:right;">Reali</th><th style="padding:6px 8px;text-align:right;">Previste</th><th style="padding:6px 8px;text-align:right;">Residuo</th></tr>
<tr style="background:#f7f7f7;"><td style="padding:6px 8px;">Bulgaria</td><td style="padding:6px 8px;">1984</td><td style="padding:6px 8px;text-align:right;">0,0</td><td style="padding:6px 8px;text-align:right;">53,6</td><td style="padding:6px 8px;text-align:right;">−53,6</td></tr>
<tr><td style="padding:6px 8px;">Giappone</td><td style="padding:6px 8px;">1980</td><td style="padding:6px 8px;text-align:right;">0,0</td><td style="padding:6px 8px;text-align:right;">46,5</td><td style="padding:6px 8px;text-align:right;">−46,5</td></tr>
<tr style="background:#f7f7f7;"><td style="padding:6px 8px;">Canada</td><td style="padding:6px 8px;">1988</td><td style="padding:6px 8px;text-align:right;">18,0</td><td style="padding:6px 8px;text-align:right;">58,5</td><td style="padding:6px 8px;text-align:right;">−40,5</td></tr>
<tr><td style="padding:6px 8px;">Federazione Russa</td><td style="padding:6px 8px;">2008</td><td style="padding:6px 8px;text-align:right;">121,0</td><td style="padding:6px 8px;text-align:right;">152,3</td><td style="padding:6px 8px;text-align:right;">−31,3</td></tr>
<tr style="background:#f7f7f7;"><td style="padding:6px 8px;">Regno Unito</td><td style="padding:6px 8px;">1996</td><td style="padding:6px 8px;text-align:right;">25,0</td><td style="padding:6px 8px;text-align:right;">44,0</td><td style="padding:6px 8px;text-align:right;">−19,0</td></tr>
</table>

Gli altri under-performer in tabella (Canada 1988, Russia 2008, Gran Bretagna 1996) sono invece più vicini al concetto di sotto-performance genuina: grandi sistemi sportivi con PIL elevato ma, in quella specifica edizione, un rendimento inferiore al potenziale stimato dal modello — non una scusa storica, semplicemente un'edizione sotto tono.

Un terzo episodio, meno estremo ma comunque rilevante, è il boicottaggio africano di Montreal 1976 (circa 30 paesi assenti in protesta contro la partecipazione della Nuova Zelanda, il cui rugby aveva giocato nel Sudafrica dell'apartheid). Il quadro completo dei tre boicottaggi del periodo — 1976, 1980, 1984 — è approfondito nella pagina "Successo Maschile e Femminile", dove la stessa perturbazione viene letta anche dal lato dell'equilibrio di genere nel medagliere.

Lo stesso fenomeno si vede, in modo speculare, nel grafico qui sotto: la correlazione tra PIL e medaglie, che in quasi tutte le edizioni resta sopra 0,8, crolla esattamente nel 1980 — l'unico anno in cui la politica, non l'economia, ha deciso chi era sul podio. Il 1976 non lascia lo stesso segno: le nazioni assenti quell'anno erano già ai margini di entrambe le scale (PIL basso, medaglie quasi nulle), mentre il 1980 ha escluso proprio le potenze economiche e sportive (USA, Germania Ovest, Giappone) — gli stessi punti che determinano la relazione.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Gianni/correlazione_pil_medaglie_nel_tempo.json" style="width: 100%; height: 100%"></vegachart>
</div>

Un modello economico, per definizione, non può sapere che una squadra è rimasta a casa per un embargo diplomatico. È uno dei limiti più onesti e più interessanti di tutta l'analisi.

## Un secondo modello: in che fascia finirà una nazione?

Accanto alla previsione puntuale (un numero di medaglie), è stato costruito anche un classificatore più intuitivo, che stima la fascia di successo. Le quattro fasce non hanno tutte la stessa ampiezza, ed è voluto: sono soglie scelte per significato, non per bilanciare la larghezza numerica.

<table style="border-collapse:collapse;width:100%;margin:16px 0;font-size:14px;">
<tr style="background:#1b2140;color:white;"><th style="padding:8px;text-align:left;">Fascia</th><th style="padding:8px;text-align:left;">Intervallo</th><th style="padding:8px;text-align:left;">Ampiezza</th></tr>
<tr style="background:#f7f7f7;"><td style="padding:8px;">Nessuna medaglia</td><td style="padding:8px;">esattamente 0</td><td style="padding:8px;">1 valore</td></tr>
<tr><td style="padding:8px;">Successo limitato</td><td style="padding:8px;">1–5</td><td style="padding:8px;">5 medaglie</td></tr>
<tr style="background:#f7f7f7;"><td style="padding:8px;">Successo medio</td><td style="padding:8px;">6–20</td><td style="padding:8px;">15 medaglie</td></tr>
<tr><td style="padding:8px;">Successo elevato</td><td style="padding:8px;">21+</td><td style="padding:8px;"><strong>aperta, senza limite superiore</strong></td></tr>
</table>

L'accuracy misura semplicemente la percentuale di nazioni-edizione classificate nella fascia corretta: il modello raggiunge **0,824**. Il numero di confronto — la **baseline** — è l'accuracy che si otterrebbe prevedendo sempre la fascia più numerosa ("Nessuna medaglia", che da sola copre il 66,3% delle osservazioni) senza usare alcuna informazione: 0,663. Il modello migliora quindi la baseline di oltre 16 punti percentuali.

<div class="full-width-chart-wrapper">
<vegachart schema-url="{{site.baseurl}}/assets/charts/Gianni/accuracy_vs_baseline_fasce.json" style="width: 100%; height: 100%"></vegachart>
</div>

Questa disparità di ampiezza ha una conseguenza pratica diretta: vicino ai bordi stretti (5→6, 20→21) un errore piccolissimo del modello di regressione — una sola medaglia — fa scavalcare la fascia, mentre dentro la fascia aperta "Successo elevato" un errore enorme (90 medaglie previste contro 180 reali) non conta affatto come errore di classificazione: sono comunque entrambi "elevato". L'accuracy diventa quindi molto sensibile agli errori piccoli vicino ai confini stretti, e cieca agli errori grandi dentro la fascia aperta.

La direzione dell'errore segue quella del modello: se il Random Forest **sovrastima** lo Score di una nazione, il rischio è classificarla in una fascia **superiore** a quella reale; se lo **sottostima**, il rischio è una fascia **inferiore**. È per questo che le due metriche — R² del modello di regressione e accuracy del classificatore — non sono direttamente confrontabili: condividono la stessa fonte di errore ma la misurano in modo diverso.

## Cosa manca ancora

Un'estensione renderebbe il quadro più completo: un indicatore esplicito di boicottaggio/non partecipazione, emerso proprio da questa analisi, che eviterebbe di scambiare un evento politico per un fallimento sportivo.

## In sintesi

Il successo olimpico è per circa il 68% spiegabile da fattori strutturali misurabili — PIL, demografia, storico sportivo — ma il predittore singolarmente più forte non è la ricchezza presente, è quella accumulata in decenni di sistema sportivo. Il PIL crea il potenziale; lo storico recente decide chi lo attiva; i residui rivelano dove efficienza, scelte ed eventi storici fanno la differenza tra realizzarlo o sprecarlo — dal +125,3 della Russia ai Giochi di casa del 2020 (in gara come ROC) al −53,6 della Bulgaria nel 1984, assente per boicottaggio nonostante un potenziale stimato di oltre 50 medaglie. Il valore del progetto non sta in un singolo numero, ma nell'aver dimostrato in modo convergente queste tre tesi, ciascuna supportata da più analisi indipendenti tra loro.
