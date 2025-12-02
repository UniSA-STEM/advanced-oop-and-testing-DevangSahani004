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

def test_staff_feed_and_clean(lion, savannah):
    keeper = Zookeeper("Sam")
    savannah.add_animal(lion)
    assert "feeds Leo" in keeper.feed_animal(lion)
    assert "cleans Savannah Enclosure" in keeper.clean_enclosure(savannah)

def test_vet_health_check(lion):
    vet = Veterinarian("Dr. Jane")
    lion.add_health_record("Routine check-up", "2025-12-03", "Low", "No issues found")
    result = vet.check_health(lion)
    assert "Dr. Jane reviews health records of Leo" in result
    assert "Routine check-up" in result

def test_remove_animal(savannah, lion):
    savannah.add_animal(lion)
    result = savannah.remove_animal("Leo")
    assert "removed" in result
    assert lion not in savannah.get_animals()
    # Edge case: removing non-existent animal
    result = savannah.remove_animal("Tiger")
    assert "No animal named Tiger" in result