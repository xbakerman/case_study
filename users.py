import os
from tinydb import TinyDB, Query 
from serializer import serializer


class User:
    
    db_connector = None

    @classmethod
    def initialize_database(cls):
        # Hier kannst du die Initialisierung der Datenbank durchführen
        cls.db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')
        print("Database initialized.")

    db_connector = TinyDB(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.json'), storage=serializer).table('users')

    def __init__(self, id, name):
        if User.db_connector is None:
            User.initialize_database()
        self.id = id
        self.name = name
        

    def __str__(self):
        return f"{self.name} ({self.id})"
    
    def to_dict(self):
        return {"id": self.id, "name": self.name}
    
    def store_data(self):
        print("Storing user data...")
        # Check if the user already exists in the database
        UserQuery = Query()
        result = self.db_connector.search(UserQuery.id == self.id)
        if result:
            # Update the existing record with the current instance's data
            result = self.db_connector.update(self.to_dict(), doc_ids=[result[0].doc_id])
            print("User data updated.")
        else:
            # If the user doesn't exist, insert a new record
            self.db_connector.insert(self.to_dict())
            print("User data inserted.")
            
    @classmethod
    def load_data_by_id(cls, user_id):
        # Lade Daten aus der Datenbank und erstelle eine Instanz der User-Klasse
        UserQuery = Query()
        result = cls.db_connector.get(UserQuery.id == user_id)

        if result:
            data = result
            return cls(data['id'], data['name'])
        else:
            return None