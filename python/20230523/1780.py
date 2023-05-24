import sys

input = sys.stdin.readline
N = int(input())

paper = [[]*N for _ in range(N)]
# 이렇게 선언해줘야 되나?

for i in range(N):
    paper[i].append(input().strip().split())
    # paper[i].append(list(input().strip().split()))
# int로 입력받는 방법
# entries = list(map(int, input().split()))

# print(entries)

print(paper[0][1])
print(paper[1])
3