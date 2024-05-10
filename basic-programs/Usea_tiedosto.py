#
import Usea_tiedosto_Kirjasto

def main():
    # alustetaan kaksi listaa kaikelle datalle
    lines_list = []
    
    results_list = []

    total_value = 0

    #  kysytään tiedostoja lukemiseen, kirjoittamiseen
    file_name = input("Anna luettavan tiedoston nimi: ")
    
    output = input("Anna kirjoitettavan tiedoston nimi: ")

    # ikuinen looppi kunnes :0
    while True:
        # vaihtoehto plus valinta
        choice = int(input("Mitä haluat tehdä:\n1) Lue tiedosto\n2) Analysoi tiedot\n3) Tallenna Tulokset\n0) Lopeta\nValintasi: "))

        if choice == 1:# Lukee annetun tiedoston
            
            lines_list = Usea_tiedosto_Kirjasto.read_file(file_name) #  kutsuu kirjastosta kyseisen tehtävän 

            print(f"Tiedosto '{file_name}' luettu, {len(lines_list)} riviä.")   # printtaa tiedon listan pituudesta
            
            print() # laiskuudesta tämä lisää tyhjän rivin  ennen  uutta kierrosta
    
    
        elif choice == 2: # analysoi tiedoston data
            
            
            
            results_list = Usea_tiedosto_Kirjasto.analyze_data(lines_list) # kutsuu kirjastosta kyseisen tehtävän
            
            print(f"Tiedot analysoitu, varaston arvo on {results_list[-1]:.2f} EUR.") # printtaa tiedon kokonais arvosta

            del results_list[-1]

            print() # laiskuudesta tämä lisää tyhjän rivin  ennen  uutta kierrosta
        
    
        elif choice == 3: # tallentaa tulokset output tiedostoon

            Usea_tiedosto_Kirjasto.save_results(results_list, output) # kutsuu kirjastosta kyseisen tehtävän

            print(f"Tulokset tallennettu tiedostoon '{output}'.")

            print() # laiskuudesta tämä lisää tyhjän rivin  ennen  uutta kierrosta
    
        elif choice == 0: # lopettaa ja kiittää

            print("Kiitos ohjelman käytöstä.")

            break

        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")

            print() #  laiskuudesta tämä lisää tyhjän rivin  ennen  uutta kierrosta

main()