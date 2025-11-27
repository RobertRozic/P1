a=11
b=3
a-= 2
d=a
c=d-b
a=2+a
if int(a/b) == (c%b)**2:
	b = c**2
	d = b
else:
	b -= 2

print(a+d*b)
