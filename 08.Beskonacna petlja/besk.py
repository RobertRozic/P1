# Beskonacna petlja

#while True: #ili while 1:
#    print("Pozdrav!")

'''
while 1:
    broj = int(input("Unesi paran broj"))
    if broj % 2 == 0:
        break

'''

while 1:
    broj = int(input("Unesi troznamenkasti broj"))
    #if broj > 99 or (broj < -99 and broj > -1000):
    if abs(broj) > 99 and abs(broj) < 1000:
        break
