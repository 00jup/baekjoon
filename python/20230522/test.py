import sys

input = sys.stdin.readline
inf = sys.maxsize

n = 4
graph = [[inf]*(n+1) for _ in range(n+1)]
# 왜 n+1이지??

for _ in range(4):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in graph:
    print(i)
