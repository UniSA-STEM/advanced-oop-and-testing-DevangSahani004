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

    def eat(self):
        return f"{self.__name} is eating according to {self.__diet} diet."

    def sleep(self):
        return f"{self.__name} is sleeping."

    def make_sound(self):
        return f"{self.__name} makes a sound."