def solution(number, k):
    stack = []
    i = 0
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            k -= 1
            stack.pop()
        stack.append(number[i])
    return ''.join(stack[:len(number)-k])