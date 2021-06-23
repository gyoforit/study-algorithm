# 어렵게 생각하지 말고 그대로 구현하기!
drc = [(1, 0), (0, 1), (-1, -1)]

def solution(n):
    grid = [[0]*i for i in range(1, n+1)]
    num = 1
    r, c = -1, 0
    idx = 0
    cnt = n
    while cnt > 0:
        for _ in range(cnt):
            r, c = r+drc[idx%3][0], c+drc[idx%3][1]
            grid[r][c] = num
            num += 1
        idx += 1
        cnt -= 1
    answer = sum(grid, [])
    return answer