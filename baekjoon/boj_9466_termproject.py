# 한 번 확인해보면 이 학생이 싸이클에 속할 지 아닐 지 확신할 수 있음
# union find는 단순히 같은 집합에 속하는지 확인할 때 쓰는 알고리즘
# 싸이클 여부를 판단해야 하는 이러한 문제에서는 적절하지 않음
T = int(input())
for _ in range(1, T+1):
    n = int(input())
    students = [0] + list(map(int, input().split()))
    check = [0] * (n+1)
    result = 0
    for i in range(1, n+1):
        # 이미 확인된 학생은 넘어감
        if check[i]:
            continue
        # 내가 바라보고 있는 학생이 이미 확인된 학생이라면 나는 속하지 못함
        if check[students[i]]:
            check[i] = 1
            result += 1
            continue

        idx_dict = dict()
        target = i
        idx = 0
        while True:
            check[target] = 1
            idx_dict[target] = idx
            next = students[target]
            # 내가 바라보고 있는 학생이 경로에 있으면 싸이클 형성
            if next in idx_dict.keys():
                result += idx_dict[students[target]]
                break
            # 타고 타고 가다가 나가리된 학생 선택했을 때는 실패
            if check[next]:
                result += len(idx_dict)
                break
            # 다음 학생으로 넘어가기
            target = students[target]
            idx += 1
    print(result)






