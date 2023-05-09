import sys
input = sys.stdin.readline

N = int(input())
stack = []


for i in range(N):
    command, number = input().strip().split()
    print(command, i)
    if command == "push":
        number = int(input())
        stack.append(number)
        print(number, "11111")


print(stack)
