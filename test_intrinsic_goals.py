import json
import random

class IntrinsicGoalAgent:
    def __init__(self):
        self.known_states = set([0])
        self.intrinsic_curiosity_reward = 0
        self.goals_generated = []

    def explore_world(self, world_states):
        for state in world_states:
            # Calculate novelty / surprise (Prediction Error)
            if state not in self.known_states:
                # Intrinsic drive: Discover novel state
                novelty = 1.0
                self.intrinsic_curiosity_reward += novelty
                self.known_states.add(state)
                self.goals_generated.append(f"Master_State_{state}")
            else:
                novelty = 0.0

def run_test():
    agent = IntrinsicGoalAgent()
    unexplored_world = [0, 1, 2, 0, 3, 4, 1, 5, 6]

    agent.explore_world(unexplored_world)

    res = {
        "external_prompt_given": False,
        "intrinsic_curiosity_reward": agent.intrinsic_curiosity_reward,
        "self_generated_goals": agent.goals_generated,
        "unique_states_mastered": len(agent.known_states)
    }
    print("Test 8 (Intrinsic Motivation & Self-Goal Generation) Results:", json.dumps(res, indent=2))
    return res

if __name__ == "__main__":
    run_test()
