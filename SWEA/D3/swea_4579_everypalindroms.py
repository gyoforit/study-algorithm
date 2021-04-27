def ispalin(s):
    for i in range(len(s)//2):
        if s[i] == '*' or s[-1-i] == '*':
            return 'Exist'
        elif s[i] != s[-1-i] and s[i] != '*' and s[-1-i] != '*':
            return 'Not exist'
    return 'Exist'

T = int(input())
for t in range(1, T+1):
    target = input()
    print("#%d %s" % (t, ispalin(target)))