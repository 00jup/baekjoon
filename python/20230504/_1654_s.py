import sys
input = sys.stdin.readline
K, N = map(int, input().split())
number = []
for _ in range(K):
  number.append(int(input()))
min = 1
max = max(number)

while min <= max: 
  mid = (max+min)//2
  count = 0
  for i in range(K):
    count += number[i] // mid
  if count >= N:
    min = mid+1
  else:
    max = mid-1

print(max)

  
