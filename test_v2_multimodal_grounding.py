"""
Benchmark 15: Cross-Modal 512-Dimensional Latent Fusion & Semantic Alignment.
Verifies attention-weighted integration of text, vision matrix, and acoustic spectra.
"""

import json
from multimodal.embeddings import (
    EMBEDDING_DIM,
    cosine_similarity,
    embed_audio_frequencies,
    embed_image_matrix,
    embed_text,
)
from multimodal.fusion import CrossModalFusion


def test_multimodal_latent_fusion():
    fusion = CrossModalFusion()

    # 1. Generate heterogeneous sensory inputs
    text_input = "Autonomous vehicle detects pedestrian at crosswalk"
    # 4x4 visual patch representing human silhouette
    vision_patch = [
        [0.1, 0.9, 0.9, 0.1],
        [0.2, 0.9, 0.9, 0.2],
        [0.1, 0.8, 0.8, 0.1],
        [0.2, 0.7, 0.7, 0.2],
    ]
    # Acoustic FFT spectrum: footsteps + street audio
    audio_spectrum = [0.15, 0.45, 0.82, 0.65, 0.30, 0.10, 0.05, 0.02]

    # 2. Project into 512-dim normalized spaces
    t_emb = embed_text(text_input)
    v_emb = embed_image_matrix(vision_patch)
    a_emb = embed_audio_frequencies(audio_spectrum)

    assert len(t_emb) == EMBEDDING_DIM
    assert len(v_emb) == EMBEDDING_DIM
    assert len(a_emb) == EMBEDDING_DIM

    # 3. Fuse across modalities with cross-attention
    fused_vector, attention_meta = fusion.fuse(t_emb, v_emb, a_emb)

    assert len(fused_vector) == EMBEDDING_DIM
    assert "text" in attention_meta and "vision" in attention_meta and "audio" in attention_meta
    assert attention_meta["coherence"] > 0.0

    # Verify cosine alignment is non-zero and stable
    t_sim = cosine_similarity(fused_vector, t_emb)
    v_sim = cosine_similarity(fused_vector, v_emb)
    a_sim = cosine_similarity(fused_vector, a_emb)

    results = {
        "embedding_dim": EMBEDDING_DIM,
        "attention_weights": attention_meta,
        "alignment_scores": {"text_fusion": t_sim, "vision_fusion": v_sim, "audio_fusion": a_sim},
        "multimodal_coherent": True,
    }
    print("Test 15 (Multi-Modal Latent Fusion) Results:", json.dumps(results, indent=2))

    assert t_sim > 0.1 and v_sim > 0.1, "Fused latent vector poorly aligned with source modalities"
    return True


if __name__ == "__main__":
    test_multimodal_latent_fusion()
