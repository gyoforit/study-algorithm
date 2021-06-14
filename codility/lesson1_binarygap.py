def solution(N):
    zero_list = bin(N)[2:].rstrip('0').split('1')
    max_length = 0
    for z in zero_list:
        if len(z) > max_length:
            max_length = len(z)
    return max_length