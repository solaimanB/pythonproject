cijfer=int(input("Hoe oud ben je?"))

if cijfer < 13:
  print("kind")
elif cijfer >= 13 and cijfer < 17:
  print("tiener")
else:
  print("volwassen")