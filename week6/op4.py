class persoon:
 def __init__(self, naam, leeftijd, woonplaats):
  self.naam = naam
  self.leeftijd = leeftijd
  self.woonplaats = woonplaats
 def toon_info(self):
      print(f"{self.naam} is mijn naam")
      print(f"{self.leeftijd} jaar is mijn leeftijd")
      print(f"{self.woonplaats} is mijn woonplaats")

persoon = persoon("Solaiman", 16, "Beverwijk")
persoon.toon_info()