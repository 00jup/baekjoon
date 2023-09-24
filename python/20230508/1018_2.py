import sys
input = sys.stdin.readline
N, M = map(int, input().split())

chessboard = []
for _ in range(N):
    chessboard.append(input().strip())


whBoard = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"]
blBoard = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"]


def whBoard_check(k, l):
    count = 0
    for x in range(N):
        for y in range(M):
            if chessboard[x+k][y+l] != whBoard[x][y]:
                count += 1
    return count


def blBoard_check(k, l):
    count = 0
    for x in range(8):
        for y in range(8):
            if chessboard[x+k][y+l] != blBoard[x][y]:
                count += 1
    return count


def solution():
    for k in range(N-8):
        for l in range(M-8):
            A = whBoard_check(k, l)
            B = blBoard_check(k, l)
            if A < B:
                tmp = A
            else:
                tmp = B

        if result >= tmp:
            result = tmp
    print(result)


solution()
