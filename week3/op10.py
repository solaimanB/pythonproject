vraag1 = int(input("hoeveel weeg je?"))
vraag2 = int(input("hoelang ben je?"))
uitkomst = vraag2/100
uitkomst2 = uitkomst*uitkomst
uitkomst3 = 90//uitkomst2

if uitkomst3>20 and uitkomst3<30:
    print("je bent gezond gewicht")
elif uitkomst3<20:
    print("je bent ondergewicht")
elif uitkomst3>30:
    print("je bent overgewicht")