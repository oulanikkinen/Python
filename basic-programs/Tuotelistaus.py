
class auto: 
  def __init__(self, make, price):
    self.make = make
    self.price = price

def auto_tiedot(auto_lista):
  make = input("Anna auton merkki: ")
  price = int(input("Anna auton hinta: \n"))
  auto_lista.append(auto(make, price))
  return auto_lista

def kerro_auto_info(auto_lista):
    print("Listalta löytyy seuraavat automerkit ja hinnat:")
    for car in auto_lista:
        print(f"{car.make} {car.price}")
    print()

def main():
  auto_lista = []
  print("Tämä ohjelma lisää autojen tietoja listaan ja tulostaa ne.")
  while True:
    #print()
    print("Käytettävissä olevat toiminnot:")
    print("1) Anna auton tiedot")
    print("2) Tulosta autojen tiedot")
    print("0) Lopeta")
    selection = int(input("Valintasi: "))

    if selection == 1:
      auto_lista = auto_tiedot(auto_lista)
    elif selection == 2:
      kerro_auto_info(auto_lista)
    elif selection == 0:
      print("Kiitos ohjelman käytöstä.")
      break
    else:
      print("Tuntematon valinta, yritä uudestaan.\n")

if __name__ == "__main__":
  main()
