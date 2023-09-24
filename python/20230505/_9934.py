import sys
input = sys.stdin.readline
N = int(input())
b = [] #이중 배열 선언하기


b = input().strip().split(' ')

def inorderTraveral(root):
  inorderTraveral(root)