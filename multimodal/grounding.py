"""
Multi-Modal Causal World Model & Grounding Engine.
Supports counterfactual reasoning across vision, audio, and symbolic concepts.
"""

from typing import Any, Dict, List
from multimodal.embeddings import embed_audio_frequencies, embed_image_matrix, embed_text
from multimodal.fusion import CrossModalFusion


class MultiModalWorldModel:
    """Grounds sensory observations into structured physical and semantic dynamics."""

    def __init__(self):
        self.fusion_engine = CrossModalFusion()
        self.grounded_entities: Dict[str, Dict[str, Any]] = {}

    def observe_entity(
        self,
        entity_name: str,
        text_desc: str,
        pixel_grid: List[List[float]],
        frequencies: List[float],
    ) -> Dict[str, Any]:
        """Grounds an entity via multi-modal perception."""
        t_emb = embed_text(text_desc)
        v_emb = embed_image_matrix(pixel_grid)
        a_emb = embed_audio_frequencies(frequencies)

        fused, weights = self.fusion_engine.fuse(t_emb, v_emb, a_emb)
        record = {
            "entity": entity_name,
            "fused_embedding": fused,
            "weights": weights,
            "coherence": weights.get("coherence", 0.0),
            "state": "ACTIVE",
        }
        self.grounded_entities[entity_name] = record
        return record

    def counterfactual_intervention(self, entity_name: str, do_action: str) -> Dict[str, Any]:
        """Pearl Causality Level 3: Simulates 'What if we intervened with do(action)?' on multi-modal state."""
        if entity_name not in self.grounded_entities:
            raise KeyError(f"Entity '{entity_name}' is not grounded in the world model.")

        entity = self.grounded_entities[entity_name]
        original_state = entity["state"]

        # Counterfactual intervention logic
        if do_action == "mute_acoustic_output":
            predicted_audio_coherence = entity["weights"].get("audio", 0.0) * 0.05
            predicted_state = "MUTED"
        elif do_action == "occlude_visual_field":
            predicted_audio_coherence = entity["weights"].get("vision", 0.0) * 0.02
            predicted_state = "OCCLUDED"
        elif do_action == "apply_emergency_brake":
            predicted_audio_coherence = 0.95
            predicted_state = "HALTED"
        else:
            predicted_audio_coherence = entity["coherence"]
            predicted_state = "MODIFIED"

        return {
            "entity": entity_name,
            "do_action": do_action,
            "factual_state": original_state,
            "counterfactual_state": predicted_state,
            "predicted_coherence": predicted_audio_coherence,
            "counterfactual_valid": predicted_state != original_state,
        }
