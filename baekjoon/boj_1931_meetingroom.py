'''
SWEA에서 풀었던 것 보다 더 까다로운 조건
예를 들어 5 7/ 7 7/ 7 7 이 나오면 7 7 때문에 5 7이 못 들어갈 수 있음
따라서 끝나는시간 순으로 오름차순 정렬 후 시작시간 순으로 다시 오름차순 해야 함!
'''
N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort(key=lambda x: (x[1], x[0]))
cnt, now = 0, 0
ans = []
# 가장 최근 종료시각보다 시작 시각이 <= 이면 추가
for start, end in times:
    if now <= start:
        cnt += 1
        ans.append((start, end))
        now = end
print(cnt)


