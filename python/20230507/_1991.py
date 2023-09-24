# def preorderTraveral(root):
#   if root != NULL:
#     print()
#     preorderTraveral(root)
#     preorderTraveral(root)

# def postorderTraveral(root):
#   if root != NULL:
#     preorderTraveral(root)
#     preorderTraveral(root)
#     print()

# def inorderTraveral(root):
#   if root != NULL:
#     preorderTraveral(root)
#     print()
#     preorderTraveral(root)

import sys
input = sys.stdin.readline
N = int(input())

tree = [[0 for i in range(3)] for j in range(N)]
print(tree)

for i in range(N):  
  for j in range(3):
    tree[i][j] = input().strip()

print(tree)
