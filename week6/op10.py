class Klant:
    def __init__(self, klant_id, naam, nummer):
        self.klant_id = klant_id
        self.naam = naam
        self.nummer = str(nummer)
    def __str__(self):
        return f"{self.nummer}"
    def controleer_telefoonnummer(self):
        if len(self.nummer) == 10:
            print("de nummer is geldig")
            return True
        else:
            print("telefoonnummer invalide")
            return False
klant1 = Klant(1, "Jan", "0612345678")
klant1.controleer_telefoonnummer()