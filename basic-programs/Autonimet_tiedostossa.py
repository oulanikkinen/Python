#
def read_file(file_name, car_brands):
  
  try:
    with open(file_name, 'r') as f:
      
      for line in f:
        car_brands.append(line.strip())
  
  except:
    print(f"Tiedoston '{file_name}'käsittelyssä virhe, lopetetaan.")

def analyze_data(car_brands):
  
  different_brands = set()
  
  for brand in car_brands:
    different_brands.add(brand)
  
  return different_brands

def write_file(file_name, different_brands):
  
  try:
    with open(file_name, 'w') as f:
      
      for brand in different_brands:
        f.write(brand + '\n')
  
  except:
    print(f"Tiedoston '{file_name}' käsittelyssä virhe, lopetetaan.")
    exit()

def main():
  
  car_brands = []
  
  file_to_read = input("Anna luettavan tiedoston nimi: ")
  file_to_write = input("Anna kirjoitettavan tiedoston nimi: ")
  read_file(file_to_read, car_brands)
  
  if not car_brands:
    print("Tiedosto oli tyhjä, yhtään automerkkiä ei tunnistettu.")
  
  else:
    different_brands = analyze_data(car_brands)
    print(f"Tiedostossa oli {len(different_brands)} eri automerkkiä.")
    
    
    for brand in sorted(different_brands):
      
      print(brand)
      write_file(file_to_write, sorted(different_brands))
  
  print("Kiitos ohjelman käytöstä.")


main()
