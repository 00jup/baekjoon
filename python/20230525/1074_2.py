import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())
size = 2**N
count = 0


def recursion(size, x, y):
    global count
    if (x == c and y == r):
        print(int(count))
        return
        # column이 x좌표구나..
    elif (c < x+size and r < y+size and c >= x and r >= y):
        recursion(size/2, x, y)
        recursion(size/2, x+size/2, y)
        recursion(size/2, x, y+size/2)
        recursion(size/2, x+size/2, y+size/2)
    else:
        count += size*size


recursion(size, 0, 0)
