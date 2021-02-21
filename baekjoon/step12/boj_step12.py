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