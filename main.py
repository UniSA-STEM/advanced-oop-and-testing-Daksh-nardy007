from Mammal import Mammal
from Bird import Bird
from Reptile import Reptile
from enclosure import Enclosure
from Zoo import Zoo
from HealthRecord import HealthRecord
from zookeeper import Zookeeper
from Veterinarian import Veterinarian

print("\nADELAIDE ZOO: INITIALISE")
zoo = Zoo("Adelaide City Zoo")
print("Zoo created:", "Adelaide City Zoo")

print("\nCREATE ADELAIDE ENCLOSURES")
aussie_forest = Enclosure("Australian Forest", "eucalyptus_forest", 3)
coastal_aviary = Enclosure("Coastal Aviary", "coastal_aviary", 3)
outback_habitat = Enclosure("Outback Habitat", "outback", 3)
zoo.addEnclosure(aussie_forest)
zoo.addEnclosure(coastal_aviary)
zoo.addEnclosure(outback_habitat)
print("Enclosures:", [e.name for e in zoo.getEnclosures()])

print("\nADD SOUTH AUSTRALIAN FAUNA")
kangaroo = Mammal("Roo", "Kangaroo", 6, "herbivore", "Mammal", "outback")
koala = Mammal("Koko", "Koala", 4, "herbivore", "Mammal", "eucalyptus_forest")
penguin = Bird("Pebble", "Little Penguin", 3, "piscivore", "Bird", "coastal_aviary")
shingleback = Reptile("Stumpy", "Shingleback Lizard", 5, "insectivore", "Reptile", "outback")
zoo.addAnimal(kangaroo); zoo.addAnimal(koala); zoo.addAnimal(penguin); zoo.addAnimal(shingleback)
print("Animals:", [a.getName() for a in zoo.getAnimals()])

print("\nASSIGN ANIMALS TO ADELAIDE ENCLOSURES")
zoo.assignAnimalToEnclosure(kangaroo, outback_habitat)
zoo.assignAnimalToEnclosure(shingleback, outback_habitat)
zoo.assignAnimalToEnclosure(koala, aussie_forest)
zoo.assignAnimalToEnclosure(penguin, coastal_aviary)
print("Australian Forest:", [a.getName() for a in aussie_forest.animals])
print("Coastal Aviary   :", [a.getName() for a in coastal_aviary.animals])
print("Outback Habitat  :", [a.getName() for a in outback_habitat.animals])

print("\nHEALTH RECORD (ADELAIDE VET CASE)")
penguin_record = HealthRecord("Minor flipper abrasion", "2025-11-12", "low", "Apply antiseptic daily")
penguin_record.severity = "low"
penguin_record.treatment = "Apply antiseptic daily"
penguin.addHealthRecord(penguin_record)
print("Penguin health (before vet):", str(penguin.getHealthRecord()))

print("\nBEHAVIOUR SHOWCASE")
print("Sounds:", kangaroo.makeSound(), "|", koala.makeSound(), "|", penguin.makeSound(), "|", shingleback.makeSound())
print("Eating:", kangaroo.eat(), "|", koala.eat(), "|", penguin.eat(), "|", shingleback.eat())
print("Sleeping:", kangaroo.sleep(), "|", koala.sleep(), "|", penguin.sleep(), "|", shingleback.sleep())

print("\nZOOKEEPER (ADELAIDE OPERATIONS)")
keeper = Zookeeper("Alex (Adelaide Keeper)")
zoo.addStaff(keeper)
keeper.assignToEnclosure(aussie_forest)
keeper.assignToEnclosure(coastal_aviary)
keeper.assignToEnclosure(outback_habitat)
print("Staff:", [(s.name, s.role) for s in zoo.getStaff()])
print("Keeper enclosures:", [e.name for e in keeper.assignedEnclosures])

print("\nFEEDING CYCLE (ADELAIDE MORNING)")
print("Hunger BEFORE:", {"Roo": kangaroo.getHunger(), "Koko": koala.getHunger(), "Pebble": penguin.getHunger(), "Stumpy": shingleback.getHunger()})
keeper.feedAnimal()
print("Hunger AFTER :", {"Roo": kangaroo.getHunger(), "Koko": koala.getHunger(), "Pebble": penguin.getHunger(), "Stumpy": shingleback.getHunger()})

print("\nCLEANING CYCLE (ADELAIDE MIDDAY)")
aussie_forest.cleanliness = 48
coastal_aviary.cleanliness = 62
outback_habitat.cleanliness = 51
keeper.cleanEnclosure()
print("Cleanliness:", {
    "Australian Forest": aussie_forest.cleanliness,
    "Coastal Aviary": coastal_aviary.cleanliness,
    "Outback Habitat": outback_habitat.cleanliness
})

print("\nADELAIDE VETERINARIAN CHECKS")
vet = object.__new__(Veterinarian)
vet.name = "Dr. Mia (Adelaide Vet)"
vet.assignedAnimals = [penguin]
vet.conductHealthChecks()
print("Penguin health (after vet):", str(penguin.getHealthRecord()))

print("\nADELAIDE ZOO SNAPSHOT")
print("Zoo animals:", [a.getName() for a in zoo.getAnimals()])
print("Zoo enclosures:", [e.name for e in zoo.getEnclosures()])
print("Zoo staff:", [(s.name, s.role) for s in zoo.getStaff()])
print("Australian Forest:", [a.getName() for a in aussie_forest.animals], "| Cleanliness:", aussie_forest.cleanliness)
print("Coastal Aviary   :", [a.getName() for a in coastal_aviary.animals], "| Cleanliness:", coastal_aviary.cleanliness)
print("Outback Habitat  :", [a.getName() for a in outback_habitat.animals], "| Cleanliness:", outback_habitat.cleanliness)
print("Roo:", {"species": kangaroo.getSpecies(), "age": kangaroo.getAge(), "hunger": kangaroo.getHunger()})
print("Koko:", {"species": koala.getSpecies(), "age": koala.getAge(), "hunger": koala.getHunger()})
print("Pebble:", {"species": penguin.getSpecies(), "age": penguin.getAge(), "hunger": penguin.getHunger(), "health": str(penguin.getHealthRecord())})
print("Stumpy:", {"species": shingleback.getSpecies(), "age": shingleback.getAge(), "hunger": shingleback.getHunger()})
