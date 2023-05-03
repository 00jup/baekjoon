import sys
N = int(sys.stdin.readline())
count = 0
while N>=0:
  if(N%5==0):
    count = N / 5
    break
  count += 1
  N -= 3
  
print(count)

