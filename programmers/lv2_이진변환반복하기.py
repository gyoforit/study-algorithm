def solution(s):
    answer = []
    cnt, zeros = 0, 0
    while s != '1':
        cnt += 1
        new_s = s.replace('0', '')
        zeros += len(s)-len(new_s)
        s = bin(len(new_s))[2:]
    answer.append(cnt)
    answer.append(zeros)
    return answer