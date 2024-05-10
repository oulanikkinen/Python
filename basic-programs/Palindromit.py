#
input_file_name = input("Anna luettavan tiedoston nimi: ")
output_file_name = "L06T3T1.txt"


input_file = open(input_file_name, "r")
output_file = open(output_file_name, "w")


for line in input_file:
  
  line = line.strip()

  
  if line.isdigit():
    
    print("Rivi '"+ line + "' on numerorivi.")
    continue

  
  if line == line[::-1]:
    
    output_file.write(line + "\n")
    print("Rivi '"+ line + "' on palindromi.")
  else:
    
    print("Rivi '"+ line + "' ei ole palindromi.")


input_file.close()
output_file.close()
print("Kiitos ohjelman käytöstä.")#prints lovely thanks message