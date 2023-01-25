#Napišite program koji će ispisati
#sve troznamenkaste brojeve koji su djeljivi sa 7.
#Koliko takvih brojeva ima.
brojac = 0
for i in range(100, 1000):
    if i%7 == 0 and i % 5 == 0:
        print(i)
        brojac += 1

print("Takvih brojeva je: ", brojac)
