#
tiedosto =  input("Anna tiedoston nimi: ")
with open(tiedosto) as f:
    # skippaa ekan rivin  "otsikko"
    next(f)

    # käy läpi ne loput rivit
    for line in f:
        # jakaa tiedot tollasella pistepilkulla
        data = line.split(';')

        # erottelee ajan ja nimen 
        aika = data[2].strip()
        marja = data[0].strip()

        # printtaa arvot tekstin sisällä
        print(f"Kello oli {aika}, kun punnittiin marjoja {marja}.")

print("Kiitos ohjelman käytöstä.")
