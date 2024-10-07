# API Validierung

Das Schema der API wird sowohl beim Rendern validiert, als auch beim
Einchecken von Konfiguration im Vivi.

Für genaue Fehlermeldungen bei der Validierung sind die `discriminators`
im Schema wichtig. Sie machen aus "Validation error in Doc" ein "666
is not of type String in tabs/0/title". Diese Erweiterung des Schemas
wurde mit [PR 115](https://github.com/ZeitOnline/docs-zappi/pull/115)
eingeführt.

## Validierung im Vivi

Beim Einchecken im Vivi werden Dateien vom Typ JSON schon immer darauf
validiert, dass sie gültiges JSON sind. Das passiert beim Speichern.

Zusätzlich für die großen Structure-Dokumente der API wurde eine weitere
Validierung beim Einchecken eingeführt. Diese prüft das Dokument gegen
ein Schema. Beim Bearbeiten von JSON Dokumenten im Vivi gibt es den Tab
"Validieren". Hier kann eine Schema URL (z.B.
[https://zappi.staging.zeit.de/1.0.0/openapi.yaml](https://zappi.staging.zeit.de/1.0.0/openapi.yaml)) und ein Schemafeld
(z.B. `Structure`) eingegeben werden. Dann wird beim Einchecken des
Dokuments der Inhalt gegen eben jenes Schema überprüft.

Für die meisten JSON Dateien im Vivi gibt es solche eine Validierung
nicht, da sind diese Felder dann leer. Für API-Strukturen (Navigation
z.B.) ist das Feld gesetzt. Die Werte werden gespeichert. Also wird
zukünftig bei jedem Einchecken eines Dokuments gegen das Schema
validiert.

Achtung: bei einer Schema-Änderung, die zum Beispiel nur auf Staging
liegt, muss dann auch die Staging-Adresse der Spec eingetragen werden
(solange diese neue Spec noch nicht nach Production deployed wurde). Die
wird beim Sync von Production nach Staging ggf überschrieben.

Zur Einordnung: das ist kein Zappi-Feature, sondern in Vivi eingebaut,
dass man JSON nur als JSON validiert, oder gegen ein konkretes Schema.
Aber weil das Feature ausschließlich für die Validierung der
App-Navigation gegen das Zappi-Schema genutzt wird, steht es hier.

## Validierung in der API

Beim Rendern von Inhalten (Centerpages) oder Dokumenten (Navigation
Structure) über die Zappi (API View bzw. "App-Vertical" von zeit.web)
wird die Response gegen das Schema validiert, bevor sie gesendet wird.
Ist etwas falsch, gibt es eine Fehlermeldung im JSON Format als Antwort.
