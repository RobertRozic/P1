# Program za izračun zbroja brojeva do određenog broja

n = int(input("Unesi broj:")) # neki broj
zbroj = 0 # inicijaliziranje varijable zbroj
i = 1 # broj od kojeg krecemo zbrajanje

# sve dok nam je i manje od 10
while i <= n:
    print("i:", i)
    zbroj += i
    i += 1

print("i nakon izlaza iz while petlje:", i)
print("Zbroj brojeva je", zbroj)
    
