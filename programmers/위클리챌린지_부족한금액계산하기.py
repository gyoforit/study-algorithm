def solution(price, money, count):
    answer = -1
    total = 0
    for i in range(1, count+1):
        total += i
    total *= price
    return total-money if total-money > 0 else 0