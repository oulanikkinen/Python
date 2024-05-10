#
def comp_numbers(a,b):
   
    if a > b:
        print("Testatuista luvuista "  + str(a)+ " on suurempi kuin "+ str(b))
        
        return a
    elif b > a:
        print("Testatuista luvuista "  + str(b)+ " on suurempi kuin "+ str(a))
        
        return b 
    else:
        print("Luvut ovat samansuuruiset.")
        
        return a
def comp_numbers2(a,b):
   
    if a > b:
        #print("Testatuista luvuista "  + str(a)+ " on suurempi kuin "+ str(b))
        
        return b
    elif b > a:
        #print("Testatuista luvuista "  + str(b)+ " on suurempi kuin "+ str(a))
        
        return a 
    else:
        #print("Luvut ovat samansuuruiset.")
        
        return a 

a = int(input("Anna ensimmäinen luku: "))
b = int(input("Anna toinen luku: "))

greater = comp_numbers(a, b)
lower = comp_numbers2(a, b)


d = int(input("Paljonko vähennetään suuremmasta luvusta: "))

erotus = greater - d

greater = comp_numbers(erotus, lower)


   # print("Testatuista luvuista "+ str(greater)+ " on suurempi kuin "+  str(erotus))

print("Kiitos ohjelman käytöstä.")
