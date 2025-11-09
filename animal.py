'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''
class Animal:
    def __init__(self, name, species, age, diet, category, environment):
        self.__name= name
        self.__species = species
        self.__age = age
        self.__diet = diet
        self.__category = category
        self.__environment = environment
        self.__health_record = None

    def getName(self):
        return self.__name
    def getSpecies(self):
        return self.__species
    def getAge(self):
        return self.__age
    def getDiet(self):
        return self.__diet
    def getCategory(self):
        return self.__category
    def getEnvironment(self):
        return self.__environment

    def makeSound(self):
        return self.__name+' makes sound.'
    def eat(self):
        return self.__name+'eats'+self.__diet
    def sleep(self):
        return self.__name+'is sleeping.'
    def getHealthRecord(self):
        return self.__health_record
    def addHealthRecord(self, healthRecord):
        self.__health_record = healthRecord