a = int(input("Unesi stranicu a: "))
b = int(input("Unesi stranicu b: "))

if a == b:
    print('Unijeli ste kvadrat')

if a < 0 or b < 0:
    print("Jedan od unosa je manji od 0.")
else:
    opseg = 2*a + 2*b # 2 * (a+2) opseg pravokutnika
    povrsina = a*b # povrsina pravokutnika
    if a > b:
        print("Opseg je", opseg)
    else:
        print("Povrsina je", povrsina)
