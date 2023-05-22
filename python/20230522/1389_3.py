import sys

input = sys.stdin.readline
inf = sys.maxsize

n, m = map(int, input().split())
graph = [[inf]*(n+1) for _ in range(n+1)]
# 왜 n+1이지??

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, m+1):
    graph[i][i] = 0

for k in range(1, m+1):
    for i in range(1, m+1):
        for j in range(1, m+1):
            if graph[i][j] > graph[i][k]+graph[k][j]:
                graph[i][j] = graph[i][k]+graph[k][j]
# 옆에 초록 선은 뭐지
sum = [0] * (n+1)
result = inf

for i in range(1, n+1):
    for j in range(1, n+1):
        sum[i] += graph[i][j]


for i in range(1, n+1):
    if result > sum[i] and sum[i] != 0 and sum[i] != result:
        result = sum[i]
        idx = i

print(idx)
