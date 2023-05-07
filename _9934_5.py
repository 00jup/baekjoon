import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().strip().split(' ')))

tree =[[] for _ in range(N)]
len = len(num)

#값을 바꾸려는 게 아니라 append를 하면 붙여나갈 수 있다.
def inorderReverse(depth, len):
  if depth == N:
    return 
  mid = len // 2
  tree[depth].append(num[mid])

  inorderReverse(depth + 1, mid//2)
  inorderReverse(depth + 1, mid+len//2)


inorderReverse(0, len)
for i in tree:
  print(*i)

# print(tree)
