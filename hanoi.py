def hanoi(n, a, b, c):
    if n>=1:

        hanoi(n-1, a, c, b)
        print(a, c)
        hanoi(n-1, b, a, c)


number = int(input())
print((2**number-1))
hanoi(number, '1', '2', '3');

