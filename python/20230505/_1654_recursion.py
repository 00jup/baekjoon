import sys
input = sys.stdin.readline
K, N = map(int, input().split())
number = []

for _ in range(K):
  number.append(int(input()))
max = max(number)

def counting_binary(n):
  count = 0
  for item in number:
    count += item // n
  return count

def recursion(min, max, N):
  if min>max:
    return max
  mid = (max+min)//2
  count = counting_binary(mid)
  if count>=N:
    return recursion(mid+1, max, N)
  else:
    return recursion(min, mid-1, N)

print(recursion(1, max, N))

