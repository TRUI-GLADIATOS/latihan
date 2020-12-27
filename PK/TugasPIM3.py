# 3
# Armelia Ramandha

angka = []
while True:
    inp = input('Masukkan angka: ')
    if inp == 'selesai':
        break
    try:
        angka.append(int(inp))
    except ValueError:
        print ('Error')
print (angka)

max = -1
min = None
for urutan in angka :
    if urutan > max :
        max = urutan
    if min is None :
        min = urutan
    elif urutan < min:
        min = urutan
print ('Maksimum :', max)
print ('Minimum  :', min)