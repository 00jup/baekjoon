import queue
import sys
input = sys.stdin.readline

que = queue.Queue()

N = int(input())

for _ in range(N):
    ans = input().split()
    if ans[0] == 'push':
        que.put(int(ans[1]))
    # print(ans[0], ans[1]) split을 해야 함.
    elif ans[0] == 'front':
        if len(que) == 0:
            print(-1)
        else:
            print(que[0])
    elif ans[0] == 'size':
        print(que.qsize())
    elif ans[0] == 'pop':
        print(que.get())
    elif ans[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif ans[0] == 'empty':
        if que.empty():
            print(1)
        else:
            print(0)
