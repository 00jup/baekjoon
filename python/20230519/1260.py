import sys
from collections import deque


def dfs(v):
    visited_dfs[v] = 1
    print(graph[v][0])
    for i in range(1, n+1):
        if not visited_dfs[i]:
            dfs(i)
# if visited_dfs[v] != 1:
#     dfs


n, m, v = map(int, input().split())

graph = [[0] * 2 for _ in range(1, m+1)]
visited_dfs = [0] * m
for i in range(1, m+1):
    a, b = map(int, input().split())
    graph[i][0] = a
    graph[i][1] = b

for i in range(m):
    visited_dfs[i] = 0
print(graph)
print(visited_dfs)

dfs(v)
