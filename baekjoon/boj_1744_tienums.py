# 수 관련 문제에서는 0, 1을 항상 고려하기!
# 1 끼리 남았을 때 곱하기 보다 더하기가 더 커지므로 1만 따로 모아놓기
# 음수의 경우 같은 음수를 곱하거나 0을 곱했을 때 - 가 상쇄되기 때문에 0, 음수는 같이 모아놓기
N = int(input())
plus = []
minus = []
one = []
for _ in range(N):
    tmp = int(input())
    if tmp > 1:
        plus.append(tmp)
    elif tmp <= 0:
        minus.append(tmp)
    else:
        one.append(tmp)
plus.sort(reverse=True)
minus.sort()

max_num = 0
P = len(plus)
M = len(minus)
if P:
    if P%2:
        max_num += (sum([plus[i]*plus[i+1] for i in range(0, P-2, 2)])+plus[-1])
    else:
        max_num += sum([plus[i]*plus[i+1] for i in range(0, P, 2)])
if M:
    if M%2:
        max_num += (sum([minus[i] * minus[i + 1] for i in range(0, M-2, 2)]) + minus[-1])
    else:
        max_num += sum([minus[i]*minus[i+1] for i in range(0, M, 2)])
max_num += sum(one)

print(max_num)