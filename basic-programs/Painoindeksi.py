# Tiedosto L03T5.py

pit = float(input("Anna pituus (cm): "))
pit = pit / 100
pai = float(input("Anna paino (kg): "))


ind = float(pai / (pit * pit))
round(ind, 1)


ind2 = None
if ind < 17:
    ind2 = str("(Vaarallinen aliravitsemus)")

elif 17 < ind < 18.5:
    ind2 = str("(Liiallinen laihuus)")

elif 18.5 <= ind < 25:
    ind2 = str("(Normaali paino)")

elif 25 <= ind < 30:
    ind2 = str("(Ylipaino eli lievä lihavuus)")

elif 30 <= ind < 35:
    ind2 = str("(Merkittävä lihavuus)")

elif 35 <= ind < 40:
    ind2 = str("(Vaikea lihavuus)")

elif 40 <= ind:
    ind2 = str("(Sairaalloinen lihavuus)")


print("Painoindeksi on " + str(round(ind, 1)) +" "+ str(ind2) +"")

indk = float(input("Anna tavoiteindeksi: "))

tavoite = float(round(indk * (pit * pit), 1))



vert = round(pai - round(tavoite, 1), 2)
vert2 = (round(tavoite, 1) - pai)



if ind < indk:
    print("Tavoiteindeksi vastaa " + str(abs(vert))+ " kg suurempaa painoa.")
    
else: print("Tavoiteindeksi vastaa " + str(abs(vert2))+ " kg alhaisempaa painoa.")
    
print("Kiitos ohjelman käytöstä.")
