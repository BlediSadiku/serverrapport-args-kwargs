# Hoofdstuk 5 – Functies & Modules
# Oefening: maak een rapportfunctie met *args en **kwargs.
# Bron: Scripting with Python SNB1, hoofdstuk 5, slides 9–11.

servernaam = "web-01"
statussen = ("online", "back-up voltooid", "updates beschikbaar")
details = {"locatie": "Brussel", "beheerder": "Demo"}


def maak_serverrapport(servernaam, *statussen, **details):
    """Druk een rapport af met variabele statussen en details."""
    print("Server:", servernaam)
    print("Statussen:")
    # *statussen verzamelt de extra positionele argumenten in een tuple.
    for status in statussen:
        print("-", status)
    print("Details:")
    # **details verzamelt de benoemde argumenten in een dictionary.
    for naam, waarde in details.items():
        print(naam + ":", waarde)


if __name__ == "__main__":
    # Pak de tuple en dictionary uit bij het aanroepen van de functie.
    maak_serverrapport(servernaam, *statussen, **details)
