'''
File: tests.py
Description: A brief description of this Python module.
Author: Daksh Narang
ID: 110402195
Username: Nardy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

import unittest

from animal import Animal
from Mammal import Mammal
from Bird import Bird
from Reptile import Reptile
from enclosure import Enclosure
from HealthRecord import HealthRecord
from Zoo import Zoo
from zookeeper import Zookeeper


class TestZooSystem(unittest.TestCase):

    def test_animal_initial_state(self):
        animal = Animal("Roo", "Kangaroo", 6, "herbivore", "Mammal", "outback")
        self.assertEqual(animal.getName(), "Roo")
        self.assertEqual(animal.getSpecies(), "Kangaroo")
        self.assertEqual(animal.getAge(), 6)
        self.assertEqual(animal.getDiet(), "herbivore")
        self.assertEqual(animal.getCategory(), "Mammal")
        self.assertEqual(animal.getEnvironment(), "outback")
        self.assertEqual(animal.getHunger(), 60)

    def test_animal_feeding_reduces_hunger(self):
        animal = Animal("Roo", "Kangaroo", 6, "herbivore", "Mammal", "outback")
        msg = animal.feedAnimal(30)
        self.assertEqual(animal.getHunger(), 30)
        self.assertEqual(msg, "Now hunger is 30")

    def test_animal_feeding_not_below_zero(self):
        animal = Animal("Roo", "Kangaroo", 6, "herbivore", "Mammal", "outback")
        msg = animal.feedAnimal(200)
        self.assertEqual(animal.getHunger(), 0)
        self.assertEqual(msg, "Now hunger is 0")

    def test_animal_and_subclass_sounds(self):
        base = Animal("Generic", "Unknown", 1, "mixed", "Other", "anywhere")
        mammal = Mammal("Roo", "Kangaroo", 6, "herbivore", "Mammal", "outback")
        bird = Bird("Pebble", "Little Penguin", 3, "piscivore", "Bird", "coastal_aviary")
        reptile = Reptile("Stumpy", "Shingleback", 5, "insectivore", "Reptile", "outback")

        self.assertIn("makes sound", base.makeSound())
        self.assertIn("ooo aaaa", mammal.makeSound())
        self.assertIn("chirping", bird.makeSound())
        self.assertIn("hiss", reptile.makeSound().lower())
