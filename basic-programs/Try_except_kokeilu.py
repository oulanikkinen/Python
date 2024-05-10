#
import sys

# Aliohjelma tiedoston lukemiseen
def read_file(filename):
  # Alustetaan tyhjä lsita
  numbers = []
  
  try:
    # avaa tiedosto
    with open(filename, 'r') as f:
      # lue koko tiedosto 
      lines = f.readlines()
      
      # muuta listan ainekset int muotoon
      for line in lines:
        numbers.append(int(line))
  except IOError:
    print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(filename))
    sys.exit(0)
  
  # palauta lista numeroilla 
  return numbers

# aliohjelma tiedoston kirjoitukseen
def write_file(filename, numbers):
  try:
    # avaa tiedosto
    with open(filename, 'w') as f:
      # käy listan läpi ja kirjaa rivit
      for number in numbers:
        f.write(str(number) + '\n')
  except IOError:
    print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(filename))
    sys.exit(0)

# pääruoka
def main():
  # kysyy ensimmäistä tiedostoa
  input_filename = input("Anna luettavan tiedoston nimi: ")
  
  # kutsuu lukemiseen apua
  numbers = read_file(input_filename)
  
  #printtaa käyttäjälle
  print("Tiedoston '{}' lukeminen onnistui, {} riviä.".format(input_filename, len(numbers)))
  
  # kysyy toista tiedostoa
  output_filename = input("Anna kirjoitettavan tiedoston nimi: ")
  
  # kysyy apua kirjoitukseen
  write_file(output_filename, numbers)
  
  #printtaa käyttäjälle 
  print("Tiedoston '{}' kirjoittaminen onnistui.".format(output_filename))
  
  # kiittää käytöstä
  print("Kiitos ohjelman käytöstä.")

# huhuilee pääohjelmaa

main()
