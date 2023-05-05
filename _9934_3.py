import sys
input = sys.stdin.readline
N = int(input())
b = input().strip().split(' ')

tree = [[0 for i in range(3)] for j in range(N)]

def inorderReverse(depth, start, end):
  if end > N:
    return 0;
  if depth == start:
    tree[end][0] = b[depth]
  mid = (1+end)//2
  
  if (mid < 0 or mid >= N):
    return;
  tree[end][0] = b[mid]
  inorderReverse(depth, m-1, end+1)
  inorderReverse(m + 1, start, end+1)
  

print(tree)
