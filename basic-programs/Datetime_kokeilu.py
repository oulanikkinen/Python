#
import datetime #tuodaan datetime kirjasto


def get_date_time(): # määritellään päivä+aika combon printtaus
  date_time_str = input("Anna päivämäärä ja kello muodossa 'pp.kk.vvvv hh:mm': ")
  date_time_obj = datetime.datetime.strptime(date_time_str, "%d.%m.%Y %H:%M")
  print("Annoit vuoden", date_time_obj.year)
  print("Annoit kuukauden", date_time_obj.month)
  print("Annoit päivän", date_time_obj.day)
  print("Annoit tunnin", date_time_obj.hour)
  print("Annoit minuutin", date_time_obj.minute)


def get_age_in_days(): # määritellään iän laskeminen annetusta ajasta vakio päivään asti
  birthday_str = input("Anna syntymäpäiväsi muodossa pp.kk.vvvv: ")
  birthday_obj = datetime.datetime.strptime(birthday_str, "%d.%m.%Y")
  january_1_2000 = datetime.datetime(2000, 1, 1)
  age_in_days = (january_1_2000 - birthday_obj).days
  print("1.1.2000 sinä olit", age_in_days, "päivää vanha.")


def print_days_of_week(): # määritellään viikonpäivien vakio printtaus
  monday = datetime.datetime(2022, 1, 3)  # maanantai  ensin
  for i in range(7):
    print(monday.strftime("%A"))
    monday += datetime.timedelta(days=1)


def print_months(): # määritellään kuukausien vakio printtaus
  january = datetime.datetime(2022, 1, 1)  # aloittaa tammikuusta
  for i in range(12):
    print(january.strftime("%b"))
    january += datetime.timedelta(days=31)  # vaihto seuraavaan  kuuhun


def main():
  print("Tämä ohjelma käyttää datetime-kirjastoa tehtävien ratkaisemiseen.")
  while True: # printataan vaihtoehdot ja kysytään haluttua toimintoa.
    choice = int(input("Mitä haluat tehdä:\n1) Tunnistaa aika-olion komponentit\n2) Laskea iän päivinä\n3) Tulostaa viikonpäivät\n4) Tulostaa kuukaudet\n0) Lopeta\nValintasi: "))
    
    if choice == 1: # päivä+aika combo
      get_date_time()
      print()
    
    elif choice == 2: # iän laskeminen päivissä
      get_age_in_days()
      print()
    
    elif choice == 3: # viikonpäivien printtaus
      print_days_of_week()
      print()
    
    elif choice == 4: # kuukausien printtaus
      print_months()
      print()
    
    elif choice == 0: # lopetus plus kiitokset
      print("Kiitos ohjelman käytöstä.")
      break
    
    else: # väärä valinta
        print("Valintaa ei tunnistettu, yritä uudestaan.")

main()
