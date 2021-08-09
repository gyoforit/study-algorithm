import sys
sys.stdin = open('input.txt')

A, B = input().split()
min_val = 987654321
for i in range(0, len(B)-len(A)+1):
    cnt = 0
    for j in range(0, len(A)):
        if B[i+j] != A[j]:
            cnt += 1
            if cnt >= min_val:
                break

    min_val = min(cnt, min_val)

print(min_val)