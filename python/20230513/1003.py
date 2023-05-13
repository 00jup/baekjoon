import sys
input = sys.stdin.readline

T = int(input())
fibo = []


def fib(n):
    if n == 0:
        fibo[0] += 1
        return
    elif n == 1:
        fibo[1] += 1
        return
    else:
        return fib(n-1) + fib(n-2)


for _ in range(T):
    fibo[0] = 0
    fibo[1] = 0
    num = int(input())
    fib(num)
    print(fibo[0]+fibo[1])
