
from __future__ import annotations

import json

from .engine import forecast
from .models import UtilizationPoint


def main() -> None:
    points = [
        UtilizationPoint(1, 58.0),
        UtilizationPoint(2, 62.0),
        UtilizationPoint(3, 66.0),
        UtilizationPoint(4, 69.0),
    ]
    print(json.dumps({"forecast_day_7": forecast(points, 3)}, indent=2))


if __name__ == "__main__":
    main()
