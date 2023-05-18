import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

arr = deque()
arr2 = deque()
for i in range(n):
    arr.append(i+1)

print("<", end="")
while (len(arr)>0):
    for _ in range(k-1):
        tmp = arr.popleft()
        arr.append(tmp)
    arr2.append(arr.popleft())
print(*arr2, sep=", ", end="")
print(">")
