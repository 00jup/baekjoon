import sys
input = sys.stdin.readline
K, N = map(int, input().split())
number = []
for _ in range(K):
  number.append(int(input()))
min = 0
max = max(number)
mid = int((max+min)//2)
while True: 
  count = 0
  for i in range(K):
    count += number[i] // mid
  if count >= N:
    print(mid)
    break
  mid = int((min+mid)//2)

  
