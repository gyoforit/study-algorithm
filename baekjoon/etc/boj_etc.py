# 백준 기타문제
# 210220
# 2167. 2차원 배열의 합
# python3으로 돌리면 시간초과, pypy3으로 돌려야 통과
# 나중에 동적계획법 배워서 다시 풀어보기
N, M = map(int, input().split())
arr = []
for n in range(N):
    arr.append(list(map(int, input().split())))
K = int(input())
for k in range(K):
    r1, c1, r2, c2 = map(int, input().split())
    result = 0
    for r in range(r1-1, r2):
        for c in range(c1-1, c2):
            result += arr[r][c]
    print(result)

# 210222
# 2527. 직사각형
for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    result = 'a'
    if p1 < x2 or q2 < y1 or q1 < y2 or p2 < x1:
        result = 'd'
    elif p1 == x2:
        if q1 == y2 or y1 == q2:
            result = 'c'
        else:
            result = 'b'
    elif y1 == q2:
        if p1 == x2 or x1 == p2:
            result = 'c'
        else:
            result = 'b'
    elif x1 == p2:
        if y1 == q2 or q1 == y2:
            result = 'c'
        else:
            result = 'b'
    elif y2 == q1:
        if x1 == p2 or p1 == x2:
            result = 'c'
        else:
            result = 'b'

    print(result)

# 210307 - 별찍기 시리즈
# 2440. 별찍기 - 3
N = int(input())
for i in range(N, 0, -1):
    print("*"*i)

# 2441. 별찍기 - 4
N = int(input())
for i in range(N, 0, -1):
    print((' '*(N-i))+'*'*(i))

# 2442. 별찍기 - 5
N = int(input())
for i in range(1, N+1):
    print((' '*(N-i))+('*'*(2*i-1)))

# 2443. 별찍기 - 6
N = int(input())
for i in range(N, 0, -1):
    print((' '*(N-i))+('*'*(2*i-1)))

# 2444. 별찍기 - 7
N = int(input())
for i in range(1, 2*N):
    if i <= N:
        print((' '*(N-i))+('*'*(2*i-1)))
    else: # 6, 7, 8, 9
        # tmp = abs(N-i) # i-N
        # print((' '*(i-N))+('*'*(2*(N-tmp)-1)))
        print((' ' * (i-N)) + ('*'*(2*(2*N-i)-1)))

# 2445. 별찍기 - 8
N = int(input())
for i in range(1, 2*N):
    x = abs(N-i)
    print(('*'*(N-x))+(' '*(2*x))+('*'*(N-x)))

# 2446. 별찍기 - 9
N = int(input())
for i in range(1,2*N):
    x = abs(N-i)
    print((' '*(N-x-1))+('*'*(2*x+1)))

# 210327
# 11399. ATM
# DFS재귀로 풀면 시간 초과
def DFS(idx, S, total):
    global mn
    if total >= mn:
        return

    if idx == N:
        if total < mn:
            mn = total
            return

    for i in range(N):
        if check[i] == 0:
            NS = S+pp[i]
            Ntotal = total+NS
            check[i] = 1
            DFS(idx+1, NS, Ntotal)
            check[i] = 0

N = int(input())
pp = list(map(int, input().split()))
check = [0]*N
mn = 987654321
DFS(0, 0, 0)
print(mn)

# 그리디로 풀면 통과!
N = int(input())
pp = list(map(int, input().split()))
pp.sort()
total = 0
for i in range(N):
    tmp = sum(pp[:i+1])
    total += tmp
print(total)

# 16953: A -> B
def calc(A, B):
    X = B
    cnt = 0
    while A != X:
        if X < A:
            return -1
        if X % 2:
            NX = str(X)
            if NX[-1] == '1':
                X = int(NX[:-1])
            else:
                return -1
        else:
            X //= 2
        cnt += 1
        # print(A, X)
    return cnt+1

A, B = map(int, input().split())
print(calc(A, B))

# 12907. 동물원
def zoo(N, data):
    if max(data) >= N:
        return 0
    else:
        X = max(data) + 1
        Y = N-X
        for i in range(0, X):
            if Y != 0:
                if i <= Y - 1:
                    if data.count(i) != 2:
                        return 0
                else:
                    if data.count(i) != 1:
                        return 0
            else:
                if data.count(i) != 1:
                    return 0
        if X != Y:
            return (2**Y)*2
        else:
            return 2**Y

N = int(input())
data = list(map(int, input().split()))
print(zoo(N, data))

# 210328
# 12871. 무한 문자열
s = input()
t = input()
if len(s) > len(t):
    s, t = t, s
ls = len(s)
lt = len(t)
ns = s * (100//ls) + s[:100%ls]
nt = t * (100//lt) + t[:100%lt]
result = 1 if ns == nt else 0
print(result)