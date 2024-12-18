umnozak1 = 1
umnozak2 = 1
parni=0
treci=0
for i in range(10):
	broj = a=int(input("Unesite broj:"))
	if i == 2:
		treci = broj
	if i<5:
		umnozak1*=broj
	else:
		umnozak2*=broj
	if broj % 2 == 0:
		parni += 1
		
if treci % 3 == 0:
	print(umnozak1)
else:
	print(umnozak2)	

print("Broj parnih:", parni)
