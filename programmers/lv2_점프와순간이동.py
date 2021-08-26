# N = 10억일 때 시간초과가 나진 않을지..?
def solution(n):
    ans = 1
    while n > 1:
        if n%2:
            ans += 1
            n -= 1
        n //= 2
    return ans