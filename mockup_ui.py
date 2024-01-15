# mockup_ui.py
import streamlit as st

from devices import Device
from users import User

import json

nutzer_liste = []
json_dateipfad = "database.json"

# Beispiel-Nutzer und -Gerät für das Mockup
#beispiel_nutzer = User(id="nutzer@example.com", name="Max Mustermann", email="nutzer@example.com")
#beispiel_geraet = Device(device_name="Laser-Cutter", managed_by_user_id=beispiel_nutzer, wartungsdatum="2024-03-01", reservierungsbedarf_start="2021-03-01", reservierungsbedarf_ende="2021-03-31")

Geräte = ["3D-Drucker", "Laser-Cutter", "CNC-Fräse", "CNC-Drehbank", "Schweißgerät", "Lötkolben", "Oszilloskop", "Multimeter", "Bandsäge", "Ständerbohrmaschine"]

#def lade_daten():
#    try:
#        with open(json_dateipfad, "r") as datei:
#            daten = json.load(datei)
#    except FileNotFoundError:
#        daten = {"users": []}
#    except json.JSONDecodeError as e:
#        print(f"Fehler beim Laden der JSON-Daten: {e}")
#        daten = {"users": []}
#    return daten
#
#def speichere_daten(daten):
#    with open(json_dateipfad, "w") as datei:
#        # Benutze die `to_dict`-Methode, um die User-Objekte in dictionaries umzuwandeln
#        daten_to_save = {"users": [user.to_dict() for user in daten["users"]]}
#        json.dump(daten_to_save, datei, indent=2)



def nutzer_verwaltung():
    st.title("Nutzer-Verwaltung")

    # Button zum Anlegen neuer Nutzer
    anlegen_button_key = "button_anlegen"
    st.button("Nutzer anlegen", key=anlegen_button_key)

    nutzer_name = st.text_input("Name des Nutzers:")
    nutzer_email = st.text_input("E-Mail-Adresse des Nutzers:")
        
    
    daten = lade_daten()
    if not nutzer_name or not nutzer_email:
        st.warning("Bitte fülle alle erforderlichen Felder aus.")
    else:
        # Hier kannst du die User-Klasse verwenden, um einen neuen Nutzer anzulegen
        #neuer_nutzer = User(id=nutzer_email, name=nutzer_name)
        #daten["users"].append(neuer_nutzer)

        neuer_nutzer = User(id=nutzer_email, name=nutzer_name)
        neuer_nutzer.store_data()
        # Speichere die aktualisierten Daten in der JSON-Datei
        speichere_daten(daten)
        st.success(f"Nutzer '{neuer_nutzer.name}' mit E-Mail '{neuer_nutzer.id}' wurde angelegt.")
    

   # Dropdown-Menü zum Auswählen bestehender Nutzer
    daten = lade_daten()
    ausgewaehlter_nutzer_id = st.selectbox("Wähle einen Nutzer aus:", [user.id for user in daten["users"]])

    # Button zum Löschen des ausgewählten Nutzers
    loeschen_button_key = "button_loeschen"
    if st.button("Nutzer löschen", key=loeschen_button_key):
        ausgewaehlter_nutzer = User.load_data_by_id(ausgewaehlter_nutzer_id)
        if ausgewaehlter_nutzer:
            nutzer_loeschen(ausgewaehlter_nutzer, daten)
        else:
            st.warning(f"Nutzer mit ID '{ausgewaehlter_nutzer_id}' nicht gefunden.")



def nutzer_loeschen(ausgewaehlter_nutzer, daten):
    if ausgewaehlter_nutzer in daten["users"]:
        # Entferne den Nutzer aus der Liste
        daten["users"].remove(ausgewaehlter_nutzer)

        # Speichere die aktualisierten Daten in der JSON-Datei
        speichere_daten(daten)

        st.success(f"Nutzer '{ausgewaehlter_nutzer}' wurde gelöscht.")
    else:
        st.warning(f"Nutzer '{ausgewaehlter_nutzer}' nicht gefunden.")



# Hauptablauf für die Geräteverwaltung
def geraet_verwaltung():
    st.title("Geräte-Verwaltung")

    # Hier ersetzen wir die Mock-Klasse durch die echte Klasse
    geraet_name = st.selectbox("Gerät:", [device.device_name for device in Device.db_connector.all()])
    geraet_wartungsdatum = st.date_input("Wartungsdatum:")
    geraet_reservierungsbedarf_start = st.date_input("Reservierungsbedarf Startdatum:")
    geraet_reservierungsbedarf_ende = st.date_input("Reservierungsbedarf Enddatum:")

    if st.button("Gerät anlegen/ändern"):
        if geraet_reservierungsbedarf_start > geraet_reservierungsbedarf_ende:
            st.error("Das Startdatum darf nicht nach dem Enddatum liegen.")
        else:
            # Hier verwenden wir die echte Device-Klasse, um ein Gerät anzulegen oder zu ändern
            neues_geraet = Device(device_name=geraet_name,
                                  reservierungsbedarf_start=geraet_reservierungsbedarf_start,
                                  reservierungsbedarf_ende=geraet_reservierungsbedarf_ende,
                                  managed_by_user_id=beispiel_nutzer,
                                  wartungsdatum=geraet_wartungsdatum)
            neues_geraet.store_data()  # Speichern der Daten in der Datenbank
            st.success(f"Gerät '{neues_geraet.device_name}' wurde mit Reservierungsbedarf von '{neues_geraet.reservierungsbedarf_start}' bis '{neues_geraet.reservierungsbedarf_ende}' angelegt/geändert.")
def Reservierungssystem(): 
    st.title("Reservierungssystem") 

# Auswahl des Hauptablaufs basierend auf Benutzeraktion
auswahl = st.sidebar.selectbox("Wählen Sie eine Option:", ["Nutzer-Verwaltung", "Geräte-Verwaltung", "Reservierungssystem", "Wartungsmanagement" ])

if auswahl == "Nutzer-Verwaltung":
    nutzer_verwaltung()
    
elif auswahl == "Geräte-Verwaltung":
    geraet_verwaltung()

