'''
Napišite program koji će ispisati sve troznamenkaste brojeve
koji su djeljivi sa 7.
'''

for i in range(100,1000,1):
    if i % 7 == 0:
        print("Broj", i, "je djeljiv sa 7!")

print('--------------------')

for i in range(105,1000,7):
    print("Broj", i, "je djeljiv sa 7!")
