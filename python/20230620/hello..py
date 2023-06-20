import sys
input = sys.stdin.readline
N = int(input().strip())
tree = {}

for n in range(N):
    root, left, right = input().strip().split()
    tree[root] = [left, right]

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


# 입력할 때 . 이 포함되어 있어야 함.
# ##ex
# 0 1 2
# 1 3 4
# 2 5 6
# 3 . .
# 4 . .
# 5 . .
# 6 . .
# . 이 없으면 언제 끝날지 모르기 때문이다.
