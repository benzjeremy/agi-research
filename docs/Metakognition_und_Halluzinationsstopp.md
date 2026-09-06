# Test 9: Metakognition & Epistemische Selbstbewertung (Halluzinations-Stopp)

## 1. Ausgangshypothese & Klassische Theorien ("Alte Werte")
Ein Hauptargument gegen die Möglichkeit von AGI bei LLMs ist das **Halluzinationsproblem**: Modelle raten platt auf Basis statistischer Wahrscheinlichkeiten, ohne zu "wissen, was sie nicht wissen".

## 2. Testergebnisse & Befunde (`test_metacognition.py`)
- **Test-Setup**: Evaluation von epistemischer Konfidenzmessung vor der Antwort-Generierung.
- **Ergebnis**: 
  - Ohne Metakognition generiert das Modell falsche Gewissheiten.
  - Mit metakognitiver Bewertung schaltet der Agent bei Unsicherheit automatisch auf `REFUSE_AND_SEARCH` um (Halluzinations-Vermeidung).

## 3. Widerlegung / Bestätigung
- ❌ **Widerlegt**: Das Dogma, dass Neuronale Netze unheilbar zum Halluzinieren verdammt sind.
- ✅ **Bestätigt**: Metakognitive Selbstbewertung ("I know that I don't know") ist durch Agenten-Architekturen umsetzbar.

## 4. Relevanz für AGI
AGI erfordert Selbsterkenntnis über die eigenen Wissenslücken, um gezielt fehlende Informationen zu beschaffen, statt plausible Lügen zu erfinden.
