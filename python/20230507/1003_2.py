import sys
input = sys.stdin.readline
N = int(input())
#a = [list(map(int, input().split())) for _ in range(N)]

def count_fibo(n):
  global count1
  global count0
  if n == 0:
    count0 += 1
    return
  elif n == 1:
    count1 += 1
    return
  else:
    while n>=2:
      if n-1 == 0:
        count0 += 1
      if n-2 == 0:
        count0 += 1
      if n-1 == 1:
        count1 += 1
      if n-2 == 1:
        count1 += 1
      n-=1



for _ in range(N):
  num = int(input())
  count1=0
  count0=0
  count_fibo(num)
  print(count0, count1)