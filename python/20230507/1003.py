import sys

input = sys.stdin.readline

N = int(input())
def count_fibo(case, sum):
  global count1
  global count0
  if case == 1:
    count1 +=1
    return 1
  elif case == 0:
    count0 +=1
    return 0
  elif sum > 0: 
    return sum
  else:
    sum = count_fibo(case-1)+count_fibo(case-2)
    return sum


for _ in range(N):
  num = int(input())
  sum = 0
  count1=0
  count0=0
  count_fibo(num, sum)
  print(count0, count1)