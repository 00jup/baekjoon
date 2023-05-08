import sys
input = sys.stdin.readline
N = int(input())
b = input().strip().split(' ')
tree = {}

for i in range(N):
  root, left, right = [i, 0, 0]
  tree[root]=[left, right]
  i += 1

i = 0

def inorderTraveral(root):
  inorderTraveral(tree[root][0])
  tree[b[i]] = tree[root]
  del tree[root]
  i += 1
  inorderTraveral(tree[root][1])

inorderTraveral(0)

print(tree)