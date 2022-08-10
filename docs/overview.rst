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


Versionierung
-------------

Bisher ist keine echte Versionierung der API erfolgt, allerdings wird die Version in Fastly in den Backend Request Header geschrieben `x-zappi-version=major.minor.patch`. Diese Version wird bei Requests an die `app_structure` und `app_config` Endpunkte genutzt, um unterschiedliche Versionen der Dateien ausliefern zu können. 
Die Dateien liegen in Ordnern in vivi folgen dem Format: /major-minor-patch/{filename}. Sollte die angefragte Version nicht zur Verfügung stehen, wird die `/default-version/{filename}` ausgegeben.

Auslieferung
------------

Zappi liefert Inhalte in Form von json aus, die von der App nativ gerendert werden. Das Backend baut hierzu auf dem Framework von `zeit.web.site` auf. Aus diesem Grund werden spezielle Anpassungen aus den Vertikals nicht unterstützt. 
