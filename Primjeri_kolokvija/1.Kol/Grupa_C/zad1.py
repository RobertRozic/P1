a=int(input("Unesi prvi broj:"))
b=int(input("Unesi drugi broj:"))
c=int(input("Unesi treci broj:"))

najveci = a
najmanji = b
if b > najveci:
	najveci = b
	namjanji = a
if c > najveci:
	najveci = c
	najmanji = a
elif a > c:
	najmanji = c	


prosjek = (a+b+c)/3

if prosjek > 30:
	print(najveci**2 - najmanji**2)
	print(a*b*c)
else:
	print(najveci%najmanji)
