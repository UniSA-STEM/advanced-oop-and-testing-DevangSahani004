'''
File: main.py
Description: Script to demo the program that ties everything together, showing animals, enclosures, staff actions, and health reports.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Mammal
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

"""simple demo script to show how the zoo system works"""

# create the main objects we need
lion = Mammal("Leo", "Lion", 5, "Carnivore")   # a lion named leo
savannah = Enclosure("Savannah Enclosure", 500, "Savannah")   # big savannah enclosure
keeper = Zookeeper("Sam")   # zookeeper staff member
vet = Veterinarian("Dr. Jane")   # veterinarian staff member

print("\n--- Zoo Setup ---")
print(savannah.add_animal(lion))   # try adding the lion to the enclosure
print(savannah.report_status())   # show enclosure details

print("\n--- Staff Actions ---")
print(keeper.feed_animal(lion))   # keeper feeds the lion
print(keeper.clean_enclosure(savannah))   # keeper cleans the enclosure