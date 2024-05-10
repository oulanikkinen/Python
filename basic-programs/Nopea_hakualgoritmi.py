#
import time
import sys

def searchfunc(filename):
    # alustetaan lista nollaksi
    numbers = [0, 0]

    # avataan tiedosto ja aloitetaan luku
    try:
        with open(filename, 'r') as f:
            num_list = [int(x) for x in f.read().split()]
    except FileNotFoundError:
        print(f"Tiedoston '{filename}' käsittelyssä virhe, lopetetaan.")
        sys.exit()
    # Loopataan numeroiden läpi etsien oikeaa
    for i in range(len(num_list)):
        for j in range(i + 1, len(num_list)):
            if num_list[i] < num_list[j] / 3:
                numbers[0] = num_list[i]
                numbers[1] = num_list[j]
                return numbers

    # Jos ei löydy niin palauttaa nollat
    return numbers

def main():
    filename = input("Anna tiedoston nimi: ")
    
    Clock1 = time.perf_counter()
    Results = searchfunc(filename)
    Clock2 = time.perf_counter()
    Time = Clock2 - Clock1

    if ((Results[0] == 0) and (Results[1] == 0)):
        print("Hakualgoritmi ei löytänyt sopivaa lukuparia.")
        print("Kiitos ohjelman käytöstä.")
        sys.exit()

    #elif (Time > 2):
        print("Hakualgoritmi ei ollut tarpeeksi nopea.")
        print("Kiitos ohjelman käytöstä.")
        sys.exit()

    else:
         print("Hakualgoritmi oli riittävän nopea!")
         print("Se löysi sopivan parin:", Results[0], "ja", Results[1])


main()
print("Kiitos ohjelman käytöstä.")