import json
import random

class EmergentAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.knowledge = random.randint(1, 10)

    def communicate(self, other_agent):
        # Emergent consensus protocol
        shared = round((self.knowledge + other_agent.knowledge) / 2)
        self.knowledge = shared
        other_agent.knowledge = shared

def run_test():
    agents = [EmergentAgent(i) for i in range(10)]
    initial_states = [a.knowledge for a in agents]

    # Run consensus rounds
    for _ in range(120):
        a1, a2 = random.sample(agents, 2)
        a1.communicate(a2)

    final_states = [a.knowledge for a in agents]
    consensus_reached = len(set(final_states)) == 1

    res = {
        "num_agents": 10,
        "initial_variance": initial_states,
        "final_states": final_states,
        "consensus_reached": consensus_reached
    }
    print("Test 4 (Multi-Agent Emergence) Results:", json.dumps(res, indent=2))
    return res

if __name__ == "__main__":
    run_test()
