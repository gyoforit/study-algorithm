# 백준 12단계 - 정렬
# 210221
# 10814. 나이순 정렬
# 카운트 정렬로 풀이
N = int(input())
age = []
name = []
max_age = 0
for n in range(N):
    a, b = input().split()
    age.append(int(a))
    name.append(b)
    if int(a) > max_age:
        max_age = int(a)

cnt = [0] * (max_age+1)
for a in age:
    cnt[a] += 1
for i in range(len(cnt)-1):
    cnt[i+1] = cnt[i] + cnt[i+1]
result = [''] * N
for j in range(len(age)-1, -1, -1):
    cnt[age[j]] -= 1
    result[cnt[age[j]]] += str(age[j]) + ' ' + name[j]
for r in result:
    print(r)

#210228
# 2750. 수 정렬하기
N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

for i in range(N-1, -1, -1): # 비교 끝 인덱스
    for j in range(0, i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]

for n in nums:
    print(n)

# 10989. 수 정렬하기 3
# 인덱스랑 맞춤 -> 등장횟수 카운트해서 카운트수만큼 인덱스를 출력
import sys
N = int(input())

num = [0] * 10001

for _ in range(N):
    i = int(sys.stdin.readline())
    num[i] += 1

for n in range(10001):
    if num[n] != 0:
        for _ in range(num[n]):
            print(n)