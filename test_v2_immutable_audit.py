"""
Benchmark 18: Cryptographic Immutable Audit Trail & Tamper Resistance.
Proves tamper-evident detection of unauthorized state modifications in distributed agent logs.
"""

import json
from distributed.audit import AuditTrail


def test_immutable_audit_trail_tamper_defense():
    trail = AuditTrail()

    # 1. Record series of distributed cognitive actions
    trail.record_action("agent-node-01", "HYPOTHESIS_PROPOSED", {"hypothesis_id": "H_101"})
    trail.record_action("agent-node-02", "AST_VERIFIED", {"verified": True})
    trail.record_action("agent-node-03", "CONSENSUS_COMMITTED", {"status": "SUCCESS"})

    # Verify untampered integrity
    assert trail.verify_integrity() is True, "Legitimate audit trail failed verification"

    # 2. Simulate adversarial tamper attempt on historical block 1
    original_action = trail.records[1].action
    trail.records[1].action = "MALICIOUS_TAMPERED_ACTION"

    # Integrity verification MUST fail
    tamper_detected = not trail.verify_integrity()
    assert tamper_detected is True, "Cryptographic audit trail failed to detect malicious tampering!"

    # 3. Restore and verify self-healing integrity validation
    trail.records[1].action = original_action
    assert trail.verify_integrity() is True, "Audit trail failed to validate after restoring integrity"

    metrics = {
        "records_logged": len(trail.records),
        "latest_block_hash": trail.get_latest_hash(),
        "adversarial_tamper_detected": tamper_detected,
        "cryptographic_defense_passed": True,
    }
    print("Test 18 (Immutable Audit Trail) Results:", json.dumps(metrics, indent=2))
    return True


if __name__ == "__main__":
    test_immutable_audit_trail_tamper_defense()
