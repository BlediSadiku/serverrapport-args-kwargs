# Hoofdstuk 5 – Functies & Modules
# Oefening: maak een rapportfunctie met *args en **kwargs.
# Bron: Scripting with Python SNB1, hoofdstuk 5, slides 9–11.

servernaam = "web-01"
statussen = ("online", "back-up voltooid", "updates beschikbaar")
details = {"locatie": "Brussel", "beheerder": "Demo"}

# TODO:
# 1. Definieer maak_serverrapport met een vaste servernaam, *args en **kwargs.
# 2. Druk servernaam, alle statussen en alle details overzichtelijk af.
# 3. Roep de functie op met de startdata.

def maak_serverrapport(servernaam,*statussen,**details):
    print("-", servernaam)
    for status in statussen:
        print("-", status)
    print("Details:")
    for naam, waarde in details.items():
        print(naam + ":", waarde)

maak_serverrapport(servernaam, *statussen, **details)

# Verwachte output van het VOLTOOIDE programma:
# Server: web-01
# Statussen:
# - online
# - back-up voltooid
# - updates beschikbaar
# Details:
# locatie: Brussel
# beheerder: Demo

# Hint: *args is een tuple en **kwargs is een dictionary.
