broj = int(input("Unesi troznamenkasti broj:"))

if broj >= 100 and broj < 1000:
    print("Broj je troznamenkast.")
    zadnja = broj % 10
    print("zadnja je:", zadnja)
    predzadnja = (broj % 100) // 10
    #treca_sa_zada = (broj % 1000) // 100 itd. 
    print("predzadnja je:", predzadnja)
    if zadnja % 3 == 0:
        print("zadnja znamenka je djeljiva s 3")
    else:
        print("zadnja znamenka nije djeljiva s 3")
else:
    print("Broj nije troznamenkast.")
