keypad = [(3, 1), (0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]

def solution(numbers, hand):
    answer = ''
    left, right = (3, 0), (3, 2)
    set1 = {1, 4, 7}
    set2 = {3, 6, 9}
    for num in numbers:
        key_rc = keypad[num]
        # 왼손으로만 누를 수 있는 숫자
        if num in set1:
            answer += 'L'
            left = key_rc
        # 오른손으로만 누를 수 있는 숫자
        elif num in set2:
            answer += 'R'
            right = key_rc
        # 2, 5, 8, 0 이라면
        else:
            # 각 손가락으로부터 거리 재서 파악
            dis_l = abs(left[0]-key_rc[0])+abs(left[1]-key_rc[1])
            dis_r = abs(right[0]-key_rc[0])+abs(right[1]-key_rc[1])
            if dis_l > dis_r:
                answer += 'R'
                right = key_rc
            elif dis_l < dis_r:
                answer += 'L'
                left = key_rc
            else:
                if hand == 'right':
                    answer += 'R'
                    right = key_rc
                else:
                    answer += 'L'
                    left = key_rc
    return answer

# print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
# print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], 'left'))
# print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], 'right'))