# 2068. 최대수 구하기
T = int(input())
numbers = []
for i in range(T):
    numbers =list(map(int, input().split()))
    max_number = numbers[0]
    for num in numbers:
        if num > max_number:
            max_number = num
    print(f'#{i+1} {max_number}')
# 이제야 input 넣는 방법을 깨달았다...

# 2070. 큰 놈, 작은 놈, 같은 놈
T = int(input())
for i in range(T):
    a, b =map(int, input().split())
    if a > b:
        print(f'#{i+1} >')
    elif a == b:
        print(f'#{i+1} =')
    else:
        print(f'#{i+1} <')

# 2050. 알파벳을 숫자로 변환
empty_list = []
empty_list.extend(input())
new_list = []
for i in range(len(empty_list)):
	new_list += [str(ord(empty_list[i]) - 64)]
print(' '.join(new_list))
#.join() 자꾸 헷갈림. 리스트 속 '문자열'(not int)들을 합체하는 것!
    
# 2063. 중간값 찾기
T = int(input())
numbers = list(map(int, input().split()))
sorted_list = sorted(numbers)
length = len(numbers)
print(sorted_list[length//2])

# 2019. 더블더블
a = int(input())
result = []
for i in range(a+1):
    result += [f'{2**(i)}']
print(' '.join(result))

# 1545. 거꾸로 출력해 보아요
a = int(input())
result = []
while a > 0:
    result.append(str(a))
    a -= 1
print(' '.join(result))

# 2072. 홀수만 더하기
T = int(input())
for i in range(T):
    result = list(map(int, input().split()))
    total = 0
    for number in result:
        if number % 2:
            total += number
    print(f'#{i+1} {total}')

# 2071. 평균값 구하기
T = int(input())
for i in range(T):
	result = list(map(int, input().split()))
	total = 0
	for number in result:
		total += number
	total = total / len(result)
	print(f'#{i+1} {round(total)}')

# 2056. 연월일 달력
T = int(input())
for i in range(T):
    ymd = input()
    yr = ymd[0:4]
    mnth = ymd[4:6]
    dy = ymd[6:8]
    
    if int(mnth) in [1, 3, 5, 7, 8, 10, 12]:
            if int(dy) < 1 or int(dy) > 31 or yr == '0000':
                print(f'#{i+1} -1')
            else:
                print(f'#{i+1} {yr}/{mnth}/{dy}')
    elif int(mnth) == 2:
            if int(dy) < 1 or int(dy) > 28 or yr == '0000':
                print(f'#{i+1} -1')
            else:
                print(f'#{i+1} {yr}/{mnth}/{dy}')
    elif int(mnth) in [4, 6, 9, 11]:
            if int(dy) <1 or int(dy) > 30 or yr == '0000':
                print(f'#{i+1} -1')
            else:
                print(f'#{i+1} {yr}/{mnth}/{dy}')
    elif int(mnth) == 0:
        print(f'#{i+1} -1')