import sys
input = sys.stdin.readline
N, M = map(int, input().split())

chessboard = [[] for _ in range(N)]
for _ in range(N):
    for _ in range(M):
        chessboard.append(input().split().strip())

print(chessboard)
