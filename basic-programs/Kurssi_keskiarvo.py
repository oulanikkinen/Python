#
arvo = 0
num = 0
while (True): # Jatketaan ikuisesti, breakillä pääsee ulos
    arvosana = int(input("Anna kurssiarvosana väliltä 1-5 (-1 lopettaa): "))
    if (-1!= arvosana < 1):
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")
    if (arvosana > 5):
        print("Väärä syöte. Vain arvosanat 1-5 kelpaavat (-1 lopettaa).")


    elif (1<=arvosana<=5):
        num = num + arvosana
        arvo = arvo + 1
        #print("Arvasit oikein!")
        #print("Peli päättyy tähän")
    
    elif (arvosana == -1):
        break # hypätään ulos while-silmukasta

#print(num)
#print(arvo)
ka = num / arvo
#ka = float(ka)
ka = round(ka, 2)

print("Arvosanojen keskiarvo on " +str(ka) +".")
print("Kiitos ohjelman käytöstä.")
