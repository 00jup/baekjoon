import sys

input = sys.stdin.readline

players = []
callings = []

players = input().split()
callings = input().split()


def solution(players, callings):
    player_result = {player: index for index, player in enumerate(players)}
    index_result = {index: player for index, player in enumerate(players)}

    for call in callings:
        rank = player_result[call]
        player_result[index_result[rank - 1]], player_result[index_result[rank]
                                                             ] = player_result[index_result[rank]], player_result[index_result[rank-1]]
        index_result[rank -
                     1], index_result[rank] = index_result[rank], index_result[rank-1]

    return list(index_result.values())


print(solution(players, callings))
