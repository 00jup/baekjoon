import sys

input = sys.stdin.readline

N = int(input())
#a = [list(map(int, input().split())) for _ in range(N)]

def count_fibo(case):
  global count1
  global count0
  if case == 1:
    count1 +=1
    return 1
  elif case == 0:
    count0 +=1
    return 0
  else:
    return count_fibo(case-1)+count_fibo(case-2)


for _ in range(N):
  num = int(input())
  count1=0
  count0=0
  count_fibo(num)
  print(count0, count1)