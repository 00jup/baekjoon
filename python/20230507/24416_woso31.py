f=[0]*50
f[1]=f[2]=1
n=int(input())

def fib(n):
    for i in range(3, n+1):
        f[i] = f[i-1]+f[i-2]
    return f[n]

cnt1=fib(n)
cnt2= n-2
print(cnt1, cnt2)