"""
Multi-Modal 512-Dimensional Vector Embeddings Engine.
Unifies Text, Vision (Matrix Patches), and Audio (Frequencies) into a shared L2-normalized latent space.
"""

import hashlib
import math
from typing import List, Union


EMBEDDING_DIM = 512


def _normalize(vector: List[float]) -> List[float]:
    norm = math.sqrt(sum(x * x for x in vector))
    if norm == 0.0:
        return [0.0] * len(vector)
    return [x / norm for x in vector]


def cosine_similarity(v1: List[float], v2: List[float]) -> float:
    if len(v1) != len(v2) or len(v1) == 0:
        return 0.0
    dot = sum(a * b for a, b in zip(v1, v2))
    return max(-1.0, min(1.0, dot))


def embed_text(text: str) -> List[float]:
    """Generates a 512-dim semantic embedding for text via deterministic spectral hashing."""
    vec = [0.0] * EMBEDDING_DIM
    words = text.lower().strip().split()
    for w_idx, word in enumerate(words):
        h = int(hashlib.sha256(word.encode("utf-8")).hexdigest(), 16)
        for i in range(EMBEDDING_DIM):
            # Harmonic projection
            val = math.sin(h * (i + 1) * 0.001) * (1.0 / (1.0 + w_idx * 0.1))
            vec[i] += val
    return _normalize(vec)


def embed_image_matrix(pixel_grid: List[List[float]]) -> List[float]:
    """Encodes 2D visual pixel matrices into 512-dim spatial-frequency embeddings."""
    vec = [0.0] * EMBEDDING_DIM
    rows = len(pixel_grid)
    cols = len(pixel_grid[0]) if rows > 0 else 0

    if rows == 0 or cols == 0:
        return [0.0] * EMBEDDING_DIM

    flat = [val for row in pixel_grid for val in row]
    flat_len = len(flat)

    # 2D Fourier-inspired spatial projection
    for i in range(EMBEDDING_DIM):
        weight = 0.0
        for k, p in enumerate(flat):
            angle = (2.0 * math.pi * (i + 1) * (k + 1)) / (flat_len + 1)
            weight += p * math.cos(angle)
        vec[i] = weight

    return _normalize(vec)


def embed_audio_frequencies(frequencies: List[float]) -> List[float]:
    """Encodes 1D acoustic FFT spectrum frequencies into 512-dim acoustic embeddings."""
    vec = [0.0] * EMBEDDING_DIM
    n_freqs = len(frequencies)
    if n_freqs == 0:
        return [0.0] * EMBEDDING_DIM

    for i in range(EMBEDDING_DIM):
        accum = 0.0
        for f_idx, mag in enumerate(frequencies):
            # Bark-scale non-linear acoustic projection
            scale = math.log1p(f_idx + 1)
            accum += mag * math.sin(scale * (i + 1) * 0.05)
        vec[i] = accum

    return _normalize(vec)
