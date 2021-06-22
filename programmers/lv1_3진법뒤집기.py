def solution(n):
    tmp = ''
    while n > 0:
        tmp = str(n%3) + tmp
        n //= 3
    answer = sum([int(tmp[t])*(3**t) for t in range(len(tmp))])
    return answer