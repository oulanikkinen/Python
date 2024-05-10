
class Product: # määritellään tavara lista
  
  def __init__(self, identifier, quantity, price):

    self.identifier = identifier

    self.quantity = quantity

    self.price = price


def valikko(): # valikko 

    choice = int(input("Mitä haluat tehdä:\n1) Lue tiedosto\n2) Analysoi tiedot\n3) Tallenna Tulokset\n0) Lopeta\nValintasi: "))

    return choice


def read_file(file_name):# lukee tiedoston

  lines_list = []

  with open(file_name, "r") as f:

    for line in f:
      # jakaa tiedoston rivit omiin infobokseihin
      identifier, quantity, price = line.strip().split(";")

      quantity = int(quantity)

      price = float(price.replace(",", "."))

      # tehdään tavara olio ja tallennetaan tavaran tiedot
      product = Product(identifier, quantity, price)

      lines_list.append(product)

  return lines_list

# analysoi tiedoston tiedot
def analyze_data(lines_list):

  results_list = []

  total_value = 0

  for product in lines_list:

    value = product.quantity * product.price # laskee hinnan tehtävänannon  kaavalla

    results_list.append(value)  # lisää tämä pääohjelman listaan

    total_value += int(product.quantity) * float(product.price) # laskee yhteisarvon
  
  results_list.append(total_value) # lisää listaan
   
  return results_list


def save_results(results_list, file_name):  # tallentaa tiedot haluttuun tiedostoon


  with open(file_name, "w") as f: # tiedoston avaus juttuja
    

    for value in results_list:  # käy for loppilla läpi kaikki tallennettavat

      f.write(f"{value:.2f}\n")
      