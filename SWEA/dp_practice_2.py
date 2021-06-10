def DP(r, c):
    if cave[r][c] == '#':
        memo[r][c] = 0
        return
    elif memo[r][c]:
        return memo[r][c]
    elif r < 0 or r > 3 or c < 0 or c > 4:
        return 987654321

    memo[r][c] = min(DP(r-1, c), DP(r+1, c), DP(r, c-1), DP(r, c+1))+1
    return memo[r][c]


cave = []
start_r, start_c = 0, 0
finish_r, finish_c = 0, 0
for r in range(4):
    tmp = input()
    for c in range(len(tmp)):
        if c == 'A':
            start_r, start_c = r, c
        elif c == 'B':
            finish_r, finish_c = r, c
    cave.append(tmp)
memo = [[0]*5 for _ in range(4)]