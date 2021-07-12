N = int(input())
result = []
for _ in range(N):
    brackets = input()
    stack = []
    for b in brackets:
        if b == '(':
            stack.append(b)
        else:
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(b)
    if not stack:
        result.append('YES')
    else:
        result.append('NO')

for r in result:
    print(r)
