import queue
import sys
input = sys.stdin.readline

que = queue.Queue()

N = int(input())

for _ in range(N):
    ans = input()
    if ans[0] == 'push':
        que.put(int(ans[1]))
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
        print(que.empty())
