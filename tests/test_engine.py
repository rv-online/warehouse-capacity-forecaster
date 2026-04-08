
import unittest

from src.engine import forecast, slope
from src.models import UtilizationPoint


class ForecastTests(unittest.TestCase):
    def setUp(self) -> None:
        self.points = [
            UtilizationPoint(1, 50.0),
            UtilizationPoint(2, 55.0),
            UtilizationPoint(3, 60.0),
            UtilizationPoint(4, 65.0),
        ]

    def test_positive_slope(self) -> None:
        self.assertGreater(slope(self.points), 0)

    def test_forecast_increases(self) -> None:
        self.assertGreater(forecast(self.points, 2), 65.0)


if __name__ == "__main__":
    unittest.main()
