a, b =map(int, input().split())
#print(a +" "+b)
#a 15 b 10 10 5
#a 9 b 7 
def gcd(a , b):
  if b == 0:
    return a
  # if (a==1 or b==1):
  #   print(1)
  #   return 10
  if a>b:
    return gcd(b, a%b)
  else:
    return gcd(a, b%a)

gcd_num = gcd(a, b)

def lcm(a, b):
  return a*b/gcd_num

print(gcd_num)
print(int(lcm(a,b)))