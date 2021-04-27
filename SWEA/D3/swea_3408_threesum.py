T = int(input())
for t in range(1, T+1):
    N = int(input())
    S1 = N*(N+1)//2
    S2 = N**2
    S3 = N*(N+1)
    print("#%d %d %d %d" % (t, S1, S2, S3))