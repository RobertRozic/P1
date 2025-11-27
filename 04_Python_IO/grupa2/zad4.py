'''
a = 5
b = 5.5
c = "Programiranje"
d = False

print(a, "je tipa", type(a))
print(b, "je tipa", type(b))
print(c, "je tipa", type(c))
print(d, "je tipa", type(d))


br_int = 5
br_flo = 1.23
br_zbroj = br_int + br_flo

print("Br int je tip", type(br_int))
print("Br flo je tip", type(br_flo))
print("Rezultat je:", br_zbroj)
print("Zbroj je tip:", type(br_zbroj))
'''

br_int = 123
br_str = "456"
print("Tip br_str prije typecasting-a: ", type(br_str))
br_str = int(br_str)
print("Tip br_str prije typecasting-a: ", type(br_str))
zbroj = br_int + br_str
print("Zbroj je:", zbroj)
