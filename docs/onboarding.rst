=====================
Entwickler-Onboarding
=====================

API-Dokumentation
=================

Die API-Dokumentation wird als OpenAPI-Spezifikation in ``api.yaml`` gepflegt,
und mit dem swagger-ui HTML/JS daraus direkt angezeigt.

Wegen CORS&Co muss man lokal immer ``bin/docs serve`` verwenden.

Die Doku der API findet man lokal unter ``http://0.0.0.0:8000/swagger.html``


API validieren
==============

Mit ``bin/test`` kann man die ``api.yaml`` auf syntaktische Korrektheit mit dem OpenAPI-Standard überprüfen.


Backend
=======

Zappis Backend findet sich in zeit.web.app, dort ist das Zappi Repo als Submodule eingebunden. 

.. note::
    Das führt mitunter zu Mergekonflikten, wenn verschiedene Versionen des Submodules kollidieren. Hier hilft in vielen Fällen ``git submodule update --init --recursive`` um das Submodul auf den gegenwärtigen Stand (des Masters) zu bringen.


Spec Version in zeit.web hochziehen
===================================

* in ``zeit.web/src/zeit/web/app/spec`` auf den master wechseln, master pullen
* neuen Branch anlegen, Änderung machen, committen, PR stellen, PR mergern
* auf den Master wechseln, Master pullen -> neue Änderung sollte da sein

* in ``zeit.web`` neuen Branch anlegen
* ``$ git status`` sollte zeigen, dass sich ``zeit.web/src/zeit/web/app/spec`` geändert hat
* diese Änderung committen und PR in zeit.web stellen

-> Success
