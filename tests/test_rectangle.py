import pytest
from shapes.rectangle import Rectangle

pytestmark = pytest.mark.rectangle

def test_rectangle_area(my_rectangle):

    assert my_rectangle.area() == 40


def test_rectangle_perimeter(my_rectangle):

    assert my_rectangle.perimeter() == 28


def test_rectangle_is_square(square):
    assert square.is_square()


def test_rectangle_is_not_square(my_rectangle):

    assert not my_rectangle.is_square()


def test_error_negative_width():
    with pytest.raises(ValueError):
        Rectangle(width=-4, height=5)


def test_error_negative_height():
    with pytest.raises(ValueError):
        Rectangle(width=4, height=-10)

@pytest.mark.skip
def test_circle_area_bigger_than_rectangle_area(my_rectangle, circle):
    assert my_rectangle.area() < circle.area()


@pytest.mark.parametrize("width, height, expected_area", [(10, 10, 100), (4, 5, 20), (2, 1, 2)])
def test_multiple_rectangle_areas(width, height, expected_area):
    assert Rectangle(width, height).area() == expected_area