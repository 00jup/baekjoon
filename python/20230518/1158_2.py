import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

arr = deque()
arr2 = deque()
for i in range(n):
    arr.append(i+1)

print("<", end="")
while ():
    for _ in range(k-1):
        tmp = arr.popleft()
        arr.append(tmp)
    if len(arr) == 0:
        break
    arr2.append(arr.popleft())
print(*arr2, sep=", ", end="")
print(">")
