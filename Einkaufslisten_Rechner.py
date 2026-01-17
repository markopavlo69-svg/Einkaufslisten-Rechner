einkaufsliste = dict() #erstelle Dict

entry = None
preis = None
isfertig = False

while isfertig == False: #Hauptlogik
    entry = input("Bitte Produkt eingeben:") 
    try:
        preis = float(input("Bitte Preis eingeben: "))
        einkaufsliste[entry] = preis
    except:
        preis = 0
        
    
    if entry == "fertig":
        isfertig = True
        
        break
    else:
        continue
print("=== EINKAUFSLISTE ===") #Ausgabelogik
summe = 0
for produkt,preis in einkaufsliste.items():
    summe = summe + preis
    print(produkt, ": ",preis, "€")

print("------------------------------")
print( "Summe:",summe, "€")

     




