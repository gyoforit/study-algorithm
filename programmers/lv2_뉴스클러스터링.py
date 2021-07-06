def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    set_1, set_2 = dict(), dict()
    # 딕셔너리 채우기
    for i in range(len(str1)-1):
        if (97 <= ord(str1[i]) <= 122) and (97 <= ord(str1[i+1]) <= 122):
            if not set_1.get(str1[i:i+2]):
                set_1[str1[i:i+2]] = 1
            else:
                set_1[str1[i:i+2]] += 1
    for j in range(len(str2)-1):
        if (97 <= ord(str2[j]) <= 122) and (97 <= ord(str2[j+1]) <= 122):
            if not set_2.get(str2[j:j+2]):
                set_2[str2[j:j+2]] = 1
            else:
                set_2[str2[j:j+2]] += 1
    # 교집합&합집합 구하기
    gyo = list(set(set_1.keys())&set(set_2.keys()))
    hap = list(set(set_1.keys())|set(set_2.keys()))
    # 교집합&합집합 원소의 개수
    result1 = 0
    result2 = 0
    if gyo:
        for g in gyo:
            tmp = min(set_1.get(g), set_2.get(g))
            result1 += tmp
    if hap:
        for h in hap:
            tmp1 = set_1.get(h) if set_1.get(h) else 0
            tmp2 = set_2.get(h) if set_2.get(h) else 0
            tmp3 = max(tmp1, tmp2)
            result2 += tmp3
    if result1 and result2:
        answer = int((result1/result2)*65536)
    elif not result1 and not result2:
        answer = 65536
    elif not result1:
        answer = 0
    return answer


# 스터디원 풀이: Counter 적극 활용!
from collections import Counter

def make_set(str):
    result = []
    for i in range(len(str) - 1):
        if str[i:i + 2].isalpha():
            result.append(str[i:i + 2].upper())
    return result


def solution(str1, str2):
    # 바로 set() 변환하면 중복되는 것들이 사라진다
    # Counter로 중복되는 것들이 몇 개 있는지 저장해두고 그 값을 활용
    set1 = Counter(make_set(str1))
    set2 = Counter(make_set(str2))
    if len(set1) == 0 and len(set2) == 0:
        answer = 65536
        return answer

    # Coutner.elements() : Counter의 숫자만큼 요소를 반환
    intersection = sum(list((set1 & set2).values()))
    union = sum(list((set1 | set2).values()))
    answer = int(intersection / union * 65536)

    return answer