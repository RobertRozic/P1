n = int(input("Unesi broj"))

suma = 0

# Suma pomocu for petlje
#print(list(range(n)))
#for i in range(n):
#  suma += i 
#print(suma)

# Suma pomocu while petlje
brojac = 1

while brojac < n:
  suma += brojac # 0, 1, 3 ... 
  brojac += 1 # 1, 2, 3 ... 10
  
print(suma)
