=========
Überblick
=========

Eine REST API speziell für die aktuell von der Agentur Prepublic Entwickelte iOS und Android Anwendung.


Prototyp der App
----------------

Der Prototyp dazu kann auf `Invision <https://invis.io/Z6XKZ4QM3KX>`_ eingesehen werden.


Prototyp des Backends
---------------------

Die jeweils aktuelle Entwicklungsversion des Backends ist unter ``https://zappi.staging.zeit.de/x.y.z`` erreichbar, wobei ``xxx`` derzeit ein beliebiger Platzhalter für die Version sein kann, der vom Backend ignoriert wird.
Sprich, egal, welcher Wert dort steht, es wird immer die aktuellste Version ausgeliefert.

Der Endpunkt ist per Basic Auth mit hardgecodeten Credentials geschützt, die `im Vault liegen <https://vault.ops.zeit.de/ui/vault/secrets/zon%2Fv1/show/zappi/production/fastly-basic-auth>`_.


Auslieferung
------------

Zappi liefert Inhalte in Form von json aus, die von der App nativ gerendert werden. Das Backend baut hierzu auf dem Framework von `zeit.web.site` auf. Aus diesem Grund werden spezielle Anpassungen aus den Vertikals nicht unterstützt. 
