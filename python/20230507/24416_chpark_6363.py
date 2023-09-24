n=int(input())
def fib(n):
    f=[0,1,1]
    for i in range(3, n+1):
        ff=f[i-1]+f[i-2]
        f.append(ff)
    return f[n]
print(fib(n), n-2)