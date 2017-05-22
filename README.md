# ALLERTA_ALLARME

Moduli allerta allarme per Narvalo (usano il berryclip plus) usa un socket in ascolto del CC sulla porta 8082 e un socket per l'invio dei dati in ascolto sul CC alla porta 8081.

Sono in totale due: 
 - messaggi_CC.py: interprete dei mesaggi che arrivano dal CC
 - allarme_generico.py: invia i messaggi di allarme generico usando il berryclip sia al CC che al Concentratore Narvalo usando due canali separati

Alla prima installazione è necessario un sudo chmod +x nome_script.sh

Per fare il kill dei messaggi:

 - ps aux | grep python --> leggo il PID
 - sudo kill -9 PID_NUMBER


Modulo per allarme generico usa invece un socket in cui il CC è in ascolto sulla porta 8081. Gli va impostato l'indirizzo IP del CC, (la porta) e l'identificativo dell'apparato.

Moduli del berryclip plus scaricati da https://github.com/recantha/berryclip 
