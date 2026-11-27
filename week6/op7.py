class Klant:
    def __init__(self, klant_id, naam, nummer):
        self.klant_id = klant_id
        self.naam = naam
        self.nummer = nummer
    def __str__(self):
        return f"{self.klant_id} {self.naam} {self.nummer}"

def lijst():
  return [
     Klant(1, "jan", "06123456789"),
     Klant(2, "kees", "06123456788"),
     Klant(3, "piet", "06123986788"),
     Klant(4, "Ashraf", "06563456788"),
     Klant(5, "Wouter", "06123346788"),
  ]

klanten = lijst()

for klant in klanten:
 print(klant)