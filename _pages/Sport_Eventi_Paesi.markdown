---
layout: default
title: "Il DNA sportivo dei Paesi"
subtitle: "Sport, eventi e Paesi attraverso il medagliere olimpico"
vega: true
---

{% include page-hero.html title="Il DNA sportivo dei Paesi" %}

Ogni quattro anni un nuovo medagliere olimpico si aggiunge alla serie storica, contribuendo a delineare un profilo sempre più definito non solo dei Paesi che partecipano ai Giochi, ma anche delle discipline sportive e degli eventi che li compongono. In questo modo, nel corso del tempo, si mette sempre più a fuoco, ad esempio, la distinzione tra sport in cui competono numerosi Paesi e altri in cui la partecipazione è più limitata, oppure tra sport in cui la distribuzione delle medaglie d'oro è più democratica e altri in cui è concentrata nelle mani di pochi. Questo, chiaramente, vale anche per gli eventi all'interno delle varie discipline sportive. Parallelamente, emerge con maggiore chiarezza anche il profilo dei Paesi: si distinguono quelli che gareggiano in un numero più ampio di discipline da quelli più specializzati, quelli che faticano a conquistare medaglie d'oro da quelli capaci di vincere in contesti diversi. Si osservano inoltre differenze tra Paesi con popolazione numerosa che ottengono risulati modesti e Paesi con un numero inferiore di abitanti ma con elevata efficienza sportiva. 

Con questa analisi mettiamo ordine tra questi pattern, osservando la storia olimpica da tre prospettive, quella degli sport, degli eventi e dei Paesi.

## Il profilo storico degli sport

Per definire il profilo storico degli sport ci siamo posti delle domande alle quali abbiamo provato a dare risposta tramite l'utilizzo di una serie di features create ad hoc:
- Quanto è diffuso uno sport? Quanti sono, in media, i Paesi e gli atleti che partecipano ai suoi eventi?
- Quanto sono concentrati gli ori? Sono sempre gli stessi Paesi a vincere oppure le vittorie sono distribuite?
- Quanto "costa" una medaglia d'oro in termini di atleti? È necessario schierare molti atleti o basta un singolo specialista?
- Quanto "costa" una medaglia d'oro in termini di popolazione? Serve un Paese molto popoloso o è possibile essere efficienti anche con un bacino ridotto?
- Quanto contribuisce la distinzione tra sport individuali e sport di squadra nel definire il profilo di uno sport?

Nel rispondere a queste domande sono stati individuati 4 cluster: sport a media diffusione, grandi sport di massa, sport di squadra, sport di nicchia ad alta efficienza.
Di seguit analizziamo come si distribuiscono i cluster rispetto alle diverse features e quali sport vi appartengono. L'analisi è stata limitata agli sport presenti in almeno cinque edizioni olimpiche, al fine di garantire risultati più robusti e rappresentativi.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/01_coord_parall_sport.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

| Cluster   | Nome                                | Sport                                                                                                                                                                          |
|-----------|-------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cluster 0 | Sport a media diffusione            | Badminton, Boxing, Canoe Slalom, Canoe Sprint, Cycling Track, Fencing, Judo, Rowing, Sailing, Taekwondo, Tennis, Weightlifting, Wrestling                                      |
| Cluster 1 | I grandi sport di massa             | Artistic Gymnastics, Athletics, Cycling Road, Shooting, Swimming, Triathlon                                                                                                    |
| Cluster 2 | Sport di squadra                    | Baseball, Basketball, Beach Volleyball, Football, Handball, Hockey, Softball, Volleyball, Water Polo                                                                           |
| Cluster 3 | Sport di nicchia ad alta efficienza | Archery, Artistic Swimming, Cycling Mountain Bike, Diving, Equestrian Dressage, Equestrian Eventing, Equestrian Jumping, Modern Pentathlon, Rhythmic Gymnastics, Table Tennis, Trampolining|

Gli sport a media diffusione sono caratterizzati da un numero di Paesi partecipanti sopra la media, ma da un numero di atleti per evento inferiore. Si tratta principalmente di sport individuali in cui molti Paesi competono pur schierando pochi atleti. La concentrazione delle medaglie d'oro è bassa, quindi diverse nazioni riescono a vincere, incluse anche alcune con popolazione non particolarmente elevata. L'efficienza in termini di medaglie per atleta risulta nella norma.

I grandi sport di massa sono quelli con il più alto numero di Paesi e atleti partecipanti. La distribuzione degli ori è ampia e poco concentrata. Questo cluster presenta una bassa percentuale di eventi di squarda, ma un'elevata efficienza rispetto alla popolazione. Un esempio è rappresentato da Paesi come la Giamaica che, pu avendo dimensioni ridotte, risulta estremamente competitiva nell'atletica. Si tratta di sport "universali", accessibili anche a Paesi con poche risorse ma con atleti altamente specializzati.

Gli sport di squadra sono quelli con il minor numero di Paesi partecipanti. Anche il numero di atleti per evento  aspetto che può sembrare controintuitivo ma che è spiegato proprio dalla minore partecipazione complessiva. Anche l'efficienza per atleta può sembrare controintuitiva, ma dipende dal fatto che una medaglia d'oro è contata per l'intera squadra. In questi sport si osserva una maggiore concentrazione delle vittorie, spesso appannaggio di Paesi medio-grandi con sistemi sportivi collettivi ben strutturati.

Gli sport di nicchia ad alta efficienza coinvolgono pochi Paesi, ma non necessariamente pochi atleti. La concentrazione degli ori è elevata: sono pochi i Paesi che dominano queste discipline. Allo stesso tempo, l'efficienza per atleta è molto alta, pooichè bastano pochi specialisti per ottenere una medaglia. La presenza di sport di squadra è inferiore alla media e i Paesi vincitori tendono ad essere di dimensioni medio-grandi.

Tra le varie analisi condotte sull'evoluzione temporale dei cluster rispetto alle specifiche features, risulta particolarmente interessante quella che descrive come è cambiata, nel corso del tempo, la partecipazione dei Paesi.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/03_nazioni_tempo_sport.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

Si osserva un aumento graduale del numero di Paesi partecipanti in tutti i cluster. Il fenomeno di globalizzazione più evidente riguarda il cluster dei grandi sport di massa, che tra il 1964 e il 2020 vede raddoppiare il numero di Paesi partecipanti. 
Al contrario, il cluster degli sport di squadra si mantiene nel tempo su valori più contenuti, generalmente compresi tra 10 e 20 Paesi partecipanti. Si nota un leggero picco nel 2016, seguito da una diminuizione nel 2020. 
Un elemento particolarmente significativo è il calo della partecipazione in corrispondenza delle Olimpiadi di Mosca del 1980. Questo fenomeno è riconducibile al boicottaggio guidato dagli Stati Uniti in risposta all'invasione sovietica dell'Afghanistan, boicottaggio a cui aderirono numerosi Paesi che decisero di non partecipare ai Giochi.

I quattro profili descritti nascono da medie storiche aggregate, utili per cogliere pattern generali. La seguente heatmap invece segue il percorso inverso, mostrando per ogni sport e per ciasuna edizione olimpica, quali delegazioni sportive hanno dominato il medagliere, con l'obiettivo di analizzare l'evoluzione nel tempo anche di singole discipline di particolare interesse.
A differenza dell'analisi di clustering che richiedeva una base storica minima, questo grafico mostra tutti gli sport presenti tra il 1964 e il 2020, comprese le discipline comparse anche in una sola edizione. Inoltre, nel rispetto della storia delle Olimpiadi, sono state mantenute le delegazioni sportive relative a Paesi non più esistenti o a contesti particolari. Rientrano in questa seconda categoria sia le rappresentative associate a Paesi soggetti a sanzioni (come la Russia, che nel 2020 ha partecipato come ROC), sia la delegazione degli atleti rifugiati, che non rappresenta un singolo Stato ma riunisce atleti impossibilitati a gareggiare sotto la propria bandiera nazionale.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/09_heatmap_totale_sport.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

## Il profilo storico degli eventi

Oltre all'analisi degli sport, proponiamo anche un breve approfondimento sugli eventi sportivi, raggruppandoli secondo una logica analoga a quella appena vista per gli sport, ma applicata questa volta al singolo evento invece che alla disciplina nel suo complesso.
Anche qui è stato applicato un filtro sul numero minimo di edizioni coinvolte per ottenere risultati fondati su una base storica solida. Tuttavia, visto l'elevato numero di eventi che superano comunque questo filtro, ci limitiamo a mostrare la logica con cui l'algoritmo K-Means li ha divisi in tre cluster, senza elencarli uno per uno come fatto per gli sport. 

Per definire il profilo storico degli eventi ci siamo posti alcune delle domande già formulate per gli sport, aggiungendone un'altra:
- Quanto è diffuso un evento? Quanti sono, in media, i Paesi che vi gareggiano?
- Quanto "costa" una medaglia d'oro in termini di atleti? È necessario schierare molti atleti o basta un singolo specialista?
- Quanto "costa" una medaglia d'oro in termini di popolazione? Serve un Paese molto popoloso o è possibile essere efficienti anche con un bacino ridotto?
- Quanto contribuisce la distinzione tra eventi individuali ed eventi di squadra nel definire il profilo di uno evento?
- Quante sono le nazioni che hanno vinto almeno una medaglia d'oro in quell'evento nel corso del tempo?

Nel rispondere a queste domande sono stati individuati 3 cluster: eventi di nicchia ad alta efficienza, eventi di squadra, il grande bacino degli eventi individuali.
Di seguit analizziamo come si distribuiscono i cluster rispetto alle diverse features.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/10_coord_parall_event.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

Cluster 0, il cluster degli eventi di nicchia ad alta efficienza. È il cluster che presenta il valore più alto per l'efficienza in base al numero di atleti. Anche se per ogni Paese si qualificano pochi atleti in questi eventi, ne basta uno per portare a casa l'oro. Sono eventi di nicchia perchè non solo non partecipano molte nazioni, ma tra quelle che partecipano sono pochi i Paesi che si spartiscono storicamente questi ori. Infine, la percentuale di eventi di squadra e l'efficienza in base alla popolazione sono poco sotto la media.

Cluster 1, il cluster degli eventi di squadra. Così come si intuisce dal nome e come si osserva dal grafico, è il cluster che raccoglie gli eventi di squadra per cui, come già visto per gli sport, gareggiano poche nazioni. Per quanto riguarda l'efficienza in base al numero di atleti, vale quanto già detto nel caso della descrizione degli sport di squadra. L'efficienza per popolazione e il numero di nazioni che hanno vinto almeno un oro sono sul valore medio.

Cluster 2, il grande bacino degli eventi individuali. È un ampio contenitore di eventi olimpici individuali più globalizzati rispetto a quelli del Cluster 0. L'efficienza per numero di atleti, l'efficienza per popolazione e il numero di nazioni che hanno vinto almeno un oro si concentrano intorno al valore medio. 

Coerentemente con quanto fatto per gli sport, analizziamo l'evoluzione temporale della partecipazione dei Paesi agli eventi appartenenti ai tre cluster.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/12_nazioni_tempo_event.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

Il Cluster del grande bacino degli eventi inidividuali e quello degli eventi di nicchia ad alta efficienza mostrano un graduale aumento dei Paesi partecipanti nel corso del tempo. Nello specifico, per il Cluster degli eventi individuali di nicchia ad alta efficienza si notano due picchi in corrispondenza delle edizioni olimpiche del 1984 e del 1996: il primo è presumibilmente lo specchio del boicottaggio di Mosca 1980 (le nazioni occidentali tornano a gareggiare dopo l'assenza della precedente edizione), il secondo coincide con l'assestamento definitivo delle nazioni nate dalla dissoluzione dell'URSS e della Jugoslavia come Comitati Olimpici indipendenti. (DA INVESTIGARE MEGLIO)
Coerentemente con quanto visto nell'analisi temporale degli sport, il cluster degli eventi di squadra ha un moderato aumento dei Paesi partecipanti nel corso del tempo che negli anni più recenti si appiattisce e tende a decrescere.
Inoltre, così come già notato nell'analisi temporale effettuata sugli sport, si nota un importante calo nei paesi partecipanti nell'edizione olimpica dei Mosca del 1980, dovuto al già discusso boicottaggio.

## Il profilo storico dei Paesi

Anche per definire il profilo storico dei Paesi ci siamo posti una serie di domande alle quali abbiamo provato a dare risposta tramite l'utilizzo di una serie di features create ad hoc:
- Quanto è "prezioso" il medagliere di un Paese? Che quota delle due medaglie sono ori rispetto ad argenti e bronzi?
- Quanti sono gli sport distinti in cui un Paese gareggia nel corso della sua storia olimpica? Si concentra su poche discipline o partecipa ovunque?
- Quanto "costa" una medaglia d'oro in termini di atleti? È necessario schierare molti atleti o bastano pochi specialisti?
- Quando "cosa" una medaglia d'oro in termini di popolazione? Serve un paese molto popoloso o è possibile essere efficienti anche con un bacino ridotto di abitanti?
- Da quante edizioni olimpiche un Paese gareggia sotto la sua attuale bandiera? Quanto è lunga la sua storia olimpica?
 
Nel rispondere a queste domande sono stati individuati 7 cluster: sport a media diffusione, grandi sport di massa, sport di squadra, sport di nicchia ad alta efficienza.
Prima di analizzare come si distribuiscono i cluster rispetto alle diverse features e quali Paesi vi appartengono, è opportuno fare alcune considerazioni. Poiché la maggior parte delle features introdotte descivono il successo olimpico di un Paese, sono stati inclusi nell'analisi soltanto i Paesi che, durante il corso della loro partecipazione alle edizioni olimpiche, hanno conquistato almeno un totale di 10 medaglie. Inoltre, poiché l'analisi presenta una "fotografia" della situazione attuale dei Paesi, costruita aggregando i dati delle serie temporali, i cosiddetti "Paesi storici", così come i casi speciali di delegazioni che non fanno riferimento ad alcun Paese o che sono il frutto di una sanzione ad un Paese, sono stati esclusi dall'analisi. Inoltre, per mancanza di dati sulla popolazione per l'intera serie storica, sono stati esclusi dall'analisi anche Taipei Cinese e Kosovo.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/16_coord_parall_paesi.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

| Cluster   | Nome                                        | Paesi                                                                                                                                                      |
|-----------|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Cluster 0 | Paesi con breve storia olimpica             | Armenia, Azerbaijan, Belarus, Croatia, Czechia, Estonia, Georgia, Kazakhstan, Latvia, Lithuania, South Africa, Slovenia, Serbia, Slovakia, Ukraine, Uzbekistan |
| Cluster 1 | Piccoli Paesi iper-efficienti               | The Bahamas, Cuba, Finland, Hungary, Jamaica, Norway, New Zealand                                                                                          |
| Cluster 2 | Paesi con alta partecipazione ma poco successo | Argentina, Austria, Brazil, Colombia, Egypt, Israel, Mexico, Portugal, Venezuela                                                                           |
| Cluster 3 | Paesi  e poco successo | Dominican Republic, Indonesia, India, Malaysia, Mongolia, Nigeria, Trinidad and Tobago                                                                                                                                                   |
| Cluster 4 | Potenze olimpiche consolidate               | Australia, Belgium, Bulgaria, Canada, Denmark, Spain, France, Great Britain, Greece, Ireland, Italy, Japan, South Korea, Netherlands, Poland, Romania, Switzerland, Sweden                                                                                                                               |
| Cluster 5 | Le superpotenze olimpiche                   | China, Germany, Russia, United States                                                                                                                                                           |
| Cluster 6 | Paesi con bassa partecipazione ma alto sccesso | Algeria, Ethiopia, Iran, Kenya, Morocco, North Korea, Thailand, Tunisia, Türkiye, Uganda                                                                                                                                                           |

Ad esclusione del Sudafrica, il cluster dei Paesi con breve storia olimpica contiene tutti i paesi che si sono formati dopo la scissione dell'Unione Sovietica, della Yugoslavia e della Cecoslovacchia. Il tratto distintivo di questo cluster è proprio il numero ridotto di edizioni olimpiche in cui hanno gareggiato che, per quanto riguarda i paesi neoformatisi, è coerente con la loro non precedente esistenza. Un Paese che sembrerebbe stonare in questo cluster ma che in realtà è del tutto legittimo è il Sudafrica, anch'esso partecipante a poche edizioni olimpiche per via del periodo di esclusione dal 1964 al 1988 a causa delle politiche di segregazione razziale. 
Indagando la percentuale di successo dei Paesi di questo cluster nelle categorie sportive, notiamo le seguenti percentuali: Athletics 62%, Shooting 50%, Wrestling 43%, Rowing 37%, Weightlifting 37%, Judo 31%, Swimming 25%, Taekwondo 25%, Boxing 18%, Canoe Slalom 18%. Questa firma sportiva conferma e arricchisce il quadro presenato: Atletica, Tiro, Lotta, Canottaggio, Sollevamento Pesi, sono l'inequivocabile eredità dei Paesi di cui facevano parte e che avevano, per queste discipline, programmi di allenamento specializzati.

Il tratto caratteristico del cluster dei piccoli Paesi iper-efficienti è quello relativo alle medaglie d'oro per popolazione, che risulta essere il più alto tra tutti i cluster. Anche la quota di ori sul totale delle medaglie è la più alta tra tutti i cluster, quasi identica a quella del custer 5. Sul numero di sport, invece, il cluster scende leggermente sotto la media: sono Paesi che non competono ovunque, ma dove competono, spesso vincono, e lo fanno con una popolazione ridotta alle spalle.
La firma sportiva è la più netta di tutta l'analisi: Atletica al 100%. Tutte e sette le nazioni hanno vinto oro in questa disciplina, è l'unico caso in cui un intero cluster condivide lo stesso sport senza eccezioni e, alla luce dei Paesi che compongono il cluster ha perfettamente senso. Seguono Canoe Sprint 71%, Sailing 57%, Shooting 57%, Weightlifting 57%, Wrestling 57%, Rowing 42%, Boxing 28%, Cycling Track 28% e Football 28%.

Per quanto riguarda invece i Paesi del cluster "alta partecipazione ma poco successo", il tratto caratteritico è la loro assidua partecipazione alle edizioni olimpiche e in sport variegati a cui fa da contrapposizione un medagliere povero di ori. Questo è il cluster di Paesi che partecipano ampiamente al programma olimpico, ma che faticano a convertire quella partecipazione in medaglie d'oro. 
La firma sportiva conferma un quadro senza un vero punto di forza dominante: Athletics 55%,
Sailing 44%, Boxing, Football e Judo 33%, Artistic Gymnastics, Swimming, Taekwondo e Weightlifting 22%, Basketball 11%.

Anche i Paesi del Cluster 3 hanno basso successo ma, in confrotno ai paesi del Cluster precedente, partecipano in molte meno categorie sportive pur costituendo "presenza fissa" nelle varie edizioni olimpiche. Questo è il cluster con i valori più bassi su qualsiasi dimensione che misura il successo. Sono Paesi concentrati in pochissime discipline, con un tasso di conversione in oro strutturalmente basso anche in quelle poche.
La firma sportiva lo conferma visivamente in modo netto: questi paesi non hanno percentuali per sole 7 discipline e già dal quarto sport in classifica si scende sotto il 15%: Athletics 57%, Boxing 28%, Badminton, Football, Hockey, Judo e Shooting 14%.

Il tratto distintivo del cluster delle potenze olimpiche consolidate è quello di essere secondo su quasi tutte le dimensioni consolidate, nonostante sia il cluster con il numero di edizioni leggermente più alto tra tutti. È il profilo di chi ha una lunghissima storia olimpica e una partecipazione amplissima, che non rispecchia in modo netto l'efficienza, che pur essendo positiva non raggiunge mai valori estremi. È la classica "seconda fascia" delle grandi potenze olimpiche.
AGGIUNGERE FIRMA SPORTIVA

INTERPRETAZIONE CLUSTER 5 E 6 + FIRMA SPORTIVA

La seguente mappa permette di esplorare quali sono i top 5 sport in cui i singoli Paesi eccellono. Sono presenti nella mappa soltanto i paesi attualmente esistenti. In blu sono presenti tutti i paesi che hanno vinto almeno una medaglia, mentre in grigio sono presenti tutti quei Paesi che, pur avendo partecipato alle Olimpiadi, non hanno mai vinto alcuna medaglia. Sono inoltre presenti in grigio chiaro Paesi per cui non si hanno dati. Nello specifico, la Groenlandia che non ha un compitato nazionale olimpico e i cui atleti gareggiano sotto la bandiera della Danimarca, la Nuova Caledonia il cui comitato locale non è riconosciuto dal CIO e che è quindi esclusa dalle Olimpiadi, e l'Antartide che, pnaturalmente, non partecipa alle Olimpiadi.
Per esplorare i top 5 sport per le entità storiche, non più esistenti e per le suadre non appartenenti ad alcun paese o sottoposte a sanzione, è possibile visualizzare il grafico che si trova sotto la mappa.

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/18_mappa_interattiva_paesi.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

<div style="height: 560px">
<vegachart schema-url="{{site.baseurl}}/assets/charts/santina/19_grafico_interattivo_paesi_storici.json" style="width: 100%; height: 100%"></vegachart>
</div>
<br/>

### Nota metodologica

I dati provengono dal dataset storico dei risultati olimpici (dettaglio atleta-evento e biografie degli atleti) incrociato con il dato sulla popolazione proveniente dal dataset degli indicatori socio-economici World Bank.
A partire da queste fonti sono stati costruti una serie di dataset aggiuntivi, popolati con nuove features derivate da quelle originarie. Per ogni vittoria negli sport di squadra si considera una sola medaglia per tutta la squadra. I paesi storici non più esistenti sono trattati in modo disgiunto dai paesi risultanti dalla loro scissione, così come le delegazioni sportive che non hanno paesi corrispondenti o quelle risultati da sanzioni.
I profili degli sport, degli eventi e dei Paesi sono stati costruiti aggregando i dati appartenenti alle serie storiche.
