"""
Distributed Cluster Manager & Autonomous Agent Nodes.
Provides process/thread-level parallelism, consensus voting, and scale elasticity.
"""

import concurrent.futures
import time
from typing import Any, Callable, Dict, List, Optional
from distributed.audit import AuditTrail
from distributed.protocol import MessageType, RPCFrame


class AgentNode:
    """An autonomous cognitive agent operating in a distributed network."""

    def __init__(self, node_id: str, capabilities: Optional[List[str]] = None, cluster_token: str = ""):
        self.node_id = node_id
        self.capabilities = capabilities or ["reasoning", "ast_synthesis", "multimodal_fusion"]
        self.cluster_token = cluster_token
        self.state: Dict[str, Any] = {"status": "IDLE", "tasks_completed": 0, "current_belief": 0.0}
        self.inbox: List[RPCFrame] = []

    def receive_frame(self, frame: RPCFrame) -> Optional[RPCFrame]:
        if not frame.verify(self.cluster_token):
            return None

        self.inbox.append(frame)
        if frame.msg_type == MessageType.TASK_SUBMIT:
            return self._execute_task(frame)
        elif frame.msg_type == MessageType.CONSENSUS_VOTE:
            return self._vote_consensus(frame)
        return None

    def _execute_task(self, frame: RPCFrame) -> RPCFrame:
        task_data = frame.payload.get("task_data", {})
        op = task_data.get("op", "evaluate")
        val = task_data.get("val", 1.0)

        # Cognitive computation simulation
        result_val = val * 1.5 if op == "optimize" else val + 10.0
        self.state["tasks_completed"] += 1
        self.state["status"] = "BUSY"

        resp_payload = {
            "task_id": frame.payload.get("task_id", "unknown"),
            "result": result_val,
            "agent_node": self.node_id,
            "status": "COMPLETED",
        }
        self.state["status"] = "IDLE"
        return RPCFrame(
            msg_type=MessageType.TASK_RESULT,
            sender_id=self.node_id,
            payload=resp_payload,
            token=self.cluster_token,
        )

    def _vote_consensus(self, frame: RPCFrame) -> RPCFrame:
        proposal = frame.payload.get("proposal", 0.0)
        # Epistemic confidence weighting: converge belief towards evidence
        my_belief = self.state["current_belief"]
        updated_belief = (my_belief + proposal) / 2.0
        self.state["current_belief"] = updated_belief

        vote_payload = {
            "proposal_id": frame.payload.get("proposal_id", "p0"),
            "vote": True,
            "updated_belief": updated_belief,
        }
        return RPCFrame(
            msg_type=MessageType.CONSENSUS_COMMIT,
            sender_id=self.node_id,
            payload=vote_payload,
            token=self.cluster_token,
        )


class ClusterManager:
    """Orchestrates distributed SEAN agents across virtual nodes."""

    def __init__(self, cluster_id: str = "SEAN-CLUSTER-ALPHA", token: str = "sec_token_99x_sha256"):
        self.cluster_id = cluster_id
        self.token = token
        self.nodes: Dict[str, AgentNode] = {}
        self.audit_trail = AuditTrail()

    def register_node(self, node_id: str, capabilities: Optional[List[str]] = None) -> AgentNode:
        node = AgentNode(node_id, capabilities, cluster_token=self.token)
        self.nodes[node_id] = node
        self.audit_trail.record_action(
            agent_id=node_id,
            action="NODE_REGISTERED",
            details={"node_id": node_id, "capabilities": node.capabilities},
        )
        return node

    def scale_cluster(self, target_nodes: int) -> int:
        """Elastic scale up or down."""
        current = len(self.nodes)
        if target_nodes > current:
            for i in range(current, target_nodes):
                nid = f"agent-node-{i+1:02d}"
                self.register_node(nid)
        return len(self.nodes)

    def run_parallel_cognitive_workload(self, task_list: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Distributes tasks concurrently over registered nodes and measures efficiency."""
        node_ids = list(self.nodes.keys())
        if not node_ids:
            return []

        results = []
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(len(node_ids), 32)) as executor:
            futures = []
            for i, task in enumerate(task_list):
                target_node = self.nodes[node_ids[i % len(node_ids)]]
                frame = RPCFrame(
                    msg_type=MessageType.TASK_SUBMIT,
                    sender_id=self.cluster_id,
                    payload={"task_id": f"task_{i:03d}", "task_data": task},
                    token=self.token,
                )
                futures.append(executor.submit(target_node.receive_frame, frame))

            for fut in concurrent.futures.as_completed(futures):
                resp = fut.result()
                if resp:
                    results.append(resp.payload)
                    self.audit_trail.record_action(
                        agent_id=resp.sender_id,
                        action="TASK_COMPLETED",
                        details={"task_id": resp.payload.get("task_id")},
                    )

        return results

    def reach_epistemic_consensus(self, proposal_value: float, rounds: int = 3) -> Dict[str, Any]:
        """Runs iterative consensus rounds across all cluster nodes."""
        node_ids = list(self.nodes.keys())
        if not node_ids:
            return {"converged": False, "variance": 1.0}

        # Initialize varied beliefs
        for i, nid in enumerate(node_ids):
            self.nodes[nid].state["current_belief"] = float((i * 7) % 50)

        for r in range(rounds):
            frame = RPCFrame(
                msg_type=MessageType.CONSENSUS_VOTE,
                sender_id=self.cluster_id,
                payload={"proposal_id": f"round_{r}", "proposal": proposal_value},
                token=self.token,
            )
            for node in self.nodes.values():
                node.receive_frame(frame)

        final_beliefs = [n.state["current_belief"] for n in self.nodes.values()]
        mean_b = sum(final_beliefs) / len(final_beliefs)
        variance = sum((b - mean_b) ** 2 for b in final_beliefs) / len(final_beliefs)
        converged = variance < 0.1

        self.audit_trail.record_action(
            agent_id="CLUSTER_CONSENSUS",
            action="CONSENSUS_FINALIZED",
            details={"nodes": len(self.nodes), "variance": variance, "converged": converged},
        )

        return {
            "converged": converged,
            "variance": variance,
            "mean_belief": mean_b,
            "participating_nodes": len(self.nodes),
        }
