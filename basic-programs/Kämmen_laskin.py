#
while True:
 print("Tämä laskin osaa seuraavat toiminnot:")
 print("1) Anna luvut")
 print("2) Summa")
 print("3) Erotus")
 print("4) Tulo")
 print("5) Osamäärä")
 print("6) Potenssi")
 print("0) Lopeta")

 toiminto = int(input("Valitse toiminto (0-6): "))
 
 if toiminto == 1:
     eka_luku = int(input("Anna ensimmäinen luku: "))
     toka_luku = int(input("Anna toinen luku: "));
     print("Annoit luvut " + str(eka_luku) + " ja " + str(toka_luku))
     
 elif toiminto == 5 and toka_luku == 0:
     print("Nollalla ei voi jakaa.")
 
 elif toiminto ==  2:
     summa = eka_luku + toka_luku;
     print("Summa " + str(eka_luku) + " + " + str(toka_luku) + " = " + str(summa))
     
 elif toiminto == 3:
     erotus = eka_luku - toka_luku;
     print("Erotus " + str(eka_luku) + " - " + str(toka_luku) + " = " + str(erotus))

 elif toiminto == 4:
     tulo = eka_luku * toka_luku;
     print("Tulo " + str(eka_luku) + " * " + str(toka_luku) + " = " + str(tulo))

 elif toiminto == 5 and toka_luku != 0:
     osa = eka_luku / toka_luku;
     print("Osamäärä " + str(eka_luku) + " / " + str(toka_luku) + " = " + str(round(osa, 2)))

 elif toiminto == 6:
     pot = eka_luku ** toka_luku;
     print("Potenssi " + str(eka_luku) + " ** " + str(toka_luku) + " = " + str(pot))

 elif toiminto == 0:
     print("Lopetetaan")
     break
 else: print("Tuntematon valinta, yritä uudestaan.")

print("Kiitos ohjelman käytöstä.")

#