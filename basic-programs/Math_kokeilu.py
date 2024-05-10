#
import math # tuodaan math ja random  kirjastot
import random

def calculate_area(radius):  #  määritellään ympyrän  yhtälö
  area = math.pi * math.pow(radius, 2)
  return area


def guess_number():   # määritellään luvunarvaus peli
    random.seed(1) # asettaa randomilla halutun luvun 
    target_number = random.randint(0, 1000)# rajaa random luvun kuitenkin 0 ja 1000 välille
    num_guesses = 0 # alustetaan arvaukset nollaan
    print("Arvaa ohjelman arpoma kokonaisluku.")
    while True: # aloitetaan arvaus looppi
        guess = int(input("Anna kokonaisluku välillä 0-1000: "))  # kysy arvausta hehe
        
        num_guesses += 1 # lisää arvaukset jälkeen yksi lisää muistiin
        
        if guess == target_number:# tarkistaa miten hyvä arvaus oli 
            print(f"Oikein! Käytit arvaamiseen {num_guesses} kierrosta.\n")
            break
        
        elif guess > target_number:
            print("Haettu luku on pienempi.")
        
        else:
            print("Haettu luku on suurempi.")


def main():   # pääruoka
    print("Tämä ohjelma käyttää kirjastoja tehtävien ratkaisemiseen.")
    while True:
        choice = int(input("Mitä haluat tehdä:\n1) Laskea ympyrän pinta-alan\n2) Arvata luvun\n0) Lopeta\nValintasi: "))  # tulostaa valikon
        if choice == 1: # ympyrän laskenta
            radius = int(input("Anna ympyrän säde kokonaislukuna: "))
            area = calculate_area(float(radius))
            
            print("Säteellä "+str(radius)+" ympyrän pinta-ala on "+format(area,".2f")+".\n")
        elif choice == 2: # arvauspeli
            guess_number()
        elif choice == 0: # haluaa lopettaa, kiittää käytöstä
            print("Kiitos ohjelman käytöstä.")
            break
        else:  # kertoo ettei ollut hyvä valinta
            print("Tuntematon valinta. Yritä uudelleen")

main()
