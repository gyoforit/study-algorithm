# 210119
# 1000 A+B
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)

# 1001 A-B
a, b = input().split()
a = int(a)
b = int(b)
print(a - b)

# 1271 엄청난 부자2
m, n = input().split()
print(int(m) // int(n))
print(int(m) % int(n))
# 나눈 몫을 int로 반환하고 싶으면 // 사용

# 1550 16진수
n = input()
print(int(n, 16))
# int(문자열, n) = 해당 숫자를 n진수로 바꿔줌

# 2338 긴자리 계산
a = int(input())
b = int(input())
print(a + b)
print(a - b)
print(a * b)

#210124
# 10952 A+B - 5
while True:
  a, b = input().split()
  a = int(a)
  b = int(b)
    if a == 0 and b == 0:
        break
    print(a+b)

# 2475 검증수
numbers = input()
total = 0
length = len(numbers)
for i in range(length+1):
    if i % 2 == 0:
        total += int(numbers[i])**2
    total += int(numbers[0])**2
print(total % 10)

# 2557 Hello World
print('Hello World!')

# 2558 A+B - 2
a = int(input())
b = int(input())
print(a+b)