import sys

input = sys.stdin.readline

players = []
callings = []

players = input().split()
callings = input().split()


def solution(players, callings):
    answer = []

    for j in range(len(callings)):
        for i in range(len(players)):
            if players[i] == callings[j]:
                tmp = players[i-1]
                players[i-1] = players[i]
                players[i] = tmp

    answer = players

    return answer


print(solution(players, callings))
