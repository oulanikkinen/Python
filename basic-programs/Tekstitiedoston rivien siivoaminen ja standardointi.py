#
def main():
  
  file_name = input("Anna luettavan tiedoston nimi: ")

  
  accepted_lines = []
  rejected_lines = 0

  
  with open(file_name, 'r') as f:
    for line in f:
      
      if not has_numbers(line):
        
        accepted_lines.append(line)
      else:
        
        rejected_lines += 1

  
  print(f"Luettiin {len(accepted_lines) + rejected_lines} riviä tiedostosta '{file_name}'.")
  print(f"Hylättiin {rejected_lines} riviä.")

  
  output_file_name = input("Anna kirjoitettavan tiedoston nimi: ")

  
  with open(output_file_name, 'w') as f:
    f.writelines(line.lower() for line in accepted_lines)

  
  print(f"Kirjoitettiin {len(accepted_lines)} riviä tiedostoon '{output_file_name}'.")
  print("Kiitos ohjelman käytöstä.")

def has_numbers(line):
  
  for character in line:
    if character.isdigit():
      return True
  return False


main()
