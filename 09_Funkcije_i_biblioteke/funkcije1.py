def pozdrav(ime):
    dobarDan()
    sretanRodjendan(ime, 27)
    print("Dobar dan:", ime)

def dobarDan():
    print("Dobar dan!")
    #return "test"

def sretanRodjendan(ime, godine):
    print("Sretan", godine, "rodjendan", ime)

pozdrav("Ana")
dobarDan()
sretanRodjendan("Robert", 27)

test = dobarDan()
print(test)

