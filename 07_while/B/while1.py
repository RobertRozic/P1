# izračun zbroja brojeva do određenog broja
n = 10

suma = 0
i = 1

for i in range(n+1):
    suma += i

print("Zbroj pomocu for petlje:", suma)

suma = 0
i = 1
while i <= n:
    suma += i
    i += 1

print("Zbroj pomocu while petlje:", suma)

#while i <= n:
#    suma = suma + i
#    i = i+1
#
#print("Suma je", sum)
