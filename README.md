# Netzfrequenz_speichern #
## Funktionsweise ##

![](./Netzfrequenz_speichern/Netzfrequenz_speichern.drawio.svg)

https://github.com/user-attachments/assets/b993eeb0-f1e7-4647-affe-7f63ec9b3469

Dieses Python Script Speichert ungefaer jede Sekunde die Netzfrequenz, bereitgestellt durch https://www.netzfrequenz.info/, in einer csv datei. Dies CSV Datei befindet sich im Ordner Daten und hat einen Namen aus Ziffern 9999.csv. Die Ziffern sind die ersten 4 stellen des Datums als Int. (import time; print(time.time())). Die Dateigroesse betraegt zwischen 22MB und 32MB. Das Script hat eine Wartezeit von 0.5 sekunden nach Websitenanfrage und speichern der Werte um auf ungefaehr einen Wert pro Sekunde zu kommen. Die Datei wird nach jedem Wert gespeichert um Datenverlust bei Serverabsturz zu vermeiden.
## CSV format ## 
Zeitpunkt;Frequenz<br>
1663425631000;49.983

## Problem  ##
Das Anfragen des Servers nach den Daten sowie das speicher dieser dauert unterschiedlich lang. Dadurch passiert es, dass Werte doppelt erfasst oder Sekunden uebersprungen werden.

## Wie ich es hoste ##
Ich hoste mein Script auf replit.com. Um automatisches abschalten meines Scriptes zu vermeiden wird in keep_alive.py ein Webserver erstellt, welcher alle 5 minuten von uptimerobot.com angefragt wird. Da der Speicherplatz auf replit.com begrenzt ist, lade ich die Daten von replit hier hoch. Um die Daten zu erhalten, welche noch nicht auf github sind kann man diese direkt von https://replit.com/@gamebeaker/Netzfrequenzspeichern#Daten downloaden.
