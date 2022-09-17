# Netzfrequenz_speichern

Dieses Python Script Speichert ungefaer jede Sekunde die Netzfrequenz, bereitgestellt durch https://www.netzfrequenz.info/, in einer csv datei. Dies CSV Datei befindet sich im Ordner Daten und hat einen Namen aus Ziffern 9999.csv. Die Ziffern sind die ersten 4 stellen des Datums als Int. (import time; print(time.time())). Die Dateigroesse betraegt zwischen 22MB und 32MB. Das Script hat eine Wartezeit von 0.7 sekunden nach Websitenanfrage und speichern der Werte um auf ungefaehr einen Wert pro Sekunde zu kommen.
CSV format : 
Zeitpunkt;Frequenz
1663425631000;49.983

Problem:
Das Anfragen des Servers nach den Daten sowie das speicher dieser dauert unterschiedlich lang. Deshalb kann es dazukommen, dass Werte doppelt erfasst oder Sekunden uebersprungen werden.