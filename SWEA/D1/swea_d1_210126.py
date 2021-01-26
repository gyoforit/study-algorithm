# 2046. 스탬프 찍기
n = int(input())
print("#"*n)

# 2047. 신문 헤드라인
n = input()
print(n.upper())

# 1938. 아주 간단한 계산기 - split 뒤에 항상 () 쓰기!
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
# f-sting 이용해서 출력 가능
print(f'{a+b}\n{a-b}\n{a*b}\n{a//b}')

# 2058. 자릿수 더하기
a = int(input())
total = 0
while a > 0:
    total += a % 10
    a //= 10
print(total)

# 1936. 1대1 가위바위보 - output에 주의하자!
a, b = map(int, input().split())
if a > b:
    if a == 3 and b == 1:
        print('B')
    else:
        print('A')
elif a < b:
    if a == 1 and b == 3:
        print('A')
    else:
        print('B')

# 2025. N줄 덧셈
a = int(input())
total = 0
for i in range(1, a+1):
    total += i
print(total)

# 2043. 서랍의 비밀번호 - 애초에 변수 크기 제한이어서 첫번째 경우만 출력하면 됐음!
a, b = map(int, input().split())
if a > b:
    print(a-b+1)
elif a < b:
    print(1000-b+a)
else:
    print(0)

# 2027. 대각선 출력하기
for i in range(5):
    n = ['+', '+', '+', '+']
    n.insert(i, '#')
    print(''.join(n))

# 승호님 풀이
for i in range(5):
    print('+' * i + '#' + '+' * (4 - i))

# 주엽님 풀이
for i in range(5):
    for j in range(5):
        if i == j:
            print('#', end='')
        else:
            print('+', end='')
    print()

# 1933. 간단한 N의 약수
n = int(input())
for i in range(1, n+1):
    if n % i ==0:
        print(i, end=' ') # '1 2 5 10 '으로 출력. 맨 뒤에 공백 어떻게 없애지?

# 공백 없애는 법
n = int(input())
result = ''
for i in range(1, n+1):
    if n % i ==0:
        result += (i + ' ')
print(result[:-1]) # 처음부터 맨 마지막 전까지 slicing!

# 2029. 몫과 나머지 출력하기
a = int(input())
for i in range(a):
    x, y = map(int, input().split())
    print(f'#{i+1} {x//y} {x%y}')