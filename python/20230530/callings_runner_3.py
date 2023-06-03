import sys

input = sys.stdin.readline


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

# https://somjang.tistory.com/entry/Programmers-%EB%8B%AC%EB%A6%AC%EA%B8%B0-%EA%B2%BD%EC%A3%BC-Python-featChatGPT


print(solution(players, callings))
