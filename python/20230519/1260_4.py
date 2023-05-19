import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visited_bfs = [0] * (n+1)
visited_dfs = [0] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def bfs(v):
    q = deque()
    q.append(v)
    visited_bfs[v] = 1
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if not visited_bfs[i] and graph[v][i]:
                q.append(i)
                visited_bfs[i] = 1


def dfs(v):
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)


dfs(v)
print()
bfs(v)
