import sys
input = sys.stdin.readline

N = int(input())
queue = []
i = 0
for _ in range(N):
    ans = input().split()
    if ans[0] == 'push':
        queue.append(ans[1])
    elif ans[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif ans[0] == 'size':
        print(len(queue))
    elif ans[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue.pop(0))
    elif ans[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
    elif ans[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
