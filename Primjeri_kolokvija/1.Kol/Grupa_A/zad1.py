a=int(input("Unesi prvi broj:"))
b=int(input("Unesi drugi broj:"))
veci = a
manji = b
if b > a:
	veci = b
	manji = a

if (a+b) > 50:
	print("Razlika kvadrata je", a**2 - b**2)
else:
	if(manji == 0):
		print("Dijeljenje je nemoguce")
	else:
		print(veci/manji)	
