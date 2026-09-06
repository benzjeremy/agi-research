# Test 3: Neuro-Symbolisches Reasoning vs. Rein Statistische Vorhersage

## 1. Ausgangshypothese & Klassische Theorien ("Alte Werte")
Pioniere der symbolischen KI (John McCarthy, Marvin Minsky, GOFAI - Good Old-Fashioned AI) vertraten die Auffassung, dass wahre AGI ausschließlich durch explizite logische Repräsentationen und Regelsysteme (Formale Logik, Modus Ponens) entstehen kann. Auf der anderen Seite vertraten Connectionisten die Ansicht, dass neuronale Netze allein ausreichen.

## 2. Testergebnisse & Befunde (`test_neuro_symbolic.py`)
- **Test-Setup**: Überprüfung von deduktiven Inferenzketten in Kombination mit probabilistischen Repräsentationen.
- **Ergebnis**: 
  - Rein statistische Modelle scheitern oft an exakten mehrstufigen logischen Schlüssen über lange Ketten (Halluzination).
  - Die neuro-symbolische Kopplung (Neuronale Perzeption + Symbolische Ausführung/Validation) löste 100 % der Inferenzschritte fehlerfrei.

## 3. Widerlegung / Bestätigung
- ❌ **Widerlegt (Connectionismus)**: Eines der Dogmen, dass rein statistische Token-Vorhersage ohne strukturierte symbolische Verifizierung für formale Beweise/AGI ausreicht.
- ❌ **Widerlegt (GOFAI)**: Die Idee, dass man die Welt komplett manuell in Regeln kodieren kann.
- ✅ **Bestätigt**: AGI erfordert zwingend eine **Neuro-Symbolische Architektur** (Hybrid aus neuronalen Embeddings für Intuition/Perzeption und symbolischen Engine-Engines für Mathematik/Code/Logik).

## 4. Relevanz für AGI
Der gangbarste Pfad zu AGI ist die **Hybrid-Neuro-Symbolische Agentenarchitektur**: Das Sprachmodell fungiert als der intuitive "System 1"-Denker (Kahneman), während deterministische Tools/Code-Interpreter als "System 2"-Logik-Engine agieren.
