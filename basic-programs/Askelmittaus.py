#
input_file = input("Anna tiedot sisältävän tiedoston nimi: ")#
output_file = input("Anna tallennettavan tiedoston nimi: ")

# 
min_steps = 0 # 
max_steps = 0
total_steps = 0

file = open(input_file, "r", encoding="utf-8")
numbers = []
# 
for line in file:
    numbers.append(int(line))
    total_steps = sum(numbers)
    min_steps = min(numbers)

    max_steps = max(numbers)
    
# 
file.close()

# 
print("Pienin askelmäärä oli " +str(min_steps)+ " askelta.")
print("Suurin askelmäärä oli " +str(max_steps)+ " askelta.")
print("Yhteensä askelia oli " +str(total_steps)+ " askelta.")

# 
output_file = open(output_file, "w")

#
output_file.write("Pienin askelmäärä oli " +str(min_steps)+ " askelta." + "\n")
output_file.write("Suurin askelmäärä oli " +str(max_steps)+ " askelta." + "\n")
output_file.write("Yhteensä askelia oli " +str(total_steps)+ " askelta.")

#
output_file.close()
print("Kiitos ohjelman käytöstä.")#
