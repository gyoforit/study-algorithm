N = int(input())
people = []
for i in range(N):
    x, y = map(int, input().split())
    people.append((x, y))

result = []
for m, n in people:
    cnt = 0
    # 본인보다 덩치 클 때만 cnt에 1 추가
    for i, j in people:
        if m < i and n < j:
            cnt += 1

    result.append(cnt+1)

print(*result)