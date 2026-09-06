import time
import json
import random

class RealityEnvironment:
    def __init__(self):
        # Physical world state: Non-deterministic and partially observable
        self.hidden_physics = {"friction": 0.85, "gravity": 9.81, "wind": 2.1}
        self.observed_state = {"velocity": 10.0, "position": 0.0}

    def step(self, force):
        # Physics outcome changes with hidden variable shifts
        self.hidden_physics["wind"] += random.uniform(-0.5, 0.5)
        actual_accel = (force / 2.0) - (self.hidden_physics["friction"] * self.hidden_physics["wind"])
        self.observed_state["velocity"] += actual_accel
        self.observed_state["position"] += self.observed_state["velocity"]
        return self.observed_state

class WorldModelAgent:
    def __init__(self):
        self.internal_world_model = {"estimated_friction": 0.5}
        self.prediction_errors = []

    def predict_and_act(self, target_pos, env):
        # Predict outcome using current internal model
        predicted_force = (target_pos - env.observed_state["position"]) * 0.5
        
        # Execute in real non-deterministic environment
        actual_state = env.step(predicted_force)
        
        # Calculate prediction error (Grounding gap)
        error = abs(target_pos - actual_state["position"])
        self.prediction_errors.append(error)

        # Update internal world model dynamically
        if error > 2.0:
            self.internal_world_model["estimated_friction"] += 0.05
        return actual_state

def run_test():
    env = RealityEnvironment()
    agent = WorldModelAgent()

    for t in range(30):
        agent.predict_and_act(target_pos=100.0, env=env)

    res = {
        "steps": 30,
        "mean_prediction_error": sum(agent.prediction_errors) / len(agent.prediction_errors),
        "world_model_adapted": agent.internal_world_model["estimated_friction"] > 0.5
    }
    print("Test 5 (Causal World Model & Grounding) Results:", json.dumps(res, indent=2))
    return res

if __name__ == "__main__":
    run_test()
