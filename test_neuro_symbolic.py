import json

class PropositionalReasoner:
    def __init__(self):
        self.rules = []

    def add_rule(self, premise, conclusion):
        self.rules.append((premise, conclusion))

    def infer(self, facts):
        inferred = set(facts)
        changed = True
        while changed:
            changed = False
            for premise, conclusion in self.rules:
                if premise in inferred and conclusion not in inferred:
                    inferred.add(conclusion)
                    changed = True
        return inferred

def run_test():
    reasoner = PropositionalReasoner()
    # Symbolic classic logic (Modus Ponens chain)
    reasoner.add_rule("AGI_needs_reasoning", "AGI_needs_symbols")
    reasoner.add_rule("AGI_needs_symbols", "NeuroSymbolic_Architecture_Required")
    
    initial_facts = {"AGI_needs_reasoning"}
    derived = reasoner.infer(initial_facts)
    
    res = {
        "initial_facts": list(initial_facts),
        "derived_conclusions": list(derived),
        "is_neurosymbolic_valid": "NeuroSymbolic_Architecture_Required" in derived
    }
    print("Test 3 (Neuro-Symbolic Reasoning) Results:", json.dumps(res, indent=2))
    return res

if __name__ == "__main__":
    run_test()
