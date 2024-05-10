#
def rabbit_population(months):
  if months == 0:
    return 0
  elif months == 1:
    return 1

  # 
  prev = 0
  curr = 1

  # 
  for i in range(1, months + 1):
    next = prev + curr
    prev = curr
    curr = next

  return curr

# 
num_months = int(input("Anna kuukausien lukumäärä: "))
print(f"Kanipariskuntia on {num_months} kuukauden kuluttua {rabbit_population(num_months)}")
print("Kiitos ohjelman käytöstä.")
