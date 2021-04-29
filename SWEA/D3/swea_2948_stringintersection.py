'''
주의점: 처음부터 set으로 받아오면 아슬아슬하게 통과~runtime error남
연산할 때만 set으로 바꿔주는 게 좋다
'''
T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    n_list = input().split()
    m_list = input().split()
    print("#%d %d" % (t, len(list(set(n_list) & set(m_list)))))