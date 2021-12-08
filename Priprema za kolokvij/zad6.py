a = 3
b = 8

print(3 * a % b)

if int(b/a) < 3 * a % b:
    a = 14
else:
    b = a+2
    print(a,b)
