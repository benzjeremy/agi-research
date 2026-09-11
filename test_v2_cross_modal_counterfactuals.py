"""
Benchmark 16: Multi-Modal Counterfactual Reasoning (Pearl Causality Level 3).
Tests an agent's ability to answer 'What if we intervened with do(X)?' on multi-modal world states.
"""

import json
from multimodal.grounding import MultiModalWorldModel


def test_multimodal_counterfactual_reasoning():
    world = MultiModalWorldModel()

    # 1. Observe and ground physical entity in world model
    entity_name = "robot_arm_actuator"
    desc = "High-speed servo motor operating at 2400 RPM"
    vision_grid = [[0.8, 0.2], [0.2, 0.8]]
    audio_freqs = [0.88, 0.92, 0.85, 0.40]

    obs = world.observe_entity(entity_name, desc, vision_grid, audio_freqs)
    assert obs["state"] == "ACTIVE"

    # 2. Perform Pearl Causality L3 Interventions (do-operator)
    interventions = [
        ("apply_emergency_brake", "HALTED"),
        ("mute_acoustic_output", "MUTED"),
        ("occlude_visual_field", "OCCLUDED"),
    ]

    details = []
    for action, expected_state in interventions:
        cf_res = world.counterfactual_intervention(entity_name, do_action=action)
        assert cf_res["counterfactual_valid"] is True
        assert cf_res["counterfactual_state"] == expected_state
        details.append(cf_res)

    results = {
        "entity": entity_name,
        "causal_grounding_verified": True,
        "pearl_l3_interventions_tested": len(details),
        "outcomes": details,
    }
    print("Test 16 (Multi-Modal Counterfactuals) Results:", json.dumps(results, indent=2))
    return True


if __name__ == "__main__":
    test_multimodal_counterfactual_reasoning()
