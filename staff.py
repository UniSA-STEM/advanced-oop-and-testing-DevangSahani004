'''
File: staff.py
Description: A brief description of this Python module.
Author: Devang Sahani
ID: 110411585
Username: sahdy004
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    """represents a generic staff member in the zoo"""
    def __init__(self, name, role):
        self.__name = name   # staff member's name
        self.__role = role   # role type like zookeeper or veterinarian
        self.__assigned = None   # track which enclosure they are assigned to

    def get_name(self):
        return self.__name   # getter method to return the staff member's name

    def get_role(self):
        return self.__role   # getter method to return the staff member's role

    def assign_to_enclosure(self, enclosure):
        self.__assigned = enclosure   # assign staff to a specific enclosure
        return f"{self.get_name()} is now assigned to {enclosure.get_name()}."   # confirmation message

    def get_assignment(self):
        return self.__assigned   # getter method to return the enclosure details the staff is assigned to

class Zookeeper(Staff):
    """represents a zookeeper, inherits from staff"""
    def __init__(self, name):
        super().__init__(name, "Zookeeper")   # call parent constructor with role set to zookeeper

    def feed_animal(self, animal):
        return f"{self.get_name()} feeds {animal.get_name()}."   # method for zookeeper to feed an animal

    def clean_enclosure(self, enclosure):
        return f"{self.get_name()} cleans {enclosure.get_name()}."   # method for zookeeper to clean an enclosure

class Veterinarian(Staff):
    """represents a veterinarian, inherits from staff"""

    def __init__(self, name):
        super().__init__(name, "Veterinarian")   # call parent constructor with role set to veterinarian

    def check_health(self, animal):
        records = animal.get_health_records()   # get health records of a specific animal
        if records:   # if there are records
            latest = records[-1]   # look at the most recent one
            return (f"{self.get_name()} reviews health records of {animal.get_name()}:\n"
                    f"Issue: {latest['description']}, Date: {latest['date']}, "
                    f"Severity: {latest['severity']}, Treatment: {latest['treatment']}")   # show details
        return f"{self.get_name()} finds no health issues for {animal.get_name()}."   # if no records exist