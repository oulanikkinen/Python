#
import datetime
from collections import Counter


weekdays = []

def read_file(filename):
  try:
    with open(filename, 'r') as f:
      f.readline()
      
      for line in f:
        line_sentences = line.split(";")
        for sentence in line_sentences:
          words = sentence.split(",")
          if words[0].strip():
            weekdays.append(words[0])
       
    return weekdays
  except IOError:
    print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(filename))
    exit()


def print_data(weekdays):
  c = Counter(weekdays)
  print(";Palautuksia viikonpäivittäin")
  print("{};{}".format('Monday', c['Monday']))
  print("{};{}".format('Tuesday', c['Tuesday']))
  print("{};{}".format('Wednesday', c['Wednesday']))
  print("{};{}".format('Thursday', c['Thursday']))
  print("{};{}".format('Friday', c['Friday']))
  print("{};{}".format('Saturday', c['Saturday']))
  print("{};{}".format('Sunday', c['Sunday']))
  print("Yhteensä;{}".format(sum(c.values())))


def main():
  
  print("Anna haluamasi toiminnon numero seuraavasta valikosta: ")
  print("1) Lue tiedosto")
  print("2) Analysoi tiedot viikonpäivittäin")
  print("0) Lopeta")
  
  
  choice = int(input("Valintasi: "))

  
  if choice == 1:
    filename = input("Anna luettavan tiedoston nimi: ")
    read_file(filename)
    print("Tiedosto luettu.")
  
  elif choice == 2:
    print_data(weekdays)
    
  elif choice == 0:
    print("Kiitos ohjelman käytöstä.")
    exit()
  else:
    print("Tuntematon valinta, yritä uudestaan.")

while True:
  main()
