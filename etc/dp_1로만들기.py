X = int(input())
# 해당 인덱스값이 되려면 해야하는 연산의 최솟값을 담을 리스트
D = [0]*30001

for x in range(2, X+1):
    # 기본적으로는 x에서 1을 뺀 x-1의 연산횟수 + 1
    D[x] = D[x-1]+1
    # 특정 수로 나누어떨어질 경우 최솟값 비교
    if x % 2 == 0:
        D[x] = min(D[x], D[x//2]+1)
    elif x % 3 == 0:
        D[x] = min(D[x], D[x//3]+1)
    elif x % 5 == 0:
        D[x] = min(D[x], D[x//5]+1)

print(D[X])