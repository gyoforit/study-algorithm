# words.sort(key = len) 로 하면 알아서 길이 기준으로 정렬된다.
word_dict = dict()
words = set()
N = int(input())
for _ in range(N):
    tmp = input()
    if tmp in words:
        continue
    words.add(tmp)
    l = len(tmp)
    if not word_dict.get(l):
        word_dict[l] = [tmp]
    else:
        word_dict[l].append(tmp)

keys = sorted(list(word_dict.keys()))
for k in keys:
    values = sorted(word_dict[k])
    for v in values:
        print(v)