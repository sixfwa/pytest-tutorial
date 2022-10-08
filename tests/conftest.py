import pytest
from shapes.circle import Circle
from shapes.rectangle import Rectangle


@pytest.fixture
def circle():
    return Circle(radius=10)


@pytest.fixture
def my_rectangle():
    return Rectangle(width=10, height=4)


@pytest.fixture
def square():
    return Rectangle(width=10, height=10)
