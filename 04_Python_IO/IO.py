# Integer
a = 5
# Float
b = 5.5
# String
c = "Programiranje"
# Bool
d = True

'''
print(a, "je tipa", type(a))
print(b, "je tipa", type(b))
print(c, "je tipa", type(c))
print(d, "je tipa", type(d))

br_int = 5
br_flo = 1.23
br_zbroj = br_int + br_flo

print("Tip br_int je:", type(br_int))
print("Tip br_flo je:", type(br_flo))
print("Tip br_zbroj je:", type(br_zbroj))

print("Rezultat je", br_zbroj)
'''

br_int = 123
br_str = "456"
print("Tip br_str prije typecasting-a: ", type(br_str))
br_str = int(br_str)
print("Tip br_str poslije typecasting-a: ", type(br_str))
zbroj = br_int + br_str
print("Zbroj je:", zbroj)
