=====================
Entwickler-Onboarding
=====================

API-Dokumentation
=================

Die API-Dokumentation wird als OpenAPI-Spezifikation in ``api.yaml`` gepflegt,
und mit dem swagger-ui HTML/JS daraus direkt angezeigt.

Wegen CORS&Co muss man lokal immer ``bin/docs serve`` verwenden.


API validieren
==============

Mit ``bin/test`` kann man die ``api.yaml`` auf syntaktische Korrektheit mit dem OpenAPI-Standard überprüfen.
