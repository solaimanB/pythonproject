prijs= int(input("wat is het prijs van het product?"))
leden= str(input("ben je lid? (ja/nee)"))
if leden == "ja":
    print("het prijs van het product is voor jou omdat je een mooie lid bent", prijs/100*90,"euro")
else:
    print("je bent waardeloos, normale prijs!!!",prijs,"euro")