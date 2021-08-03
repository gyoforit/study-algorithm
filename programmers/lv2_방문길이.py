dir_dict = {
    'U': (-1, 0),
    'D': (1, 0),
    'R': (0, 1),
    'L': (0, -1)
}

def solution(dirs):
    roads = set()
    r, c = 0, 0
    for dir in dirs:
        dr, dc = dir_dict[dir]
        nr, nc = r+dr, c+dc
        if -5<=nr<=5 and -5<=nc<=5:
            # 방문한 적 없을 때만 add. 좌표 순서 바꾼 것도 확인해야 함!
            if (r, c, nr, nc) not in roads and (nr, nc, r, c) not in roads:
                roads.add((r, c, nr, nc))
            r = nr
            c = nc
    return len(roads)