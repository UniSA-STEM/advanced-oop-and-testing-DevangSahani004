'''
File: animal.py
Description: Defines animals with attributes, behaviors, and health records, plus child classes for sound differences.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Animal:
    """represents a generic animal"""
    def __init__(self, name, species, age, diet):
        self.__name = name   # private name
        self.__species = species   # species type
        self.__age = age   # age of the animal
        self.__diet = diet   # diet type
        self.__health_records = []

    def eat(self):
        return f"{self.__name} is currently eating according to {self.__diet} diet."  # method for basic eating action

    def sleep(self):
        return f"{self.__name} is currently sleeping. Shh, do not disturb!"  # method for simple sleep action

    def make_sound(self):
        return f"{self.__name} is making a sound."  # generic sound, overridden in child classes

    def add_health_record(self, description, date_reported, severity, treatment_notes):
        record = {
            "description": description,   # what the issue is
            "date": date_reported,   # when it was reported
            "severity": severity,   # how serious the damage is
            "treatment": treatment_notes   # notes on treatment
        }
        self.__health_records.append(record)   # add the record to the list

    def get_health_records(self):
        return self.__health_records   # getter method to return all health records

    def get_name(self):
        return self.__name   # getter method to return the animal name (private attribute)

    def get_species(self):
        return self.__species   # getter method to return the species details

    def get_age(self):
        return self.__age   # getter method to return the age

    def get_diet(self):
        return self.__diet  # getter method to return the animal diet

    def is_under_treatment(self):
        if self.__health_records:   # check if there are any records
            latest = self.__health_records[-1]   # look at the most recent one
            if "severity" in latest:   # make sure severity exists
                return latest["severity"].lower() == "high"   # if severity is high, animal is under treatment
        return False   # either there no records or aren't considered severe