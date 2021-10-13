def solution(n, lost, reserve):
    students = [1]*(n+1)
    # 잃어버린 학생 -1
    for l in lost:
        students[l] -= 1
    # 여분 있는 학생 +1
    for r in reserve:
        students[r] += 1
    # 첫번째 학생 -> 두번째 학생이 여벌 있으면 나눠줌
    if not students[1] and students[2] == 2:
        students[1] += 1
        students[2] -= 1
    # 2~(n-1)번째 학생 -> 양 옆 중 한명이 여벌 있으면 나눠가짐
    for i in range(2, n):
        if not students[i]:
            if students[i-1] == 2:
                students[i-1] -= 1
                students[i] += 1
            elif students[i+1] == 2:
                students[i+1] -= 1
                students[i] += 1
    # n번째 학생 -> (n-1)번째 학생이 여벌 있으면 나눠줌
    if not students[n] and students[n-1] == 2:
        students[n] += 1
        students[n-1] -= 1
    return sum([1 for i in range(1, n+1) if students[i]])