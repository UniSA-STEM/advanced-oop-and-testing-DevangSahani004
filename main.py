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

print("\n--- Health Check ---")
lion.add_health_record("Broken paw", "2025-12-02", "High", "Bandaged and resting")   # add a health issue
print(vet.check_health(lion))   # vet checks the lion's health records

print("\n--- Enclosure Restriction ---")
new_enclosure = Enclosure("Backup Enclosure", 300, "Savannah")   # another enclosure
print(new_enclosure.add_animal(lion))   # shouldn't go through  because lion is under treatment

print("\n--- Staff Assignment ---")
print(keeper.assign_to_enclosure(savannah))   # assign keeper to the savannah enclosure
print(f"{keeper.get_name()} is assigned to: {keeper.get_assignment().get_name()}")   # confirm assignment

# various different health records for testing purposes
lion.add_health_record("Routine check-up", "2025-12-03", "Low", "No issues found")
print(lion.get_health_report())
lion.add_health_record("Routine check-up", "2025-11-28", "Medium", "Unsure. Requires specialist.")
print(lion.get_health_report())
lion.add_health_record("Treatment", "2025-11-30", "High", "Requires urgent surgery.")
print(lion.get_health_report())   # print full health report