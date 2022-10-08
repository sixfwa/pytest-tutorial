import math
from shapes.circle import Circle
import pytest

pytestmark = pytest.mark.circle

class TestCircle:

    def test_area(self, circle):
        assert circle.area() == math.pi * circle.radius**2

    def test_negative_radius(self):
        with pytest.raises(ValueError):
            Circle(radius=-5)
