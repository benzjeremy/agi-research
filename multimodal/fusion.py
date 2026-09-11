"""
Cross-Modal Attention & Sensory Fusion Engine.
Fuses heterogeneous modalities (Text, Vision, Audio) with attention weights.
"""

import math
from typing import Dict, List, Tuple
from multimodal.embeddings import EMBEDDING_DIM, _normalize, cosine_similarity


class CrossModalFusion:
    """Fuses multi-modal embeddings using cross-attention weighting."""

    def __init__(self):
        self.modality_weights = {"text": 1.0, "vision": 1.0, "audio": 0.8}

    def fuse(
        self,
        text_emb: List[float],
        vision_emb: List[float],
        audio_emb: List[float],
    ) -> Tuple[List[float], Dict[str, float]]:
        """Computes cross-attended joint multi-modal representation."""
        if len(text_emb) != EMBEDDING_DIM or len(vision_emb) != EMBEDDING_DIM or len(audio_emb) != EMBEDDING_DIM:
            raise ValueError(f"All embeddings must have dimension {EMBEDDING_DIM}")

        # Compute pairwise agreement
        tv_sim = max(0.0, cosine_similarity(text_emb, vision_emb))
        ta_sim = max(0.0, cosine_similarity(text_emb, audio_emb))
        va_sim = max(0.0, cosine_similarity(vision_emb, audio_emb))

        # Dynamic softmax attention weights
        raw_weights = [
            self.modality_weights["text"] * (1.0 + tv_sim + ta_sim),
            self.modality_weights["vision"] * (1.0 + tv_sim + va_sim),
            self.modality_weights["audio"] * (1.0 + ta_sim + va_sim),
        ]
        sum_exp = sum(math.exp(w) for w in raw_weights)
        attn_weights = {
            "text": math.exp(raw_weights[0]) / sum_exp,
            "vision": math.exp(raw_weights[1]) / sum_exp,
            "audio": math.exp(raw_weights[2]) / sum_exp,
        }

        # Weighted latent superposition
        fused_vec = [0.0] * EMBEDDING_DIM
        for i in range(EMBEDDING_DIM):
            fused_vec[i] = (
                attn_weights["text"] * text_emb[i]
                + attn_weights["vision"] * vision_emb[i]
                + attn_weights["audio"] * audio_emb[i]
            )

        normalized_fused = _normalize(fused_vec)
        coherence_score = (tv_sim + ta_sim + va_sim) / 3.0
        attn_weights["coherence"] = coherence_score

        return normalized_fused, attn_weights
