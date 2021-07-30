def solution(n,a,b):
    cnt = 1
    while True:
        if abs(a-b) == 1:
            # 둘 중 큰 수가 짝수일 때 => 같은 그룹이므로 끝
            if not max(a, b) % 2:
                break
        cnt += 1
        if a % 2:
            a += 1
        a //= 2
        if b % 2:
            b += 1
        b //= 2
    return cnt


print(solution(8, 1, 2))
print(solution(8, 2, 3))
print(solution(8, 4, 7))