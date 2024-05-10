#
import sys

def read_file(input_filename): # lukee tiedoston
    try:# olettaa ettei löydy
        with open(input_filename, "r") as f:
            return [line.strip() for line in f]
    except:# plan b jos ei löydy
        print(f"Tiedoston '{input_filename}' käsittelyssä virhe, lopetetaan.")
        sys.exit()

def analyze_data(data):# analysoi dataa

    car_count = {}# listaus määrälle

    for car in data:# käy kaikki läpi
        if car in car_count:
            car_count[car] += 1
        else:
            car_count[car] = 1

    return car_count# palauttaa määrän

def write_file(output_filename, car_count, car_brands_count, cars_count):# kirjaa tiedostoon paljon tietoa

    with open(output_filename, "w") as f:
        f.write(f"Tunnistettiin {car_brands_count} automerkkiä ja {cars_count} autoa:\n")# otsikko

        for car, count in sorted(car_count.items()):# kaikki merkki+määrä
            if count == 1: 
                f.write(f"{car}: 1 auto\n")
            else:
                f.write(f"{car}: {count} autoa\n")

def main():# pääruoka

    input_filename = input("Anna luettavan tiedoston nimi: ")#kysyy halutut tiedostot
    output_filename = input("Anna kirjoitettavan tiedoston nimi: ")

    data = read_file(input_filename)# kutsuu luennolle 
    if not data:
        print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")# jos tiedosto tyhjä heittää tämän
        return

    car_count = analyze_data(data)# kutsuu analysoimaan
    car_brands_count = len(car_count)#laskee itse
    cars_count = sum(car_count.values())#laskee itse
    write_file(output_filename, car_count, car_brands_count, cars_count)#kutsuu kirjoittamaan

    print(f"Tunnistettiin {car_brands_count} automerkkiä ja {cars_count} autoa:")#otsikko

    for car, count in sorted(car_count.items()):# kaikki merkki+määrä
        if count == 1:
            print(f"{car}: 1 auto")
        else:
            print(f"{car}: {count} autoa")

    

main()# kutsuu pääruokaa
print("Kiitos ohjelman käytöstä.")# kiittää ja kuittaa