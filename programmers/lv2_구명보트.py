# 투포인터 사용
# 제일 가벼운사람 + 무거운사람 조합 가능하면 태우고
# 안되면 무거운사람만 태워 보내기
def solution(people, limit):
    answer = 0
    people.sort()
    left, right = 0, len(people) - 1
    while left < right:
        if people[left] + people[right] <= limit:
            left += 1
            right -= 1
        else:
            right -= 1
        answer += 1
        if left == right:
            answer += 1

    return answer