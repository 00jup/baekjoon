import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    arr.append(input().strip())

arr.sort()

for i in arr:
    print(*i)
