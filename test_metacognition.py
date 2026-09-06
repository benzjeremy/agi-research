import json

class MetacognitiveAgent:
    def __init__(self):
        self.confidence_threshold = 0.8
        self.refusal_or_hallucination_detected = 0

    def evaluate_query(self, query, knowledge_base):
        # Epistemic self-assessment
        confidence = knowledge_base.get(query, 0.1) # low if unknown
        
        if confidence < self.confidence_threshold:
            # Metacognitive awareness: "I don't know, I need to look it up or refuse to guess"
            action = "REFUSE_AND_SEARCH"
            self.refusal_or_hallucination_detected += 1
        else:
            action = "ANSWER_DIRECTLY"
        return action, confidence

def run_test():
    agent = MetacognitiveAgent()
    kb = {"What is 2+2?": 0.99, "What is the exact mass of exoplanet X99?": 0.05}

    action1, conf1 = agent.evaluate_query("What is 2+2?", kb)
    action2, conf2 = agent.evaluate_query("What is the exact mass of exoplanet X99?", kb)

    res = {
        "known_query_action": action1,
        "unknown_query_action": action2,
        "hallucination_mitigated": action2 == "REFUSE_AND_SEARCH"
    }
    print("Test 9 (Metacognition & Self-Correction) Results:", json.dumps(res, indent=2))
    return res

if __name__ == "__main__":
    run_test()
