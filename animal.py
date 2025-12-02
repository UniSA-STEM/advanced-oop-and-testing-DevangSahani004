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