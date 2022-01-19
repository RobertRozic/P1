def jeLiProst(x):
    prost = True
    i = 2
    while i < broj:
        if broj % i == 0:
            prost = False
            break
        i += 1
    return prost


while 1:
    broj = int(input("Unesite broj:"))
    if broj == 0:
        break
    test = jeLiProst(broj)

    if test:
        print("Broj je prost")
    else:
        print("Broj nije prost")
        
