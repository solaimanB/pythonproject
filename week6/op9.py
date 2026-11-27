class Huisdier:
    def __init__(self, naam, soort):
        self.naam = naam
        self.soort = soort

    def beschrijf(self):
        return f"Dit is {self.naam}, een {self.soort}."

mijn_dier = Huisdier("Luna", "kat")
print(mijn_dier.beschrijf())
#ik vroeg gemini om mij een code te geven waar er een bug in was
#de oplossing was 'self' te zetten tussen de haakjes van beschrijf