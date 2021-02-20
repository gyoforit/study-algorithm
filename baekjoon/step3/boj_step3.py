# 210214
# 백준 3단계 - for문
# 2739. 구구단
N = int(input())
for i in range(1, 10):
    print("%d * %d = %d" % (N, i, N*i))

# 10950. A+B - 3
T = int(input())
for t in range(T):
    A, B = map(int, input().split())
    print(A+B)

# 8393. 합
n = int(input())
result = 0
for i in range(1, n+1):
    result += i
print(result)

# 15552. 빠른 A+B
import sys
T = int(sys.stdin.readline())
for t in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)

# 2741. N 찍기
N = int(input())
for i in range(1, N+1):
    print(i)

# 2742. 기찍 N
N = int(input())
for i in range(N, 0, -1):
    print(i)

# 11021. A+B - 7
T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #%d: %d" % (t, A+B))

# 11022. A+B - 8
T = int(input())
for t in range(1, T+1):
    A, B = map(int, input().split())
    print("Case #%d: %d + %d = %d" % (t, A, B, A+B))

# 2438. 별 찍기 - 1
N = int(input())
for i in range(1, N+1):
    print("*"*i)

# 2439. 별 찍기 - 2
N = int(input())
for i in range(1, N+1):
    print(" "*(N-i), end='')
    print("*"*i)

# 10871. X보다 작은 수
N, X = map(int, input().split())
A = list(map(int, input().split()))
result = []
for a in A:
    if a < X:
        result += [a]
result = ' '.join(map(str, result))
print(result)