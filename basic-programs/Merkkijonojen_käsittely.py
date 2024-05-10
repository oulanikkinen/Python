#
import re

def read_file(filename):
    #"""lukee tiedoston ja palauttaa listan tiedoista"""
    try:
        with open(filename, 'r') as f:
            lines = f.readlines()
        print(f"Tiedosto '{filename}' luettu, {len(lines)} riviä.")
        
        return lines
    except FileNotFoundError:
        print(f"Tiedoston '{filename}' käsittelyssä virhe, lopetetaan.")
        exit()

def analyze_data(lines):
    #"""käsittelee tiedon ja palauttaa listaan ainoastaan hyväksytyt hommat"""
    acceptable_lines = []
    
    for i, line in enumerate(lines):
        # Skip the header line
        if i == 0:
            continue
        values = line.strip().split(';')
        
        if len(values) != 3:
            print(f"Väärä määrä arvoja, rivi {i+1}: '{line.strip()}'")
        
        else:
            # tarkistaa Idn
            id_pattern = r'^\d{4}$'

            if not re.match(id_pattern, values[0]):
                print(f"Virheellinen ID, rivi {i+1}: '{line.strip()}'")

            else:
                # Puhdistaa kommentit
                comment = re.sub(r'[^a-zA-Z0-9]', '', values[1])
                # tarkistaa ja asettaa arvostelupisteet
                
                try:
                    reputation_points = int(values[2])
                except ValueError:
                    reputation_points = 0
                acceptable_lines.append([values[0], comment, reputation_points])

    print(f"Tiedot analysoitu, {len(acceptable_lines)} hyväksyttävää tietoalkiota.")
    
    return acceptable_lines

def write_file(filename, data, header):
    #"""kirjoittaa tietoja uuteen tiedostoon"""
    with open(filename, 'w') as f:
        f.write(header)
        for d in data:
            f.write(f"{d[0]};{d[1]};{d[2]}\n")

    print(f"Tiedosto '{filename}' kirjoitettu, {len(data)+1} riviä.")

def main():
    # kysyy tiedostot ja lukee
    input_filename = input("Anna luettavan tiedoston nimi: ")
    output_filename = input("Anna kirjoitettavan tiedoston nimi: ")
    lines = read_file(input_filename)

    header = lines[0]

    # tutkii tietoja
    data = analyze_data(lines)

    # kirjoittaa uuteen tiedostoon
    write_file(output_filename, data, header)

    print("Kiitos ohjelman käytöstä.")

if __name__ == '__main__':
    main()