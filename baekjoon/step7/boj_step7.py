# 백준 7단계 - 문자열
# 210219
# 11654. 아스키 코드
print(ord(input()))

# 11720. 숫자의 합
N = int(input())
S = input()
total = 0
for s in S:
    total += int(s)
print(total)

# 10809. 알파벳 찾기
'''
알파벳 리스트 없이 아스키 코드로 풀 수 있다
'''
idx = [-1]*26
S = input()
for i, s in enumerate(S):
    if idx[ord(s)-97] == -1:
        idx[ord(s)-97] = i
    else:
        continue
print(' '.join(map(str, idx)))

# 2675. 문자열 반복
T = int(input())
for t in range(1, T+1):
    A, B = input().split()
    A = int(A)
    result = []
    for b in B:
        result.append(b*A)
    print(''.join(result))

# 1157. 단어 공부
'''
아스키 코드 활용. 더하고 빼는거 주의!
'''
S = input()
cnt = [0]*26
for s in S:
    if ord(s) < 97: # 대문자라면
        cnt[ord(s)-65] += 1
    else:
        cnt[ord(s)-97] += 1
mx = max(cnt)
mx_idx = 0
if cnt.count(mx) > 1:
    print("?")
else:
    for i in range(26):
        if cnt[i] == mx:
            mx_idx = i
    print(chr(mx_idx+65))