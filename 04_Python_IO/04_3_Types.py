a = 5
b = 5.5
c = "Proramiranje"
d = False
e = None

'''
print(a, "je tipa", type(a))
print(b, "je tipa", type(b))
print(c, "je tipa", type(c))
print(d, "je tipa", type(d))
print(e, "je tipa", type(e))


zbroj = 5 + int("5")
print(type(zbroj), "Zbroj je", zbroj)
'''

br_int = 123
br_str = "457.99"

br_int = str(br_int)
print("Tip br_str prije typecasting-a: ", type(br_str))
#br_str = float(br_str)
#br_str = int(br_str)
#print("Tip br_str poslije typecasting-a: ", type(br_str))

zbroj = br_int + br_str

print("Tip zbroj:", type(zbroj))
print("Vrijednost zbroj:", zbroj)

