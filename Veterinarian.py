'''
File: Veterinarian.py
Description: A brief description of this Python module.
Author: Daksh Narang
ID: 110402195
Username: Nardy007
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Veterinarian(Animal):
    def __init__(self, name):
        super().__init__(name, "Veterinarian")

    def conductHealthChecks(self):
        logs = []
        for a in self.assignedAnimals:
            rec = a.getHealthRecord()
            if rec is None:
                logs.append(self.name + " checked " + a.getName() + " (no issues).")
            else:
                sev = str(rec.getSeverity()).lower()
                trt = rec.getTreatment()
                # Simple rule: resolve low severity if a treatment plan exists
                if sev == "low" and trt:
                    rec.resolved()
                    logs.append(self.name + " resolved " + a.getName() + "'s issue.")
                else:
                    logs.append(self.name + " reviewed " + a.getName() + " (" + str(rec.getSeverity()) + ").")
        return logs

    def duty(self):
        return self.conductHealthChecks()