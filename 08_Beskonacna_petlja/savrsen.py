'''
Napisati program koji za uneseni
broj računa je li savršen.
Za broj kažemo da je savršen ako je jednak
zbroju svojih djelitelja (osim samog sebe).
Npr. 6 = 1+2+3
Pronaci sve savršene brojeve od 1 do 1000.
'''

#broj = int(input("Unesi broj:"))

for broj in range(1,1000):
    zbroj = 0
    for i in range(1, broj):
        if broj % i == 0:
            zbroj += i

    if zbroj == broj:
        print("Broj", broj, "je savrsen!")



