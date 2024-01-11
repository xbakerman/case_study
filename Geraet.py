class Device:
    def __init__(self, name, reservierungsbedarf_start, reservierungsbedarf_ende, verantwortlicher, wartungsdatum):
        self.name = name
        self.verantwortlicher = verantwortlicher  # Hier wird ein Objekt der Klasse Nutzer übergeben
        self.wartungsdatum = wartungsdatum
        
        self.reservierungsbedarf_start = reservierungsbedarf_start
        self.reservierungsbedarf_ende = reservierungsbedarf_ende
        self.reservierungs_queue = []

    def reservierung_hinzufuegen(self, reservierungsbedarf):
        self.reservierungs_queue.append(reservierungsbedarf)

    def wartungsdatum_aendern(self, neues_wartungsdatum):
        self.wartungsdatum = neues_wartungsdatum

    def __str__(self):
        return f"{self.name} (Verantwortlich: {self.verantwortlicher}, Wartungsdatum: {self.wartungsdatum})"