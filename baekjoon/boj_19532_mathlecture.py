# -999~999 면 1999*1999=3,996,001 이므로 완전탐색 가능
a, b, c, d, e, f = map(int, input().split())
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x+b*y == c and d*x+e*y == f:
            print(x, y)