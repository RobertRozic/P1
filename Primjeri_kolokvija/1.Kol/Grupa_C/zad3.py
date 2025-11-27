zbroj = 0
brojac1=0
brojac2=0

for i in range(10):
    broj = float(input("Unesi broj:"))
    if broj >= 3 and broj <= 7:
        zbroj += broj
        brojac1 += 1
    else:
    	brojac2 += 1

print("Prosjek je:", zbroj/brojac1)   
print("Brojevi koji nisu uzeti u obzir:", brojac2) 
