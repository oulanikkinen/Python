#
sana1 = input("Anna sana 1: ")
sana2 = input("Anna sana 2: ")

if (sana1 < sana2): print("'" + str(sana1) + "' on aakkosissa aiemmin kuin '" + str(sana2) +"'.")
elif (sana1 > sana2): print("'" + str(sana2) + "' on aakkosissa aiemmin kuin '" + str(sana1)+"'.")
else: print("Sanat ovat samoja.")

if ("z" in sana1): print("Kirjain 'z' löytyy sanasta 1.")
if ("z" in sana2): print("Kirjain 'z' löytyy sanasta 2.")
else: print("Kummastakaan sanasta ei löytynyt kirjainta 'z'.")

sana3 = input("Anna testattava sana: ")
if (sana3[::] == sana3[::-1]): print("Antamasi sana '" + str(sana3) + "' on palindromi.")
else: print("Antamasi sana ei ole palindromi.\nSe on väärinpäin '" +str(sana3[::-1] + "' ja oikein päin '" + str(sana3) + "'."))

print("Kiitos ohjelman käytöstä.")
