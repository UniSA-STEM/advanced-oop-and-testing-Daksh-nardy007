from animal import Animal

class Mammal(Animal):
    def makeSound(self):
        return self.getName()+" ooo aaaa."