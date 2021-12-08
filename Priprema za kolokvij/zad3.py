suma = 0
brojac = 0
parni = 0
for i in range(10):
    print("i nam je: ", i)
    unos = int(input("Unesi broj:"))
    # npr. treci broj
    if i == 2:
        treci = unos
    #veći ili jednaki 2 i manji ili jednaki 5.
    if unos >= 2 and unos <= 5:
        brojac += 1
        suma += unos # isto kao suma = suma + unos
    # npr prvih pet brojeva
    #if i > 1:
    #    ....
    # brojanje parnih brojeva
    #if unos % 2 == 0:
    #        parni += 1   
        
if brojac > 0:
    print("Prosjek je:", suma/brojac)
