# JSON includes

In vivi kann für JSON-Dateien aktiviert werden, dass `$include` auf weitere vivi JSON-Dateien beim Ausliefern durch Zappi aufgelöst und ersetzt werden.

(Das funktioniert auch rekursiv, include-in-einem-include, solang an jeder Datei, in der `$include` ersetzt werden soll, der "include ersetzen" Haken aktiviert ist.
Aber Achtung, dass man keine Kreise o.ä. baut.)

Beispiel:

```json
// /data/app/1-2-3/structure
{
  "tabs": [
    "items": [
      {
        "id": "section-one",
        "items": [
          {"id": "one1", ...}
        ]
      },
      {"$include": "http://xml.zeit.de/data/app/default-version/shared-section"}
      {
        "id": "section-two",
        "items": {"$include": "http://xml.zeit.de/data/app/default-version/section-two-items"}
      },
      {
        "id": "section-three",
        "items": [
          {"id": "three1"}
          {"$include": "http://xml.zeit.de/data/app/default/version/shared-item"}
        ]
      }
    ]
  ]
}

// /data/app/default-version/shared-section
{
  "id": "shared-section"
  "items": [...]
}

// /data/app/default-version/section-two-items
[
  {"id": "two1", ...},
  {"$include": "http://xml.zeit.de/data/app/default-version/shared-item"}
]

// /data/app/default-version/shared-item
{"id": "shared-item", ...}
```

wenn die App dann `zappi.zeit.de/1.2.3/structure` abruft, erhält sie

```json
{
  "tabs": [
    "items": [
      {
        "id": "section-one",
        "items": [
          {"id": "one1", ...}
        ]
      },
      {
        "id": "shared-section"
        "items": [...]
      },
      {
        "id": "section-two",
        "items": [
          {"id": "two1", ...},
          {"id": "shared-item", ...}
        ]
      },
      {
        "id": "section-three",
        "items": [
          {"id": "three1"}
          {"id": "shared-item", ...}
        ]
      }
    ]
  ]
}
```


## Implementierungsdetails

Das ist jetzt vivi-spezifische Syntax und Verhalten.
Es gibt zwar z.B. in OpenAPI/[JSON Schema](https://json-schema.org/understanding-json-schema/structuring) sowas ähnliches (`$ref` etc.),
aber das ist sowohl von der Idee als auch [der Implementierung](https://referencing.readthedocs.io/en/stable/intro/) sehr auf den Schema-Usecase zugeschnitten,
und nicht auf "löse Includes fertig auf".

Falls das hilfreich ist, könnten wir perspektivisch aber durchaus wie dort auch [JSON Pointer](https://datatracker.ietf.org/doc/html/rfc6901) bei uns [unterstützen](https://pypi.org/project/jsonpointer/),
sodass man nicht nur komplette Dateien includen kann, sondern auch Teilbäume
(z.B. `http://xml.zeit.de/data/app/default-version/shared-section#/items/0`).
