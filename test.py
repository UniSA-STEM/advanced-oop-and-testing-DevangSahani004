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

def test_health_restriction(lion, savannah):
    lion.add_health_record("Broken paw", "2025-12-02", "High", "Bandaged")
    result = savannah.add_animal(lion)
    assert "cannot be moved" in result
    assert lion not in savannah.get_animals()