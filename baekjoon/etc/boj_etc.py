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