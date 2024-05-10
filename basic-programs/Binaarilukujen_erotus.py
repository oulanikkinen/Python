#
def binary_to_decimal(binary):
  # alustetaan tulosmuuttuja 
  result = 0

  # käy läpi binääriluku ensimmäiset viimeiseen
  for i, digit in enumerate(binary[::-1]):
    # muuta kokonaisluvuksi
    digit = int(digit)
    # lisää tulokseen numeron arvon kerrottuna 2 potenssilla, näin saamme muutettua binäärin kokonaislukuksi ilman kirjastoja
    result += digit * (2 ** i)

  # palauttaa tulosmuuttujan
  return result

# kysyy ekaa binääriä
first_binary = input("Anna ensimmäinen binaariluku: ")
  # kysyy toista binääriä
second_binary = input("Anna toinen binaariluku: ")

  # muuttaa ensimmäisen kutsumalla apua
first_decimal = binary_to_decimal(first_binary)
  # muuttaa toisen kutsumalla apua
second_decimal = binary_to_decimal(second_binary)

  # printtaa mitä kyseinen binääri on kokonaislukuna
print(f"Bittijonosi {first_binary} on kymmenkantaisena kokonaislukuna {first_decimal}")
  # printtaa mitä kyseinen binääri on kokonaislukuna
print(f"Bittijonosi {second_binary} on kymmenkantaisena kokonaislukuna {second_decimal}")

  # laskee erotuksen
difference = first_decimal - second_decimal

  # printtaa erotuksen
print(f"Lukujen {first_decimal} ja {second_decimal} erotus on {difference}")

  # kiittää
print("Kiitos ohjelman käytöstä.")