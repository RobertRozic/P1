# 5. Definirati funkciju koja provjerava je li broj prost ili ne te kao rezultat vraća boolean.

def jeLiProst(broj):
    # pretpostavimo da je broj prost
    prost = True
    # postavimo brojac na 2
    i = 2
    # vrtimo petlju sve dok brojac ne dosegne broj
    while i < broj:
        # ukoliko broj podijeljen s brojacem daje ostatak 0
        if broj % i == 0:
            # broj nije prost i postavljamo boolean na false
            prost = False
            # izlazimo iz while petlje jer vise nema potrebe provjeravati djeljivost
            break
        # Uvecavanje brojaca za 1    
        i += 1
    # Vracamo rezultat u obliku booleana    
    return prost
    
a = int(input("Unesi broj"))

if jeLiProst(a):
    print("Broj je prost")
else:
    print("Broj nije prost")


