# 확장 유클리드 정리
def euclid(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    return [x, y]

T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())
    print("#%d %s" % (t, ' '.join(map(str, euclid(A, B)))))