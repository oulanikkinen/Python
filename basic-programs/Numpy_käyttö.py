#
import numpy as np

# Luo 4x4-kokonaislukumatriisi ja alusta se nolliksi numpyn zeros-jäsenfunktiolla
matrix = np.zeros((4, 4), dtype=int)

# käy läpi matriisin kaikki alkiot kahdella silmukalla rivi ja sarakkeet
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        # antaa arvon jokaiselle rivi ja sarake kohdalle perustuen sen sijaintiin 
        matrix[i][j] = (i + 1) * (j + 1)

# printtaa sen otsikko tekstin
print("Tämä ohjelma esittelee numpy-matriisin käyttöä.\nMatriisi tulostettuna numpy-muotoilulla:")

print(matrix)

# printtaa alkiot valmiiksi eroteltuina
print("\nMatriisi tulostettuna alkiot puolipisteillä eroteltuna:")
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        print(matrix[i][j], end=';')
    print()

print("\nKiitos ohjelman käytöstä.")
