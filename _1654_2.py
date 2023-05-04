import sys
K, N = map(int, sys.stdin.readline().split())
number = []
for i in range(K):
  number.append(int(sys.stdin.readline()))
min = 0
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

  
