
# Kutsutaan lämpötilamuunnos kirjastoa
import lämpötilan_muuttuja_kirjasto as lmk

# printataan kirjaston versio
print(f"Käytetään lämpötilamuunnoskirjaston versiota {lmk.VERSION}")

# printataan vaihtoehdot ja kysytään haluttua toimintoa.
while True:
    choice = int(input("Minkä lämpötilamuunnoksen haluat tehdä?\n1) Celsius->Fahrenheit\n2) Celsius->Kelvin\n3) Fahrenheit->Kelvin\n4) Fahrenheit->Celsius\n5) Kelvin->Celsius\n6) Kelvin->Fahrenheit\n0) Lopeta\nValintasi: "))  # tulostaa valikon
    if choice == 1:
      temperature = int(input("Anna lähtölämpötila: "))
      result = lmk.celsius_to_fahrenheit(temperature)
      print("Lämpötila Fahrenheit asteina:",round(result,2),end=""+"\n")
      print()

    elif choice == 2:
      temperature = int(input("Anna lähtölämpötila: "))
      result = lmk.celsius_to_kelvin(temperature)
      print("Lämpötila Kelvin asteina:", round(result,2),end=""+"\n")
      print()

    elif choice == 3:
      temperature = int(input("Anna lähtölämpötila: "))
      result = lmk.fahrenheit_to_kelvin(temperature)
      print("Lämpötila Kelvin asteina:", round(result,2),end=""+"\n")
      print()

    elif choice == 4:
      temperature = int(input("Anna lähtölämpötila: "))
      result = lmk.fahrenheit_to_celsius(temperature)
      print("Lämpötila Celsius asteina:", round(result,2),end=""+"\n")
      print()

    elif choice == 5:
      temperature = int(input("Anna lähtölämpötila: "))
      result = lmk.kelvin_to_celsius(temperature)
      print("Lämpötila Celsius asteina:", round(result,2),end=""+"\n")
      print()

    elif choice == 6:
      temperature = int(input("Anna lähtölämpötila: "))
      result = lmk.kelvin_to_fahrenheit(temperature)
      print("Lämpötila Fahrenheit asteina:", round(result,2),end=""+"\n")
      print()

    elif choice == 0:
      print("Kiitos ohjelman käytöstä.")
      break

    else:
      print("Valintaa ei tunnistettu, yritä uudestaan.")
      print()

