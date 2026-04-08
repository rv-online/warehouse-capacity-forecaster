
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class UtilizationPoint:
    day: int
    utilization: float
