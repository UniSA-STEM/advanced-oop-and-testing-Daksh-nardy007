from animal import Animal

class Bird(Animal):
    def makeSound(self):
        return self.getName()+" chirping."