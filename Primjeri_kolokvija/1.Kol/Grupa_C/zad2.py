a=input("Unesi prvu rijec:")
b=input("Unesi drugi rijec:")
c=input("Unesi treci rijec:")

if a == b or b == c or c == a:
	print("Unesene su najmanje dvije jednake rijeci")
	
print(a[::2])
print(b[::2])
print(c[::2])
