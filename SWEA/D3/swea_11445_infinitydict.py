T = int(input())
for t in range(1, T+1):
    P, Q = input().rstrip(), input().rstrip()
    result = 'Y'
    if len(Q) - len(P) == 1 and P == Q[:-1] and Q[-1] == 'a':
        result = 'N'

    print("#%d %s" % (t, result))
