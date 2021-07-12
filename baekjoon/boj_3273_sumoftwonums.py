# 투포인터 문제
# 투포인터는 반드시 정렬이 되어있어야 함
# 조건을 만족하면 양쪽 다 한칸씩 이동
# 왼쪽->오른쪽: 수 증가, 오른쪽->왼쪽: 수 감소 이므로
# 더한 값이 x보다 클 때/작을 때를 나누어서 처리
N = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
left, right = 0, N-1
cnt = 0
while left < right:
    tmp = nums[left] + nums[right]
    if tmp == x:
        cnt += 1
        left += 1
        right -= 1
    elif tmp > x:
        right -= 1
    elif tmp < x:
        left += 1
print(cnt)