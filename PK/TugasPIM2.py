# 2
# Armelia Ramandha

a=int(input("NPM: "))
c=a%10

if (c % 2) == 0 :
    b = 7
else :
    b = 17

x = 1
while x <= 50:
    suku = a + (x-1) * b
    print(suku)
    x += 1
