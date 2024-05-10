#
import datetime

# Hankkii kuukauden ja vuoden käyttäjältä
yy = int(input("Anna vuosi: "))
mm = int(input("Anna kuukausi: "))

# kuun eka päivä
first_day = datetime.date(yy, mm, 1)
# Tarkistaa onko kuukausi joulukuu
if mm == 12:
    
    next_year = yy + 1
    next_month = 1
else:
    # 
    next_year = yy
    next_month = mm + 1

#  viikon eka päivä 0=ma 6=su
day_of_week = first_day.weekday()

# kuun vika
last_day = datetime.date(next_year, next_month, 1) - datetime.timedelta(days=1)
num_days_in_month = last_day.day

# tulostaa tulostuksia
print("Kalenteri näyttää seuraavalle:")
#print(month_name, yy)

# printtaa viikonpäivät
print(' Ma', 'Ti', 'Ke', 'To', 'Pe', 'La', 'Su')

# alustaa päivälaskurin
day = 1

# printtaa ekan sarakkeen
#print(' ', end='')
for i in range(7):
    if i < day_of_week:
        # jos eka päivä ei oo maanantai laittaa tyhjiä kunnes eka päivä
        print('  ', end=' ')
    else:
        # tasaa oikealle 2 merkillä
        print(" {:>2d}".format(day), end='')
        day += 1
print('',end='\n')

# printtaa loput sarakkeet
while day <= num_days_in_month:
    print('', end='')
    for i in range(7):
        
        # tasauttaa myös oikealle
        print(" {:>2d}".format(day), end='')
        day += 1
        if day > num_days_in_month:
            break
    if day <= num_days_in_month:
        print()
