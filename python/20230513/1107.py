import sys
input = sys.stdin.readline

ten = 10
N = input()
M = int(input())
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = []
print(num)
a.append(input().split())
for i in range(M):
    for j in range(ten):
        if a[i] == num[j]:
            num.pop()
            ten -= 1


print(num)
