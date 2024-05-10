
import Valikkolaskin_kirjasto as lk

def main():
    # listat numeroille ja tuloksille
    numbers_list = []
    results_list = []
    mode = 'r'
    mode2 = 'a'
    lippu = True
    
    # kysyy luettavaaa sekä kirjoitetavaa tiedostoa
    file_name = input("Anna luettavan tiedoston nimi: ")
    output_file = input("Anna kirjoitettavan tiedoston nimi: ")
            
    choice = int(input("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta\nValitse toiminto (0-3): "))
    lk.kokeile(file_name, mode)
    # lukee numerot tiedostosta ja tallentaa ne numbers_list listalle
    with open(file_name, 'r', encoding="utf-8") as input_file:
        line = input_file.readline().strip()
        while line:
            numbers_list.append(str(line))
            line = input_file.readline().strip()

        # avaa tiedoston kirjoitukselle
     #with open(output_file, 'a', encoding="utf-8") as output_file_name:
        # lasketaan indeksillä numeroiden määrä numero listalla
        index = 0
        # numerot numero listalla
        num_count = len(numbers_list)
        
        #choice = -1
        
            
    if choice == 1: # valinnan mukaan joku näistä jos lauseista toimii kutsulla
                
                
                #  vertailee numeroiden määrää indeksiin, jotta tietää milloin numerot loppuu
            if index < num_count:
                num1 = numbers_list[index]
                num2 = numbers_list[index+1]
                    # nostetaan indeksiä kahdella
                index += 2
                    # printtaa sen hetkiset numerot jotka oli listalla seuraavaksi
                print("Luettu tiedosto '"+str(file_name)+"'.")
                print(f"Luettiin luvut {num1} ja {num2}")
                lippu = False
            else: # jos numerot pääsee loppumaan printtaa varoituksen
                    print("Luvut loppuivat, lopeta ohjelma.")
    else:
            print("Tuntematon valinta, yritä uudelleen")
        # printtaa valinnat# kysyy haluttua valintaa
        
    choice = int(input("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta\nValitse toiminto (0-3): "))
    if choice == 1 and lippu == True: # valinnan mukaan joku näistä jos lauseista toimii kutsulla
                
                
                #  vertailee numeroiden määrää indeksiin, jotta tietää milloin numerot loppuu
            if index < num_count:
                num1 = numbers_list[index]
                num2 = numbers_list[index+1]
                    # nostetaan indeksiä kahdella
                index += 2
                    # printtaa sen hetkiset numerot jotka oli listalla seuraavaksi
                print("Luettu tiedosto '"+str(file_name)+"'.")
                print(f"Luettiin luvut {num1} ja {num2}")
                
            else: # jos numerot pääsee loppumaan printtaa varoituksen
                    print("Luvut loppuivat, lopeta ohjelma.")
        
    elif choice == 1 and lippu == False: # valinnan mukaan joku näistä jos lauseista toimii kutsulla
                
                
                #  vertailee numeroiden määrää indeksiin, jotta tietää milloin numerot loppuu
            if index < num_count:
                num1 = numbers_list[index]
                num2 = numbers_list[index+1]
                    # nostetaan indeksiä kahdella
                index += 2
                    # printtaa sen hetkiset numerot jotka oli listalla seuraavaksi
                #print("Luettu tiedosto '"+str(file_name)+"'.")
                print(f"Luettiin luvut {num1} ja {num2}")
            else: # jos numerot pääsee loppumaan printtaa varoituksen
                    print("Luvut loppuivat, lopeta ohjelma.")
            
    elif choice == 2: # laskee  plus laskun
                
                result = lk.summa(num1, num2)
                
                #results_list.append(str(f"Summa {num1} + {num2} = {result}"))
                results_list.append(f"Summa {num1} + {num2} = {result}\n")
                print("Tulos lisätty listaan.")
            
    elif choice == 3:  # laskee jakolaskun
                
                result = lk.jako(num1, num2)
                
                #results_list.append(str(f"Osamäärä {num1} / {num2} = {result}"))
                results_list.append(f"Osamäärä {num1} / {num2} = {result}\n")
                print("Tulos lisätty listaan.")
        
    while choice != 0: # juoksee ympyrää kunnes lopetetaan = 0
                choice = int(input("Tämä laskin osaa seuraavat toiminnot:\n1) Anna luvut\n2) Summa\n3) Osamäärä\n0) Lopeta\nValitse toiminto (0-3): "))
                
                if choice == 1: # valinnan mukaan joku näistä jos lauseista toimii kutsulla
                    
                    if index < num_count:# kai vertailee numeroiden määrää indeksiin, jotta tietää milloin numerot loppuu
                        num1 = numbers_list[index]
                        num2 = numbers_list[index+1]
                    
                        index += 2# nostetaan indeksiä kahdella
                        print(f"Luettiin luvut {num1} ja {num2}")# printtaa sen hetkiset numerot jotka oli listalla seuraavaksi
                    else:# jos numerot pääsee loppumaan printtaa varoituksen
                        print("Luvut loppuivat, lopeta ohjelma.")
                
                elif choice == 2:
                    result = lk.summa(num1, num2)
                    results_list.append(f"Summa {num1} + {num2} = {result}\n")#results_list.append(str(f"Summa {num1} + {num2} = {result}"))
                    print("Tulos lisätty listaan.")
                
                elif choice == 3:
                    result = lk.jako(num1, num2)
                    results_list.append(f"Osamäärä {num1} / {num2} = {result}\n")#results_list.append(str(f"Osamäärä {num1} / {num2} = {result}"))
                    print("Tulos lisätty listaan.")
                elif choice == 0:
                    lk.kokeillaan(output_file, mode2)
                    with open(output_file, 'w', encoding="utf-8") as output_file_name:
                        for result in results_list:
                            output_file_name.write(result)
                        
                    print("Tallennettu tiedosto '"+str(output_file)+"'.")
                
                else: 
                    print("Tuntematon valinta, yritä uudestaan.")
                    
                    

        
    numbers_list.clear()# tyhjentää listat ja lopettaa ohjelman
    results_list.clear()
    input_file.close()
    

main()
print("Kiitos ohjelman käytöstä.")
