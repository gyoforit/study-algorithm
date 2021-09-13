import sys
sys.stdin = open('input.txt')

def quadtree(array, sr, sc, N):
    global ans
    flag = array[sr][sc]
    for r in range(sr, sr+N):
        for c in range(sc, sc+N):
            if array[r][c] != array[sr][sc]:
                flag = -1
                break
        if flag == -1:
            break

    if flag == -1:
        ans += '('
        quadtree(array, sr, sc, N//2)
        quadtree(array, sr, sc+N//2, N//2)
        quadtree(array, sr+N//2, sc, N//2)
        quadtree(array, sr+N//2, sc+N//2, N//2)
        ans += ')'

    else:
        ans += array[sr][sc]
        return


N = int(input())
grid = [list(input()) for _ in range(N)]
ans = ''
quadtree(grid, 0, 0, N)
print(ans)