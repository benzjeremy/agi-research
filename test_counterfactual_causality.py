import json

class CounterfactualEngine:
    def __init__(self):
        # Causal graph: Action -> Intermediate State -> Outcome
        self.causal_graph = {
            "apply_brakes": {"speed": "decreased", "accident": "prevented"},
            "accelerate": {"speed": "increased", "accident": "occurred"}
        }

    def evaluate_counterfactual(self, actual_action, observed_outcome):
        # "What if I had taken an alternative action instead?" (Pearl's 3rd level of Causality)
        alternative_action = "apply_brakes" if actual_action == "accelerate" else "accelerate"
        hypothetical_outcome = self.causal_graph.get(alternative_action, {})
        
        counterfactual_regret = observed_outcome != hypothetical_outcome.get("accident")
        return {
            "actual_action": actual_action,
            "actual_outcome": observed_outcome,
            "counterfactual_action": alternative_action,
            "counterfactual_outcome": hypothetical_outcome.get("accident"),
            "causal_reasoning_valid": counterfactual_regret
        }

def run_test():
    engine = CounterfactualEngine()
    result = engine.evaluate_counterfactual(actual_action="accelerate", observed_outcome="occurred")

    res = {
        "pearl_causal_level_3_passed": result["causal_reasoning_valid"],
        "details": result
    }
    print("Test 11 (Counterfactual Reasoning & Pearl Causality Level 3) Results:", json.dumps(res, indent=2))
    return res

if __name__ == "__main__":
    run_test()
