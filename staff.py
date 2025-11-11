'''
File: staff.py
Description: A brief description of this Python module.
Author: Daksh Narang
ID: 110402195
Username: Nardy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Staff:
    def __init__(self,name, role):
        self.name = name
        self.role = role
        self.assignedAnimals = []
        self.assignedEnclosures=[]

    def assignToAnimal(self, animal):
        self.assignedAnimals.append(animal)

    def assignToEnclosure(self, enclosure):
        self.assignedEnclosures.append(enclosure)

    def duty(self):
        return "Perform zoo duties."
