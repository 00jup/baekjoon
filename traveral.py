import sys
input = sys.stdin.readline
N = int(input().strip())
tree = {}

for n in range(N):
  root, left, right = input().strip().split()
  tree[root] = [left, right]
#pXPrint(tree[0][])
print(tree['A'][0])
print(tree['A'][1])


def inorderTraveral(root):
  if root != '.':
    inorderTraveral(tree[root][0])
    print(root, end="")
    inorderTraveral(tree[root][1])

def postorderTraveral(root):
  if root != '.':
    postorderTraveral(tree[root][0])
    postorderTraveral(tree[root][1])
    print(root, end="")
    
def preorderTraveral(root):
  if root != '.':
    print(root, end="")
    preorderTraveral(tree[root][0])
    preorderTraveral(tree[root][1])

preorderTraveral('A')
print('')
inorderTraveral('A')
print('')
postorderTraveral('A')