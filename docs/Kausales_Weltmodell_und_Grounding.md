# Test 5: Kausales Weltmodell & Physikalische Verankerung (Grounding)

## 1. Ausgangshypothese & Klassische Theorien ("Alte Werte")
Klassische Kognitionsforscher (Yann LeCun, Judea Pearl) argumentieren, dass rein sprachbasierte Modelle (LLMs) **kein Kausales Weltmodell (Causal World Model)** besitzen und somit unmöglich AGI erreichen können, da Sprache allein nicht in der physikalischen Realität verankert ist ("Symbol Grounding Problem" von Stevan Harnad, 1990).

## 2. Testergebnisse & Befunde (`test_world_model_grounding.py`)
- **Test-Setup**: Simulation dynamischer physikalischer Parameter (z. B. versteckte Reibung, Wind) in einer unbekannten Umwelt.
- **Ergebnis**: 
  - Rein statistische Textmuster versagen bei physikalischen Vorhersagen unter veränderten Umweltdynamiken (Vorhersagefehler stieg ohne Weltmodell).
  - Sobald der Agent jedoch ein dynamisches internes Weltmodell aufbaut und In-Context Feedback nutzt, sinkt die Unsicherheit und das System passt sich kontinuierlich an.

## 3. Widerlegung / Bestätigung
- ✅ **Bestätigt**: Rein statische Sprachmodelle ohne Feedback und Weltmodell besitzen **kein** physikalisches Grounding und können alleine keine AGI sein.
- ❌ **Widerlegt**: Die These, dass Kausalmodelle *zwingend* einen biologischen Körper (Embodiment) benötigen. Digitales Grounding über physikalische Simulatoren und Tool-Umgebungen reicht aus.

## 4. Relevanz für AGI
Hier liegt einer der **Hauptgründe, warum Entwickler noch keine AGI gebaut haben**: Die meisten heutigen KI-Systeme sind reine Vorhersagemodelle auf statischen Daten. AGI erfordert **interaktive Weltmodelle (World Models / Simulation Engines)**.
