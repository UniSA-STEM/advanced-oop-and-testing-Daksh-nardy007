class Zoo:
    def __init__(self, name):
        self.__name = name
        self.__animals = []
        self.__enclosures = []
        self.__staff=[]

    def addAnimal(self,animal):
        if animal not in self.__animals:
            self.__animals.append(animal)

    def removeAnimal(self,animal):
        if animal in self.__animals:
            self.__animals.remove(animal)
            for enc in self.__enclosures:
                enc.remove(animal)

    def addEnclosure(self,enclosure):
        if enclosure not in self.__enclosures:
            self.__enclosures.append(enclosure)

    def removeEnclosure(self,enclosure):
        if enclosure in self.__enclosures:
            self.__enclosures.remove(enclosure)

    def addStaff(self,staff):
        self.__staff.append(staff)

    def removeStaff(self,staff):
        self.__staff.remove(staff)

    def assignAnimalToEnclosure(self,animal,enclosure):
        enclosure.addAnimal(animal)

    def getAnimals(self):
        return list(self.__animals)

    def getEnclosures(self):
        return list(self.__enclosures)

    def getStaff(self):
        return list(self.__staff)
