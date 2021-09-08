def solution(new_id):
    new_id = new_id.lower()
    tmp = ''
    for n in new_id:
        if len(tmp) >= 2 and n == '.' and tmp[-1] == '.':
            continue
        if n not in '~!@#$%^&*()=+[{]}:?,<>/':
            tmp += n
    tmp = tmp.strip('.')

    if len(tmp) == 0:
        tmp = 'a'
    elif len(tmp) >= 16:
        tmp = tmp[:15]
    if len(tmp) <= 2:
        tmp += tmp[-1] * (3 - len(tmp))
    return tmp.rstrip('.')