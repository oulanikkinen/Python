
# Määritellään auto-luokka
class merkki_maara:

    merkki = ""
    maara = ""
    
# Määritellään auto-lista
autot = []

# Luodaan auto-olio
auto1 = merkki_maara()
auto1.merkki = input("Anna automerkki: ")
auto1.maara = input("Anna automerkin lukumäärä varastossa: ")

# Lisätään auto listaan
autot.append(auto1)


# Tulostetaan autojen tiedot
for auto1 in autot:
    print("Varastossa on nyt "+ str(auto1.merkki) + "-merkkisiä autoja " + str(auto1.maara) + " kpl.")

print("Kiitos ohjelman käytöstä.")
   