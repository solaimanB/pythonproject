try:
 getal = int(input("Geef een getal: "))
 getal2 = int(input("Geef nog een getal: "))
 print(getal / getal2)
except ValueError:
 print("Dat is geen geldig getal.")
except ZeroDivisionError:
 print("Je kunt niet door nul delen.")