import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().strip().split(' ')))

tree =[[] for _ in range(N)]
len = len(num)

#값을 바꾸려는 게 아니라 append를 하면 붙여나갈 수 있다.
def inorderReverse(depth, start, end):
  if depth == N:
    return
  mid = (start + end) // 2
  tree[depth].append(num[mid])

  inorderReverse(depth + 1, start, mid)
  inorderReverse(depth + 1, mid + 1, end)


inorderReverse(0, 0, len)
for i in tree:
  print(*i)

# print(tree)
