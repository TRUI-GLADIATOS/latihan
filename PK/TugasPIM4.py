# 4
# Armelia Ramandha

file = open("ftest.txt")
count = 0
line = 0
receive = 0
for line in file:
    count += 1
    if line.startswith("Received") :
      print(line)
    if line.count('Received') :
        receive += 1
print ('Line count :', count)
print ('Line starts with recieved :', receive)