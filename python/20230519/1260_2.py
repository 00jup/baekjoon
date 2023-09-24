from collections import deque
import sys

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited_dfs = [0]*(n+1)


def dfs(v):
    visited_dfs[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if not visited_dfs[i] and graph[v][i]:
            dfs(i)


print()
dfs(v)
