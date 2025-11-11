'''
File: zookeeper.py
Description: A brief description of this Python module.
Author: Daksh Narang
ID: 110402195
Username: Nardy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from staff import Staff

class Zookeeper(Staff):
    def __init__(self, name):
        super().__init__(name, "Zookeeper")
    def feedAnimal(self):
        log = []
        if not self.assignedAnimals:
            for enc in self.assignedEnclosures:
                for animal in enc.animals:
                    self.assignedAnimals.append(animal)

        for animal in self.assignedAnimals:
            animal.feedAnimal(30)

    def cleanEnclosure(self):
        for enc in self.assignedEnclosures:
            enc.cleanEnclosure()

    def duty(self):
        return "Perform cleaning and feeding"