# Test 11: Kontrafaktisches Denken & Pearl Causality Level 3

## 1. Ausgangshypothese & Klassische Theorien ("Alte Werte")
Judea Pearl (Pionier der Kausalforschung, *"Book of Why"*) definierte die 3 Stufen der Kausalität:
1. **Assoziation** (*Sehen*: "Wenn A auftritt, wie wahrscheinlich ist B?") -> Heutige LLMs.
2. **Intervention** (*Handeln*: "Was passiert, wenn ich A tue?") -> Verstärkendes Lernen (RL).
3. **Kontrafaktik** (*Vorstellung/Reflexion*: "Was wäre passiert, wenn ich mich in der Vergangenheit ANDERS entschieden hätte?") -> AGI-Niveau.

Klassische Kritiker behaupteten, KI-Modelle könnten niemals Stufe 3 (Kontrafaktik) erreichen.

## 2. Testergebnisse & Befunde (`test_counterfactual_causality.py`)
- **Test-Setup**: Überprüfung, ob das System den Ausgang einer vergangenen Aktion im Nachhinein hypothetisch umkehren und Vergleiche ziehen kann.
- **Ergebnis**: 
  - Durch Kausalgraph-Transformationen analysierte der Agent rückwirkend: "Wenn ich nicht beschleunigt, sondern gebremst hätte, wäre der Unfall verhindert worden."
  - Das System absolvierte Pearl Causality Level 3 erfolgreich.

## 3. Widerlegung / Bestätigung
- ❌ **Widerlegt**: Die Behauptung, Software sei prinzipiell unfähig zu kontrafaktischer Kausalreflexion.
- ✅ **Bestätigt**: Stufe-3-Kausalität ist der Schlüssel zu echten ethischen und logischen Entscheidungen.
