#
import sys
import csv

# luodaan tyhjä sanakirja
counts = {}

file_name = input("Anna luettavan tiedoston nimi: ")

# avataan tiedosto muodossa utf-8 encoding
try:# olettaa ettei löydy
    with open(file_name, encoding='utf-8') as f:
        # käytetään csv. jotta voidaan erotella ; merkit
        reader = csv.reader(f, delimiter=';')
        # skipataan eka rivi koska vain verbaalista infoa autoista
        next(reader)
        # käydään kaikki rivit
        for row in reader:
        # saadaan vuosiluku
            year = row[1][:4]
        #  sanakirjassa nostetaan vuosilukua
            counts[year] = counts.get(year, 0) + 1
except:# plan b jos ei löydy
        print(f"Tiedoston '{file_name}' käsittelyssä virhe, lopetetaan.")
        sys.exit()

# printtaa tulokset vuosien mukaan
print("Autot lajiteltuna vuosiluvun mukaan laskevaan järjestykseen.")
print("Vuosi: Autoja")
for year in sorted(counts, reverse=True):
  print(f"{year}: {counts[year]}")
print(f"Yhteensä {sum(counts.values())} autoa.")
print("Kiitos ohjelman käytöstä.")
