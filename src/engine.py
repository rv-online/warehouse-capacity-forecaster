
from __future__ import annotations

from .models import UtilizationPoint


def slope(points: list[UtilizationPoint]) -> float:
    count = len(points)
    x_mean = sum(point.day for point in points) / count
    y_mean = sum(point.utilization for point in points) / count
    numerator = sum((point.day - x_mean) * (point.utilization - y_mean) for point in points)
    denominator = sum((point.day - x_mean) ** 2 for point in points) or 1.0
    return numerator / denominator


def forecast(points: list[UtilizationPoint], days_ahead: int) -> float:
    trend = slope(points)
    latest = max(points, key=lambda point: point.day)
    return round(latest.utilization + trend * days_ahead, 2)
