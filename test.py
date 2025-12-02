import pytest
from animal import Mammal
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

@pytest.fixture
def lion():
    return Mammal("Leo", "Lion", 5, "Carnivore")

@pytest.fixture
def savannah():
    return Enclosure("Savannah Enclosure", 500, "Savannah")