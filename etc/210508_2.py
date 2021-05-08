drc1 = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
drc2 = [(-2, 0), (2, 0), (0, 2), (0, -2)]
drc3 = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def check(r, c, arr):
    for dr, dc in drc1:
        nr, nc = r+dr, c+dc
        if 0<=nr<5 and 0<=nc<5:
            if arr[nr][nc] == 'P':
                if arr[r+dr][c] != 'X' or arr[r][c+dc] != 'X':
                    return False

    for dr, dc in drc2:
        nr, nc = r+dr, c+dc
        if 0<=nr<5 and 0<=nc<5:
            if arr[nr][nc] == 'P':
                tmp = ('r', dr) if dr else ('c', dc)
                if tmp[0] == 'r':
                    chk = arr[r+1][c] if tmp[1] > 0 else arr[r-1][c]
                elif tmp[0] == 'c':
                    chk = arr[r][c+1] if tmp[1] > 0 else arr[r][c-1]
                if chk != 'X':
                    return False

    for dr, dc in drc3:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 5 and 0 <= nc < 5:
            if arr[nr][nc] == 'P':
                return False

    return True

def solution(places):
    answer = []
    for place in places:
        flag = 0
        for r in range(5):
            if flag: break
            for c in range(5):
                if place[r][c] == 'P':
                    if not check(r, c, place):
                        answer.append(0)
                        flag = 1
                        break
        if not flag:
            answer.append(1)

    return answer