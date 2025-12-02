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

def test_add_animal_success(lion, savannah):
    result = savannah.add_animal(lion)
    assert "Leo added" in result
    assert lion in savannah.get_animals()