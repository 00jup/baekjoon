import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

deq = deque()
for i in range(n):
    deq.append(i)

while (True):
    if arr.q == 0:
        break
    for _ in range(k):
        tmp = deq.pop()
        deq.pop()
        deq.append(tmp)
    print(deq.pop)
