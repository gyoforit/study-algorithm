def check(num):
    i = num + 1
    while True:
        if 1 <= bin(num ^ i).count('1') <= 2:
            return i
        i += 1


def solution(numbers):
    answer = []
    for number in numbers:
        answer.append(check(number))
    return answer