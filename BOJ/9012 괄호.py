def check(sen):
    s = 0
    for ch in sen:
            if ch == '(':
                s += 1
            else:
                if s:
                    s -= 1
                else:
                    return 'NO'
    return 'NO' if s else 'YES'


T = int(input())
for tc in range(T):

    sentence = input()
    print(check(sentence))