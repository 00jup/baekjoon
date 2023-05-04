import sys
K, N = map(int, sys.stdin.readline().split())
print(K, N)
number = []
for i in range(K):
  number.append(int(sys.stdin.readline().strip()))
min = 1
max = max(number)
# def binarysearch(min, mid, max):
mid = int((max+min)/2)
while True: 
  count = 0
  for i in range(K):
    count += number[i] / mid
  if count >= N:
    print(mid)
    break
  mid = int((min+mid)/2)

  
