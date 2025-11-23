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


