"""Multi-Modal Cognition, Vector Embeddings & Sensory Fusion (v2.0)"""

from multimodal.embeddings import (
    EMBEDDING_DIM,
    embed_text,
    embed_image_matrix,
    embed_audio_frequencies,
    cosine_similarity,
)
from multimodal.fusion import CrossModalFusion
from multimodal.grounding import MultiModalWorldModel

__all__ = [
    "EMBEDDING_DIM",
    "embed_text",
    "embed_image_matrix",
    "embed_audio_frequencies",
    "cosine_similarity",
    "CrossModalFusion",
    "MultiModalWorldModel",
]
