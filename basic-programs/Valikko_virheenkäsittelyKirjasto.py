
def askForFileName():
    file_name = input("Anna luettavan tiedoston nimi: ")
    return file_name

def readFile(file_name):
    # luo tyhjän listan kaikelle tiedolle
    
    data = []
    
    try:
        # Open the file
        with open(file_name, "r") as file:
        # Read the lines from the file
            lines = file.readlines()

        # Process each line
        for line in lines:
            # Split the line into fields
            fields = line.strip().split(";")
            # Create a Person object and add it to the list
            data.append(Person(fields[0], fields[1], int(fields[2])))
    except IOError:
        print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(file_name))
        exit()

    return data

def writeFile(file_name, data):
  # Ask for the age of the persons to be included in the new file
  age = int(input("Minkä ikäiset ihmiset otetaan mukaan tiedostoon (vuosia): "))

  # Create a list of the persons who have reached the given age
  filtered_data = [person for person in data if person.age >= age]

  try:
    # Open the file
    with open('L13T1T1.txt', "w") as file:
        # Write the header line
        file.write("Tiedostossa on mukana {} vähintään {} vuotiasta henkilöä:\n".format(len(filtered_data), age))
        # Write the data
        for person in filtered_data:
            file.write("{};{};{}\n".format(person.name, person.phone, person.age))

  except IOError:
    print("Tiedoston '{}' käsittelyssä virhe, lopetetaan.".format(file_name))
    exit()

def printData(data):
    # tulostaa tiedot
    for person in data:
        print("{} on {} vuotta vanha ja hänen puhelinnumero on {}.".format(person.name, person.age, person.phone))

# luokittelu henkilön tiedoille
class Person:
    def __init__(self, name, phone, age):
        self.name = name
        self.phone = phone
        self.age = age
