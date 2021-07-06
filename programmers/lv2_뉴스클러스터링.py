def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    set_1, set_2 = dict(), dict()
    for i in range(len(str1)-1):
        if (97 <= ord(str1[i]) <= 122) and (97 <= ord(str1[i+1]) <= 122):
            if not set_1.get(str1[i:i+2]):
                set_1[str1[i:i+2]] = 1
            else:
                set_1[str1[i:i+2]] += 1
    for j in range(len(str2)-1):
        if (97 <= ord(str2[j]) <= 122) and (97 <= ord(str2[j+1]) <= 122):
            if not set_2.get(str2[j:j+2]):
                set_2[str2[j:j+2]] = 1
            else:
                set_2[str2[j:j+2]] += 1
    gyo = list(set(set_1.keys())&set(set_2.keys()))
    hap = list(set(set_1.keys())|set(set_2.keys()))
    result1 = 0
    result2 = 0
    if gyo:
        for g in gyo:
            tmp = min(set_1.get(g), set_2.get(g))
            result1 += tmp
    if hap:
        for h in hap:
            tmp1 = set_1.get(h) if set_1.get(h) else 0
            tmp2 = set_2.get(h) if set_2.get(h) else 0
            tmp3 = max(tmp1, tmp2)
            result2 += tmp3
    if result1 and result2:
        answer = int((result1/result2)*65536)
    elif not result1 and not result2:
        answer = 65536
    elif not result1:
        answer = 0
    return answer