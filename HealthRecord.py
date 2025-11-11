class HealthRecord:
    def __init__(self, description, dateReported, severity, treatment=None):
        self.__description = description
        self.__dateReported = dateReported
        self.__severity = severity
        self.__treatment = treatment
        self.__resolved = False

    def getDescription(self):
        return self.description
    def getDateReported(self):
        return self.dateReported
    def getSeverity(self):
        return self.severity
    def getTreatment(self):
        return self.treatment
    def getResolved(self):
        return self.__resolved

    def resolved(self):
        self.__resolved = True

    def __str__(self):
        status = "Resolved" if self.__resolved else "Active"
        return "Issue: " + self.__description + " | Severity: " + self.__severity + " | " + status
