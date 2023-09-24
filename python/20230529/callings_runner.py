import sys

input = sys.stdin.readline

players = []
callings = []

players = input().split()
callings = input().split()


def solution(players, callings):

    for j in range(len(callings)):
        for i in range(len(players)):
            if players[i] == callings[j]:
                tmp = players[i-1]
                players[i-1] = players[i]
                players[i] = tmp

    return players


print(solution(players, callings))
