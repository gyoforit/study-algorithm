# if와 elif 주의하자!
# 이 문제에서는 r, c / r, c+1 둘다 반드시 확인해야하므로 if-if로 써야 함
# target = (0, 0)에 와야 할 문자 = B라고 가정
def search(x, y, target):
    cnt = 0
    for r in range(x, x+8):
        for c in range(y, y+8, 2):
            print(r, c)
            print(r, c+1)
            if r % 2: # 홀수행 (0열=W이어야 함)
                if board[r][c] == target:
                    cnt += 1
                if board[r][c+1] != target:
                    cnt += 1
            else: # 짝수행 (0열=B이어야 함)
                if board[r][c] != target:
                    cnt += 1
                if board[r][c+1] == target:
                    cnt += 1
    return cnt

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())
answer = 987654321
# 왼쪽 모서리 좌표
for r in range(0, N-8+1):
    for c in range(0, M-8+1):
        search(r, c, 'B')
        # print('end')
        tmp = min(search(r, c, 'B'), search(r, c, 'W'))
        answer = min(answer, tmp)
print(answer)

