import sys
input = sys.stdin.readline
N = int(input())
num = list(map(int,input().strip().split(' ')))

#tree = [[0 for i in range(3)] for j in range(N)]
tree =[[] for _ in range(N)]
print(num)
print(tree)
#값을 바꾸려는 게 아니라 append를 하면 붙여나갈 수 있다.
# def inorderReverse(depth, start, end):
#   if end > N:
#     return 0
#   if depth == start:
#     tree[end][0] = b[depth]
#   mid = (1+end)//2
  
#   if (mid < 0 or mid >= N):
#     return
#   tree[end][0] = b[mid]
#   inorderReverse(depth, m-1, end+1)
#   inorderReverse(m + 1, start, end+1)
  

# print(tree)
