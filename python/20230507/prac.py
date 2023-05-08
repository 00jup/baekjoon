tree = [1]
tree1 = ['1']

print(tree)
print(tree1)
import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().strip().split(' ')))

tree =[[] for _ in range(N)]
#len = len(num)

#값을 바꾸려는 게 아니라 append를 하면 붙여나갈 수 있다.
def inorderReverse(depth, arr):
  if depth == N:
    return
  mid = len(arr) // 2
  tree[depth].append(arr[mid])

  inorderReverse(depth + 1, arr[:mid])
  inorderReverse(depth + 1, arr[mid+1:])


print(num[:0])
print(num[:1])
print(num[:2])
print(num[:2])
print(num[0:])