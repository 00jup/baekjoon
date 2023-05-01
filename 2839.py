import sys
N = int(sys.stdin.readline())

if N%3==0 or (N%5)%3==0:
  if int(N/3) < int(N/5+(N%5)/3) or N==6 :
    print(int(N/3))  
  else:
    print(int(N/5+(N%5)/3))

else:
  print(-1)

print((11%5))