"""
entropy.py

Shannon Entropy Engine
"""

from collections import Counter
from math import log2
from typing import List


class EntropyEngine:
    """
    Computes Shannon entropy.
    """

    @staticmethod
    def shannon(values: List[str]) -> float:

        if not values:
            return 0.0

        counts = Counter(values)

        total = len(values)

        entropy = 0.0

        for count in counts.values():
            probability = count / total
            entropy -= probability * log2(probability)

        return entropy