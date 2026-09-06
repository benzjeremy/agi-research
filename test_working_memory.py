import time
import json
import random

class WorkingMemory:
    def __init__(self, capacity=7):
        self.capacity = capacity
        self.memory = []

    def add(self, item):
        if len(self.memory) >= self.capacity:
            # Miller's Law limit reached: decay/evict oldest item
            evicted = self.memory.pop(0)
        self.memory.append(item)

    def retrieve(self, query):
        return [item for item in self.memory if query in str(item)]

class TaskContext:
    def __init__(self, goal):
        self.goal = goal
        self.completed_subtasks = []
        self.subtasks = []

    def decompose(self):
        # Dynamically decompose complex goal into sequential reasoning steps
        self.subtasks = [f"Subtask {i+1} for {self.goal}" for i in range(3)]

class AgentReasoningLoop:
    def __init__(self):
        self.wm = WorkingMemory(capacity=7)

    def run_benchmark(self, num_iterations=100):
        results = {"success": 0, "evictions": 0}
        for i in range(num_iterations):
            task = f"Fact_{i}"
            self.wm.add(task)
            if len(self.wm.memory) == 7:
                results["evictions"] += 1
            # Check retrieval efficiency under load
            if self.wm.retrieve(task):
                results["success"] += 1
        return results

if __name__ == "__main__":
    agent = AgentReasoningLoop()
    res = agent.run_benchmark(50)
    print("Benchmark Working Memory Results:", json.dumps(res, indent=2))
