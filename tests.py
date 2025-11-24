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

    def test_health_record_string_and_resolve(self):
        record = HealthRecord("Minor flipper abrasion", "2025-11-12", "low", "Apply antiseptic daily")
        text_before = str(record)
        self.assertIn("Minor flipper abrasion", text_before)
        self.assertIn("Severity: low", text_before)
        self.assertIn("Active", text_before)

        record.resolved()
        text_after = str(record)
        self.assertIn("Resolved", text_after)

    def test_enclosure_add_remove_and_clean(self):
        enc = Enclosure("Outback Habitat", "outback", 3)
        roo = Mammal("Roo", "Kangaroo", 6, "herbivore", "Mammal", "outback")

        self.assertEqual(len(enc.animals), 0)

        enc.addAnimal(roo)
        self.assertEqual(len(enc.animals), 1)
        self.assertEqual(enc.animals[0], roo)

        enc.cleanliness = 40
        msg = enc.cleanEnclosure()
        self.assertEqual(enc.cleanliness, 100)
        self.assertIn("Outback Habitat", msg)

        enc.removeAnimal(roo)
        self.assertEqual(len(enc.animals), 0)

    def test_zoo_adds_and_assigns(self):
        zoo = Zoo("Adelaide City Zoo")
        forest = Enclosure("Australian Forest", "eucalyptus_forest", 3)
        aviary = Enclosure("Coastal Aviary", "coastal_aviary", 3)
        zoo.addEnclosure(forest)
        zoo.addEnclosure(aviary)

        koala = Mammal("Koko", "Koala", 4, "herbivore", "Mammal", "eucalyptus_forest")
        penguin = Bird("Pebble", "Little Penguin", 3, "piscivore", "Bird", "coastal_aviary")
        zoo.addAnimal(koala)
        zoo.addAnimal(penguin)

        self.assertEqual(len(zoo.getAnimals()), 2)
        self.assertEqual(len(zoo.getEnclosures()), 2)

        zoo.assignAnimalToEnclosure(koala, forest)
        zoo.assignAnimalToEnclosure(penguin, aviary)
        self.assertEqual(forest.animals, [koala])
        self.assertEqual(aviary.animals, [penguin])




