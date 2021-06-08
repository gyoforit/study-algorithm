def count_palin(word):
    cnt = 0
    for i in range(len(word)):
        for j in range(1, len(word)-i+1):
            tmp = word[i:i+j]
            if tmp == tmp[::-1]:
                cnt += 1
    return cnt

T = int(input())
for t in range(1, T+1):
    word = list(input())
    word.sort()
    print("#%d %s" % (t, count_palin(word)))
