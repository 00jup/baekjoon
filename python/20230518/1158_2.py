import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

arr = deque()
arr2 = deque()
for i in range(n):
    arr.append(i+1)

print("<", end="")
while (True):
    for _ in range(k-1):
        tmp = arr.popleft()
        arr.append(tmp)
    if len(arr) == 0:
        break
    # 여기 있으면 len(arr) == 0일 때 while이 한번 더 실행된다. 그러니까 while(True)의 경우 일단 조건을 처음에 적거나 아니면 while(조건식)을 하도록 하자.
    arr2.append(arr.popleft())
print(*arr2, sep=", ", end="")
print(">")
