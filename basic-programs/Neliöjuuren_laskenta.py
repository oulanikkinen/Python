#
import math

def find_square_root(number):
  #alustetaan juuri nollaksi
  square_root = 0

  #loopilla nolla lukuun asti kaikki juuret
  for i in range(1, number + 1):
    # jos juuri on jo suurempi kuin luku, valitaan edellinen eli joka jää alle
    if i**2 > number:
      square_root = i-1
      break

  # jos juuri ei ole sama kokonaisluku pyöristetään me ylöspäin 
  if square_root**2 != number:
    square_root += 1

  return square_root

# kysy numeroa
number = int(input("Anna luku: "))

# laskee juuren
square_root = find_square_root(number)

# Printtaa tulokset
print(f"Neliöjuuri on {square_root}")
print("Kiitos ohjelman käytöstä.")
