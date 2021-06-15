# O(N) or O(N*log(N))
def solution(A):
    tmp = dict()
    for i in A:
        if i not in tmp.keys():
            tmp[i] = 1
        else:
            tmp[i] += 1

    for key in tmp.keys():
        if tmp[key] % 2:
            return key