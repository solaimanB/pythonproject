cijfer= int(input("welk jaar is het?"))

if cijfer %4 ==0 or cijfer %400 ==0 :
  print("het is een schrikkeljaar")
elif cijfer % 100 == 1:
  print("het is een normaal jaar")