N = int(input())
homeworks = []
for _ in range(N):
    d, p = map(int, input().split())
    homeworks.append((d, p))
max_days = max([i[0] for i in homeworks])
answer = [0]*max_days
homeworks.sort(key=lambda x: -x[1])
for hw in homeworks:
    if not answer[hw[0]-1]:
        answer[hw[0]-1] = hw[1]
    else:
        i = hw[0]-2
        while i >= 0:
            if not answer[i]:
                answer[i] = hw[1]
                break
            else:
                i -= 1
print(sum(answer))