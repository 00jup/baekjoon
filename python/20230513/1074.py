import sys
input = sys.stdin.readline

N, row, col = map(int, input().split())
count = 0
# N=3 --> 8


def search(num, r, c):
    global count
    if num == 0:
        return
    if 2**num/2 < r:
        if 2**num/2 < c:
            count += 3*(2**(num-1))
            search(num-1, r, c)

        elif 2**num/2 > c:
            count += 2*(2**(num-1))
            search(num-1, r, c)

    elif 2**num/2 > r:
        if 2**num/2 < c:
            count += (2**(num-1))
            search(num-1, r, c)

        elif 2**num/2 > c:
            search(num-1, r, c)


search(N, row, col)
print(count)
