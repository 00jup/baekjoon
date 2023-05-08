def fibo(n):
    cache = [-1 for _ in range(n+1)]
    if n==-1:
      return 1
    def iterate(n):
# 기저사례 1.
      if n < 2:
        return n

	# 기저사례 2.
      if cache[n] != -1:
        return cache[n]

	# 기저사례 충족 못할 시 값을 실제로 구함
      cache[n] = iterate(n-1) + iterate(n-2)
      return cache[n]
    return iterate(n)
    
import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
  num = int(input())
  print(fibo(num-1), fibo(num))
  