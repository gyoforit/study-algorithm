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