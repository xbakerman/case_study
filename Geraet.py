import os
from users import User
from tinydb import TinyDB, Query
from serializer import serializer

class Device():
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
    
    def store_data(self):
        print("Storing data...")
        # Check if the device already exists in the database
        DeviceQuery = Query()
        result = self.db_connector.search(DeviceQuery.device_name == self.device_name)
        if result:
                # Update the existing record with the current instance's data
                result = self.db_connector.update(self.__dict__, doc_ids=[result[0].doc_id])
                print("Data updated.")
        else:
                # If the device doesn't exist, insert a new record
                self.db_connector.insert(self.__dict__)
                print("Data inserted.")
            
    # Class method that can be called without an instance of the class to construct an instance of the class
    @classmethod
    def load_data_by_device_name(cls, device_name):
        # Load data from the database and create an instance of the Device class
        DeviceQuery = Query()
        result = cls.db_connector.search(DeviceQuery.device_name == device_name)

        if result:
            data = result[0]
            return cls(data['device_name'], data['managed_by_user_id'])
        else:
            return None
        
   