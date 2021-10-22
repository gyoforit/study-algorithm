from itertools import permutations
n = int(input())
k = int(input())
cards = []
answer = set()
for _ in range(n):
    cards.append(input())
pers = list(map(list, list(permutations(cards, k))))
for p in pers:
    p = int(''.join(p))
    answer.add(p)

print(len(answer))