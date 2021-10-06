import sys
sys.stdin = open('input.txt')
from itertools import combinations
N, M = map(int, input().split())
cards = list(map(int, input().split()))
combs = list(combinations(cards, 3))
answer = 0
for comb in combs:
    tmp = sum(comb)
    if tmp <= M:
        answer = max(answer, tmp)

print(answer)