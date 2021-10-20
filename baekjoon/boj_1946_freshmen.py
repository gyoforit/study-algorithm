import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    people = []
    for _ in range(N):
        a, b = map(int, input().split())
        people.append((a, b))
    people.sort()
    cnt = 1
    max_point = people[0][1]
    for i in range(1, N):
        if max_point > people[i][1]:
            cnt += 1
            max_point = people[i][1]
    print(cnt)