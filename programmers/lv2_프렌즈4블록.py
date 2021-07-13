def solution(m, n, board):
    answer = 0
    changed = [list() for _ in range(n)]
    # 밑으로 떨어뜨리는거 -> 오른쪽으로 미는걸로 바꾸기 위해 배열 회전
    for r in range(m):
        for c in range(n-1, -1, -1):
            changed[n-1-c].append(board[r][c])

    while True:
        check = []
        # 같은 알파벳인 좌표들 check에 넣기
        for r in range(0, n-1):
            for c in range(0, m-1):
                if changed[r][c] != '0' and changed[r][c] == changed[r+1][c] == changed[r][c+1] == changed[r+1][c+1]:
                    check.append((r, c))
                    check.append((r+1, c))
                    check.append((r, c+1))
                    check.append((r+1, c+1))
        if check:
            # 중복 제거
            check = list(set(check))
            answer += len(check)
            # 없애기
            for x, y in check:
                changed[x][y] = ''
            # new_board에 지우고 왼쪽을 0으로 채운 배열 다시 만들기
            new_board = [list() for _ in range(n)]
            for r in range(n):
                changed[r] = ''.join(changed[r]).zfill(m)
                new_board[r].extend(changed[r])
            changed = new_board
        # 더 이상 바꿀게 없으면 탈출
        else:
            break
    return answer


solution(4, 5, ["CCBDE", "AAADE", "AAABF", "CCBBF"])