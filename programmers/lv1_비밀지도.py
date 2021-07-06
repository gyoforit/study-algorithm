def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_1 = bin(arr1[i])[2:].zfill(n)
        bin_2 = bin(arr2[i])[2:].zfill(n)
        tmp = ''
        for j in range(n):
            decode = '#' if int(bin_1[j])|int(bin_2[j]) else ' '
            tmp += decode
        answer.append(tmp)
    return answer