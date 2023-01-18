'''
Napisati program koji za uneseni broj računa je li savršen. Za broj
kažemo da je savršen ako je jednak sumi svojih djelitelja (osim samog sebe).
Npr. 6 = 1+2+3
'''

for i in range(1, 1000):
#broj = int(input("Unesi broj: "))
    broj = i
    zbroj = 0

    for j in range(1, broj):
        if broj % j == 0:
            zbroj += j

    if zbroj == broj:
        print("Broj je savrsen!", broj)
    #else:
    #    print("Broj nije savrsen!", broj)

'''
Pronaci sve savršene brojeve od 1 do 1000
'''
