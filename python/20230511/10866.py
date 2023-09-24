from collections import deque
import sys

input = sys.stdin.readline

deq = deque()
N = int(input())

for _ in range(N):
    ans = input().split()
    if ans[0] == 'push_front':
        deq.appendleft(ans[1])
    elif ans[0] == 'push_back':
        deq.append(ans[1])
    elif ans[0] == 'pop_front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.popleft())
    elif ans[0] == 'pop_back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq.pop())
    elif ans[0] == 'size':
        print(len(deq))
    elif ans[0] == 'empty':
        if len(deq) == 0:
            print(1)
        else:
            print(0)
    elif ans[0] == 'front':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[0])
    elif ans[0] == 'back':
        if len(deq) == 0:
            print(-1)
        else:
            print(deq[-1])
