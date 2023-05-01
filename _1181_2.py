count = int(input())

b = []

for i in range(count):
  b.append(input())

a = list(set(b))
a.sort() ##이걸 왜 해야 되는 거지?
a.sort(key=len)
for i in a:
  print(i)
