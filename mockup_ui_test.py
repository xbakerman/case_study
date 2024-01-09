# mockup_ui.py
import streamlit as st
from queries import find_devices
from Geraet import Device
from Nutzer import User

# Beispiel-Nutzer und -Gerät für das Mockup
#beispiel_nutzer = User(id="nutzer@example.com", name="Max Mustermann", email="nutzer@example.com")
#beispiel_geraet = Device(name="Laser-Cutter", verantwortlicher=beispiel_nutzer, wartungsdatum="2024-03-01", reservierungsbedarf="2024-04-01")

Geräte = ["3D-Drucker", "Laser-Cutter", "CNC-Fräse", "CNC-Drehbank", "Schweißgerät", "Lötkolben", "Oszilloskop", "Multimeter", "Bandsäge", "Ständerbohrmaschine"]

# Hauptablauf für die Nutzerverwaltung
def nutzer_verwaltung():
    st.title("Nutzer-Verwaltung")

    nutzer_name = st.text_input("Name des Nutzers:")
    nutzer_email = st.text_input("E-Mail-Adresse des Nutzers:")

    if st.button("Nutzer anlegen"):
        neuer_nutzer = User(id=nutzer_email, name=nutzer_name, email=nutzer_email)
        st.success(f"Nutzer '{neuer_nutzer.name}' mit E-Mail '{neuer_nutzer.email}' wurde angelegt.")

# Hauptablauf für die Geräteverwaltung
def geraet_verwaltung():
    st.title("Geräte-Verwaltung")

    geraet_name = st.selectbox("Gerät:", Geräte)
    #geraet_wartungsdatum = st.date_input("Wartungsdatum:")
    geraet_reservierungsbedarf_start = st.date_input("Reservierungsbedarf Startdatum:" )
    geraet_reservierungsbedarf_ende = st.date_input("Reservierungsbedarf Enddatum:" )

    if st.button("Gerät anlegen/ändern"):
        if geraet_reservierungsbedarf_start > geraet_reservierungsbedarf_ende:
            st.error("Das Startdatum darf nicht nach dem Enddatum liegen.")
        else:
            neues_geraet = Device(name=geraet_name, reservierungsbedarf_start=geraet_reservierungsbedarf_start, reservierungsbedarf_ende=geraet_reservierungsbedarf_ende)
            st.success(f"Gerät '{neues_geraet.name}' wurde mit Reservierungsbedarf von '{neues_geraet.reservierungsbedarf_start}' bis '{neues_geraet.reservierungsbedarf_ende}' angelegt/geändert.")

# Auswahl des Hauptablaufs basierend auf Benutzeraktion
auswahl = st.sidebar.selectbox("Wählen Sie eine Option:", ["Nutzer-Verwaltung", "Geräte-Verwaltung"])

if auswahl == "Nutzer-Verwaltung":
    nutzer_verwaltung()
elif auswahl == "Geräte-Verwaltung":
    geraet_verwaltung()
