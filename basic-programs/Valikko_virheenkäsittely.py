#
import Valikko_virheenkäsittelyKirjasto as library

def main():
  # kertoo alkusanat
    
    print("Tämä ohjelma lukee tiedoston ja tulostaa sen tiedot näytölle.")
    # luo tyhjän listan tiedoille
    data = []
  
  # näyttää valikon ja kysyy mitä haluaa
  
    choice = displayMenu()

  # käy valintaa läpi
    while choice != 0:
        if choice == 1:
            file_name = library.askForFileName()# kysyy tiedostoa
        elif choice == 2:
      # lukee tiedoston ja tallentaa listaan
            data = library.readFile(file_name)
        elif choice == 3:
      # printtaa käyttäjälle kaikki
            library.printData(data)
        elif choice == 4:
      # kutsuu kirjoitukseen 
            library.writeFile(file_name, data)
            
            # näyttää valikon
        
        choice = displayMenu()

  # lopputekstit
    print("Kiitos ohjelman käytöstä.")

def displayMenu():
  choice = int(input("1) Anna tiedoston nimi\n2) Lue tiedosto\n3) Tulosta tiedot\n4) Kirjoita tiedosto\n0) Lopeta\nAnna valintasi: "))
  return choice

# pääruoka kutsuu
main()
