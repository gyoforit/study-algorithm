import sys
input = sys.stdin.readline

N, M = map(int, input().split())
case_a = set()
case_b = set()
for _ in range(N):
    case_a.add(input().strip())
for _ in range(M):
    case_b.add(input().strip())

answer = sorted(list(case_a&case_b))
print(len(answer))
for ans in answer:
    print(ans)