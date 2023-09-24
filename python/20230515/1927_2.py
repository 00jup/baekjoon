import sys
import heapq
input = sys.stdin.readline
heap = []
N = int(input()) 

num = int(input())
heapq.heappush(heap, num)

for _ in range(N-1):
  num = int(input())
  if num == 0:
    if len(heap)==0:
      print()
      break
    print(heap)
    print(heapq.heappop(heap))
  else:
    heapq.heappush(heap, num)