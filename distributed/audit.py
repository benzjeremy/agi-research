"""
Immutable Epistemic Audit Trail for Distributed Cognition.
Guarantees tamper-evident execution tracing across distributed agents.
"""

import hashlib
import json
import time
from typing import Any, Dict, List, Optional


class AuditRecord:
    def __init__(
        self,
        index: int,
        agent_id: str,
        action: str,
        details: Dict[str, Any],
        prev_hash: str,
        timestamp: Optional[float] = None,
    ):
        self.index = index
        self.agent_id = agent_id
        self.action = action
        self.details = details
        self.prev_hash = prev_hash
        self.timestamp = timestamp or time.time()
        self.hash = self.compute_hash()

    def compute_hash(self) -> str:
        content = (
            f"{self.index}:{self.agent_id}:{self.action}:{self.prev_hash}:"
            f"{self.timestamp}:{json.dumps(self.details, sort_keys=True)}"
        )
        return hashlib.sha256(content.encode("utf-8")).hexdigest()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "index": self.index,
            "agent_id": self.agent_id,
            "action": self.action,
            "details": self.details,
            "prev_hash": self.prev_hash,
            "timestamp": self.timestamp,
            "hash": self.hash,
        }


class AuditTrail:
    """Tamper-evident ledger of all cognitive decisions and consensus commits."""

    GENESIS_HASH = "0000000000000000000000000000000000000000000000000000000000000000"

    def __init__(self):
        self.records: List[AuditRecord] = []
        # Add genesis record
        genesis = AuditRecord(
            index=0,
            agent_id="SYSTEM_ROOT",
            action="GENESIS_INIT",
            details={"version": "2.0", "standard": "ISO-25010-Security"},
            prev_hash=self.GENESIS_HASH,
        )
        self.records.append(genesis)

    def record_action(self, agent_id: str, action: str, details: Dict[str, Any]) -> AuditRecord:
        prev_hash = self.records[-1].hash
        rec = AuditRecord(
            index=len(self.records),
            agent_id=agent_id,
            action=action,
            details=details,
            prev_hash=prev_hash,
        )
        self.records.append(rec)
        return rec

    def verify_integrity(self) -> bool:
        """Verifies the complete cryptographic chain of the ledger."""
        for i in range(1, len(self.records)):
            curr = self.records[i]
            prev = self.records[i - 1]

            if curr.prev_hash != prev.hash:
                return False
            if curr.hash != curr.compute_hash():
                return False
        return True

    def get_latest_hash(self) -> str:
        return self.records[-1].hash
