a='kolokvij'
b='test'
if a[2:7] != 'olo':
	if b[3] == 't':
		b=str(2**2-3)
elif b[::2] == 'ts':
	b=str(6%3)

print(b + a)
