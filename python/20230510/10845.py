from queue import Queue ##이거 차이는 뭐지
import sys
input = sys.stdin.readline

que = Queue()

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
        print(len(que))
    elif ans[0] == 'pop':
        print(que.get())
    elif ans[0] == 'back':
        if len(que) == 0:
            print(-1)
        else:
            print(que[-1])
    elif ans[0] == 'empty':
        if len(que) == 0:
            print(1)
        else:
            print(0)
