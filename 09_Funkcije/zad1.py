def dobarDan():
    print("Dobar dan!")
    
def pozdrav(ime):
    dobarDan()
    print("Pozdrav " + ime)

pozdrav("Ivan")
a = pozdrav("Robert")


def apsolutna(a):
    if a > 0:
        return a
    else:
        return -a

aps = apsolutna(-5)
print(aps)

print("Apsolutna vrijednost od -2 je: " + str(abs(-2)))



dobarDan()

print(min(15,-9,56,123,0))

print(len("abcde"))
print(len([1, 4, 2, 0, 12]))


print(min("abcde"))
print(max("abcde"))

print(ord("A"))
print(ord("a"))
print(chr(91), chr(92), chr(93), chr(94), chr(95), chr(96))


