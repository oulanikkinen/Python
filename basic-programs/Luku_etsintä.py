#
# kysyy ylä ja alarajaa
ala_raja = int(input("Anna alueen alaraja: "))
yla_raja = int(input("Anna alueen yläraja: "))


sopiva_numero_loytyi = False# laita True/False lippu, jotta voit seurata, löytyikö sopiva numero vai ei


for number in range(ala_raja, yla_raja + 1):# Toista hakualueen numerot
    if  number  % 5 == 0 and number % 7 == 0:# Tarkista, onko nykyinen luku jaollinen 5:llä ja 7:llä
        print("Luku " + str(number) + " on jaollinen 5:llä ja 7:llä.")# Jos numero on jaettavissa 5 ja 7, printaa viesti ja laita lippu True.
        sopiva_numero_löytyi = True
        print("Lopetetaan etsintä.")
        break
    else:
        if number % 5 != 0:# Jos numero ei ole jaettavissa 5,  printtaa viesti ja eteenpäin
            print(str(number) + " ei ole jaollinen viidellä, hylätään.")
        elif number % 7 != 0:#  Jos numero ei jaettavissa  7,  printtaa ja eteenpäins
            print(str(number) + " ei ole jaollinen seitsemällä, hylätään.")
if not sopiva_numero_loytyi:#Jos lippu edelleen False, löydetty ei numeroa.
    print("Alueelta ei löytynyt sopivaa arvoa.")

print("Kiitos ohjelman käytöstä.")
        
