# Napišite program koji će ispisati
# sve troznamenkaste brojeve
# koji su djeljivi sa 7.

print("Troznamenkasti brojevi djeljivi sa 7 su:")
for i in range(100, 1000):
    if i % 7 == 0:
        print(i)
