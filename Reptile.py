from animal import Animal

class Reptile(Animal):
    def makeSound(self):
        return self.getName()+" hissssss."