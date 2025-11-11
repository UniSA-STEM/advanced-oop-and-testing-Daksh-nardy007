'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Enclosure:
    def __init__(self,name, environment, capacity):
        self.name = name
        self.environment = environment
        self.capacity = capacity
        self.cleanliness = 100
        self.animals =[]

    def addAnimal(self, animal):
        self.animals.append(animal)
    def removeAnimal(self,animal):
        if animal in self.animals:
            self.animals.remove(animal)

    def cleanEnclosure(self):
        self.cleanliness = 100
        return self.name + "cleaned"

