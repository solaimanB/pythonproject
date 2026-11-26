class solaiman:
 def __init__(self, naam, leeftijd):
  self.naam = naam
  self.leeftijd = leeftijd
 def toon_info(self):
      print(f"{self.naam} is mijn naam en ik ben {self.leeftijd} jaar oud!")
solaiman = solaiman("solaiman", 16)
solaiman.toon_info()