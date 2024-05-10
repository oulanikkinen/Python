#
def test_index_error():
    # Testaa IndexError käyttämällä luetteloa, jossa on elementit 11, 22, 33, 44 ja 55
    test_list = [11, 22, 33, 44, 55]

    try:
        # Pyydä käyttäjää syöttämään indeksi väliltä 0–4
        index = int(input("Anna indeksi 0-4: "))

        # Yritä käyttää luettelon annetussa hakemistossa olevaa elementtiä
        element = test_list[index]
        print("Listan arvo on "+str(element)+" indeksillä "+str(index)+".")

    except IndexError:
        # Ilmoita käyttäjälle IndexError-virheestä
        print(f"Tuli IndexError, indeksi {index}.")


def test_zero_division_error():
    # Testaa ZeroDivisionError jakolaskelmassa
    try:
        # Pyydä käyttäjää syöttämään jakaja
        divisor = int(input("Anna jakaja: "))
        # Suorita jakolaskenta
        result = float(4 / divisor)
        
        #print("+ str(result)+")
        print("4/"+ str(divisor) + " on "+("%.2f"%result)+".")

    except ZeroDivisionError:
        # Ilmoita käyttäjälle ZeroDivisionError-virheestä
        print(f"Tuli ZeroDivisionError, jakaja {divisor}.")


def test_type_error():
    # Testaa TypeError, kun yrität kertoa kaksi merkkijonoa yhteen
    try:
        # Pyydä käyttäjää syöttämään numero
        number = (input("Anna numero: "))
        # Yritä kertoa luku itsellään
        result = number * number
    except TypeError:
        # Ilmoita käyttäjälle TypeError-virheestä
        print(f"Tuli TypeError, {number}*{number} merkkijonoilla ei onnistunut.")



def main():

    while True:
        # printtaa valikko
        #kysy haluttua
        choice = input("Mitä haluat tehdä:\n1) Testaa ValueError\n2) Testaa IndexError\n3) Testaa ZeroDivisionError\n4) Testaa TypeError\n0) Lopeta\nValintasi: ")
        while True:       #  loopilla kunnes laittaa kokonaisluvun
            try:
                choice = int(choice)
                break
            except ValueError:
                choice = input("Anna valinta kokonaislukuna.\nValintasi: ")
                
                
        
        if choice == 1:# testaa valueerrorin
            print("Valikko-ohjelma testaa ValueError'n.")

            # testa indexerror
        elif choice == 2:
            test_index_error()
            
            # testaa ZeroDivisionError
        elif choice == 3:
            test_zero_division_error()

            # testaa TypeError
        elif choice == 4:
            test_type_error()

            # lopettaa
        elif choice == 0:
            print("Kiitos ohjelman käytöstä.")
            break
            # väärä valinta

        else:
            print("Valintaa ei tunnistettu, yritä uudestaan.")
main()