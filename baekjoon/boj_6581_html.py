words_list = []

while True:
    try:
        words = input().split()
        words_list += words
    except:
        break

result = []
sentence = ''
for w in words_list:
    if w == '<br>':
        result.append(sentence)
        sentence = ''
    elif w == '<hr>':
        if sentence:
            result.append(sentence)
        result.append('-'*80)
        sentence = ''
    else:
        if len(w)+len(sentence) >= 80:
            result.append(sentence)
            sentence = w
        else:
            if sentence:
                sentence += (' ' + w)
            else:
                sentence += w
result.append(sentence)

for r in result:
    print(r)