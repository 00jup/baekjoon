import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().strip().split(' ')))

tree =[[] for _ in range(N)]
midnum = N // 2
i = 0
#값을 바꾸려는 게 아니라 append를 하면 붙여나갈 수 있다.
def inorderReverse(depth, mid):
  if depth == N:
    return
  tree[depth].append(num[mid])
  if (mid < 0 or mid >= N):
    return
  inorderReverse(depth + 1, (mid+N+1)//2)
  inorderReverse(depth + 1, mid//2)


inorderReverse(0, midnum)
print(tree)
# print(tree)
