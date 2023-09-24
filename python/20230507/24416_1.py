import sys
input = sys.stdin.readline

N = int(input())

count = 0
def fib(n):
  global count
  if n == 1 or n==2:
    count += 1
    return 0
  else:
    return fib(n-1) + fib(n-2)
fib(N)
print(count, N-2)
