#
def check_id(id_str):
  # tarkistaa että henkkari on 11 merkkiä
  if len(id_str) != 11:
    return False
  
  # tarkistaa että ensimmäiset 6 numeroa ovat aito päivämäärä (ppkkvv)
  try:
    day = int(id_str[0:2])
    month = int(id_str[2:4])
    year = int(id_str[4:6])
    if not (1 <= day <= 31) or not (1 <= month <= 12) or not (0 <= year <= 99):
      return False
  except ValueError:
    return False
  
  # tarkistaa onko vuosisata symbooli oikein
  if id_str[6] not in ['+', '-', 'A']:
    return False
  
  # tarkistaa onko (nnn) numerot aidot
  try:
    individual_number = int(id_str[7:10])
    if not (2 <= individual_number <= 999):
      return False
  except ValueError:
    return False
  
  # tarkistaa meneekö t merkintä läpi
  check_mark_table = {
  0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
  10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F', 16: 'H', 17: 'J', 18: 'K',
  19: 'L', 20: 'M', 21: 'N', 22: 'P', 23: 'R', 24: 'S', 25: 'T', 26: 'U', 27: 'V',
  28: 'W', 29: 'X', 30: 'Y'
}
  date_and_number = int(id_str[0:6] + id_str[7:10])
  check_mark = check_mark_table[date_and_number % 31]

  if id_str[10] != check_mark:
    return False
  
  # jos läpäisee kaikki palauttaa toden
  return True

# kysyy peiffejä
id = input("Anna henkilötunnus: ")

# tarkistaa onko toimivat henkkarit
if check_id(id):
  print("Henkilötunnus hyväksytty.")
else:
  print("Henkilötunnusta ei hyväksytä.")

print("Kiitos ohjelman käytöstä.")
