count = int(input())

b = []

for i in range(count):
  b.append(input())



b.sort(key=len)
for i in range(count):
  print(b[i])
