"""
SEAN Distributed RPC & Epistemic Consensus Protocol
Pure Python zero-dependency asynchronous messaging with cryptographic token verification.
"""

import hashlib
import hmac
import json
import time
from typing import Any, Dict, Optional


class MessageType:
    JOIN = "JOIN"
    HEARTBEAT = "HEARTBEAT"
    TASK_SUBMIT = "TASK_SUBMIT"
    TASK_RESULT = "TASK_RESULT"
    CONSENSUS_VOTE = "CONSENSUS_VOTE"
    CONSENSUS_COMMIT = "CONSENSUS_COMMIT"
    SYNC_STATE = "SYNC_STATE"


class RPCFrame:
    """Standardized message frame for distributed agent communication."""

    def __init__(
        self,
        msg_type: str,
        sender_id: str,
        payload: Dict[str, Any],
        token: str = "",
        timestamp: Optional[float] = None,
    ):
        self.msg_type = msg_type
        self.sender_id = sender_id
        self.payload = payload
        self.timestamp = timestamp or time.time()
        self.token = token
        self.signature = self._compute_signature()

    def _compute_signature(self) -> str:
        data = f"{self.msg_type}:{self.sender_id}:{self.timestamp}:{json.dumps(self.payload, sort_keys=True)}"
        if self.token:
            return hmac.new(self.token.encode(), data.encode(), hashlib.sha256).hexdigest()
        return hashlib.sha256(data.encode()).hexdigest()

    def verify(self, expected_token: str = "") -> bool:
        """Verifies integrity and authenticity of the frame."""
        data = f"{self.msg_type}:{self.sender_id}:{self.timestamp}:{json.dumps(self.payload, sort_keys=True)}"
        if expected_token or self.token:
            token = expected_token or self.token
            expected_sig = hmac.new(token.encode(), data.encode(), hashlib.sha256).hexdigest()
            return hmac.compare_digest(self.signature, expected_sig)
        expected_sig = hashlib.sha256(data.encode()).hexdigest()
        return hmac.compare_digest(self.signature, expected_sig)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "msg_type": self.msg_type,
            "sender_id": self.sender_id,
            "payload": self.payload,
            "timestamp": self.timestamp,
            "token": self.token,
            "signature": self.signature,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RPCFrame":
        frame = cls(
            msg_type=data["msg_type"],
            sender_id=data["sender_id"],
            payload=data["payload"],
            token=data.get("token", ""),
            timestamp=data.get("timestamp"),
        )
        frame.signature = data.get("signature", "")
        return frame
