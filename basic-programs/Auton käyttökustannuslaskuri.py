
# 
import math

annual_kilometers = int(input("Anna vuotuiset kilometrit: "))
fuel_consumption = float(input("Anna moottorin polttoaineen kulutus (l/100km): "))
fuel_price = float(input("Anna polttoaineen hinta (€/l): "))
age_of_car = int(input("Anna auton ikä vuosissa: "))
insurance_amount = int(input("Anna vakuutusten määrä (euroissa): "))
bonus_percentage = int(input("Anna bonusprosentti kokonaislukuna: "))


bonus_amount = insurance_amount * (bonus_percentage / 100)


taxes = int(input("Anna verojen määrä: "))


hinta1 = (annual_kilometers / 100 * fuel_consumption * fuel_price + (insurance_amount - bonus_amount) + taxes + (200 * math.sqrt(age_of_car)))

hinta2 = (annual_kilometers / 100 * fuel_consumption * fuel_price + (insurance_amount - bonus_amount) + taxes + (200 * math.sqrt(age_of_car+1)))

hinta3 = (annual_kilometers / 100 * fuel_consumption * fuel_price + (insurance_amount - bonus_amount) + taxes + (200 * math.sqrt(age_of_car+2)))

hinta4 = (annual_kilometers / 100 * fuel_consumption * fuel_price + (insurance_amount - bonus_amount) + taxes + (200 * math.sqrt(age_of_car+3)))

hinta5 = (annual_kilometers / 100 * fuel_consumption * fuel_price + (insurance_amount - bonus_amount) + taxes + (200 * math.sqrt(age_of_car+4)))

#print(hinta1)
if hinta1 % 1 >= 0.5000:
    phinta1 = math.ceil(hinta1)
else:
    phinta1 = math.floor(hinta1)
#print(phinta1)
#print(hinta2)
if hinta2 % 1 >= 0.5000:
    phinta2 = math.ceil(hinta2)
else:
    phinta2 = math.floor(hinta2)
#print(phinta2)
#print(hinta3)
if hinta3 % 1 >= 0.5000:
    phinta3 = math.ceil(hinta3)
else:
    phinta3 = math.floor(hinta3)
#print(phinta3)
#print(hinta4)
if hinta4 % 1 >= 0.5000:
    phinta4 = math.ceil(hinta4)
else:
    phinta4 = math.floor(hinta4)
#print(phinta4)
#print(hinta5)
if hinta5 % 1 >= 0.5000:
    phinta5 = math.ceil(hinta5)
else:
    phinta5 = math.floor(hinta5)
#print(phinta5)

print("1. vuosi:", (phinta1))
print("2. vuosi:", (phinta2))
print("3. vuosi:", (phinta3))
print("4. vuosi:", (phinta4))
print("5. vuosi:", (phinta5))


total_operating_costs = (hinta1 + hinta2 + hinta3 + hinta4 + hinta5)
#print(total_operating_costs)
if total_operating_costs % 1 >= 0.5000:
    phinta6 = math.ceil(total_operating_costs)
else:
    phinta6 = math.floor(total_operating_costs)
#print(phinta6)

print("Viiden vuoden aikana autoon käytettiin rahaa", (phinta6), "euroa.")
print("Kiitos ohjelman käytöstä.")
