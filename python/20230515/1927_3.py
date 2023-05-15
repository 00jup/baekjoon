import sys
import heapq
input = sys.stdin.readline
heap = []
N = int(input()) 

num = int(input())
heapq.heappush(heap, num)
if heapq.heappop(heap) == 0: ########### 0이 아니라도 pop 해버림.
  print(0)

for _ in range(N-1):
  num = int(input())
  if num == 0:
    if len(heap)==0:
      print(0)
    else:
      print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, num)