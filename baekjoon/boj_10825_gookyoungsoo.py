import sys
sys.stdin = open('input.txt')
N = int(input())
scores = []
for _ in range(N):
    name, k, e, m = input().split()
    scores.append((name, int(k), int(e), int(m)))

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))
for score in scores:
    print(score[0])