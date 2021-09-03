A, B, C = map(int, input().split())
if C == B:
    ans = -1
else:
    cnt = A/(C-B)
    ans = -1 if cnt <= 0 else int(cnt)+1
print(ans)