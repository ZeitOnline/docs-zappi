# YAML Coding-Style

## Syntax

-   Indentation: 2 Leerzeichen (Listen immer einrücken, auch wenn der
    yaml-Standard es dort nicht zwingend verlangt)
-   Strings quoten mit Double Quotes (`"foobar"`, NICHT `'foobar'`)
-   Identifier nicht quoten (`type: string`, NICHT `type: "string"`)
-   Leerzeilen zwischen inhaltlichen Abschnitten verwenden
-   Inline Listen/Dicts höchstens bei Beispielen verwenden (z.B.
    `example: ["zplus"]`), sonst immer neue Zeile und einrücken

## Namen

-   Schema-Objekte verwenden CamelCase mit Großbuchstaben vorn (z.B.
    `CenterpageElement`, `TabDefinitionBase`)
-   Properties verwenden dromedaryCase (lower camel case) (z.B.
    `baseUrl`, `dateFirstPublished`)
-   Identifier verwenden kebab-case und werden klein geschrieben (z.B.
    `zplus-register`, `menu-entry-native`)
