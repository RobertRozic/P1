#x = int(input("Unesi broj:"))
'''
i = 2
prost = True
while 1:
  if i >= x:
    break
  if x % i == 0:
    prost = False
    break
  i += 1

if prost:
  print("Broj je prost")
else:
  print("Broj nije prost")
'''

def jeLiProst(x):
  i = 2
  prost = True
#  while 1:
#    if i >= x:
#       break
  while i < x:
    if x % i == 0:
      prost = False
      break
    i += 1
  return prost

rez = jeLiProst(7)
print(rez)
