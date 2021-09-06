# 테케 3은 틀리는데 제출하면 통과하는 기묘한 코드..
def change_key(key, M):
    new_key = [[0] * M for _ in range(M)]
    for r in range(M):
        for c in range(M):
            new_key[r][c] = key[M-c-1][r]
    return new_key

def is_possible(key, lock, sr, sc):
    M, N = len(key[0]), len(lock[0])
    cnt = 0
    for r in range(M):
        for c in range(M):
            nr, nc = sr + r, sc + c
            if 0 <= nr < N and 0 <= nc < N:
                if key[r][c] and lock[nr][nc]:
                    return False
                elif key[r][c] and not lock[nr][nc]:
                    cnt += 1
    cnt_0 = sum([l.count(0) for l in lock])
    if cnt == cnt_0:
        return True
    return False

def solution(key, lock):
    M, N = len(key[0]), len(lock[0])
    # 아예 열려있는 경우
    if not sum([l.count(0) for l in lock]):
        return True

    for _ in range(4):
        for r in range(-(M - 1), N):
            for c in range(-(M - 1), N):
                result = is_possible(key, lock, r, c)
                if result:
                    return True
        key = change_key(key, M)
    return False