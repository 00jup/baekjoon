import sys
input = sys.stdin.readline
N = int(input().strip())
tree = {}

for n in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]
# print(tree[0][])
# print(tree['A'][0])
# print(tree['A'][1])

print(tree)


def inorderTraversal(root):
    if root != '.':
        inorderTraversal(tree[root][0])
        print(root, end="")
        inorderTraversal(tree[root][1])


def postorderTraversal(root):
    if root != '.':
        postorderTraversal(tree[root][0])
        postorderTraversal(tree[root][1])
        print(root, end="")


def preorderTraversal(root):
    if root != '.':
        print(root, end="")
        preorderTraversal(tree[root][0])
        preorderTraversal(tree[root][1])


preorderTraversal('0')
print('')
inorderTraversal('0')
print('')
postorderTraversal('0')
