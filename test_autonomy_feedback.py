import time
import random
import json

class Environment:
    def __init__(self):
        self.state = {"temperature": 20, "pressure": 100, "anomaly": False}

    def mutate(self):
        # Unexpected environmental perturbation
        self.state["temperature"] += random.choice([-5, -2, 3, 8])
        if self.state["temperature"] > 25:
            self.state["anomaly"] = True

class AgentFeedbackLoop:
    def __init__(self):
        self.knowledge_base = {"rule_temp_high": "cool_down", "rule_normal": "maintain"}
        self.adaptation_score = 0

    def perceive_and_act(self, env_state):
        if env_state["anomaly"]:
            # Action required: Adapt or learn new policy
            action = "cool_down"
            self.adaptation_score += 1
            return action
        return "do_nothing"

    def learn_new_pattern(self, new_condition, action):
        self.knowledge_base[new_condition] = action

def run_test():
    env = Environment()
    agent = AgentFeedbackLoop()
    history = []

    for step in range(20):
        env.mutate()
        action = agent.perceive_and_act(env.state)
        history.append({"step": step, "env": dict(env.state), "action": action})

    results = {
        "steps": 20,
        "adaptation_score": agent.adaptation_score,
        "final_knowledge_size": len(agent.knowledge_base)
    }
    print("Test 2 (Autonomie & Feedback) Results:", json.dumps(results, indent=2))
    return results

if __name__ == "__main__":
    run_test()
