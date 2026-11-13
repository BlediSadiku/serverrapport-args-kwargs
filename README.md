# Oefening: *args en **kwargs

Een kleine Python-oefening uit hoofdstuk 5 van Scripting with Python SNB1. Met een eenvoudig serverrapport oefen ik hoe je een variabel aantal argumenten aan een functie meegeeft.

## Wat oefen ik?

```python
def maak_serverrapport(servernaam, *statussen, **details):
```

- `servernaam` is een verplicht argument.
- `*statussen` verzamelt extra positionele argumenten in een tuple (`*args`).
- `**details` verzamelt benoemde argumenten in een dictionary (`**kwargs`).

Bij het aanroepen pakken `*statussen` en `**details` de voorbeeldgegevens weer uit tot afzonderlijke argumenten.

## Uitvoeren

Vereist Python 3, zonder externe pakketten.

```sh
python3 03_serverrapport_args_kwargs.py
```

Voorbeelduitvoer:

```text
Server: web-01
Statussen:
- online
- back-up voltooid
- updates beschikbaar
Details:
locatie: Brussel
beheerder: Demo
```

## Verbetering

Na de eerste versie heb ik de koppen `Server:` en `Statussen:` toegevoegd. Daardoor komt de uitvoer overeen met het voorbeeld uit de oefening.

## Tests

```sh
python3 -B test_serverrapport.py
```

Vijf kleine tests controleren de uitvoer en het aanroepen van de functie.
