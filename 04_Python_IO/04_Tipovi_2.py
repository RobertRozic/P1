'''
br_int = 5 # definiramo broj kao integer
br_flo = 1.23 # definiramo broj kao float
br_novi = br_int + br_flo # zbrajamo integer i float

print("Tip br_int:", type(br_int))
print("Tip br_flo:", type(br_flo))

print("Vrijednost br_novi:", br_novi)
print("Tip br_novi:", type(br_novi))
'''

br_int = 123
br_str = "456"

print("Tip br_str prije typecasting-a: ", type(br_str))

br_str = int(br_str)

print("Tip br_str poslije typecasting-a: ", type(br_str))

zbroj = br_int + br_str

print("Tip zbroj:", type(zbroj))
print("Vrijednost zbroj:", zbroj)


