# 교집합이 1이상이면서 원소가 서로 달라야 한다 = 공통원소가 반드시 1개 있어야 한다
from collections import Counter
def solution(a):
    answer = -1
    # 카운트배열의 딕셔너리 버전을 만들어주는 Counter
    cnt_dict = Counter(a)

    for num in cnt_dict.keys():
        # 공통 원소의 개수가 answer 보다 작으면 더 볼 필요 x
        if cnt_dict[num] <= answer:
            continue
        tmp = 0
        i = 0
        while i < len(a)-1:
            # 조건에 맞지 않으면 인덱스 1칸 이동하여 다시 확인
            if (a[i] == a[i+1]) or (a[i] != num and a[i+1] != num):
                i += 1
                continue
            # 조건에 맞으면 맞는 원소 개수 +1, 인덱스 2칸 이동
            tmp += 1
            i += 2
        answer = max(answer, tmp)

    if answer == -1:
        return 0
    # answer는 공통원소의 개수이므로 *2 해서 리턴
    return answer*2


print(solution([0,3,3,0,7,2,0,2,2,0]))
print(solution([0]))