
ostoslista = [] # alustetaan ostoslista (lista)
print("Ostoslistasi sisältää seuraavat tuotteet:")
print(ostoslista) # printtaa tuotteet

while True:
    print("Voit valita alla olevista toiminnoista:") # printtaa valikon
    print("1) Lisää")
    print("2) Poista")
    print("0) Lopeta")

    valinta = int(input("Valintasi: ")) # kysyy valintaa


    if valinta == 1: # jos haluaa lisätä
        lisays = input("Anna lisättävä tuote: ")
        ostoslista.append(lisays)

        print("\nOstoslistasi sisältää seuraavat tuotteet:") #kertoo lisäyksen jälkeisen tilanteen
        print(ostoslista)
        

    elif valinta == 2: # jos haluaa poistaa 
        
        print("Ostoslistassasi on",len(ostoslista), "tuotetta.") # kertoo numeroina listan pituuden
        #ostoslista.sort()
        poista = int(input("Anna poistettavan tuotteen järjestysnumero: ")) # kysyy minkä numeron poistaa
        del ostoslista[poista-1]

        print("\nOstoslistasi sisältää seuraavat tuotteet:") # kertoo poiston jälkeisen tilanteen
        print(ostoslista)


    elif valinta == 0: # jos haluaa lopetaa 
        print("Sinulta jäi ostamatta seuraavat tuotteet:") # kertoo jäikö jotain ostamatta
        print(ostoslista)

        print("Kiitos ohjelman käytöstä.") #kiittää ja kuittaa
        break


    else:
        print("Tunnistamaton valinta.") # extrana kertoo jos valintaa ei tunnisteta
        print("\nOstoslistasi sisältää seuraavat tuotteet:") # kertoo ostoslistan
        print(ostoslista)

