import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
count = 0


def recursion(n, x, y):
    if n == 0:
        return 0
    half = 2**(n-1)
    if (r < half and c < half):
        return recursion(n-1, x, y)
    elif (r < half and c >= half):
        return half*half + recursion(n-1, x, y-half)
    elif (r >= half and c < half):
        return 2*half*half + recursion(n-1, x-half, y)
    else:
        return 3*half*half + recursion(n-1, x-half, y-half)


print(recursion(N, r, c))
