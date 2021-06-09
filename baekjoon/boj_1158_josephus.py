N, K = map(int, input().split())
people = list(range(1, N+1))
result = []
now = 0
while people:
    now = (now+K-1)%(len(people))
    target = people.pop(now)
    result.append(target)

print('<'+', '.join(map(str, result))+'>')