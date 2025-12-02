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