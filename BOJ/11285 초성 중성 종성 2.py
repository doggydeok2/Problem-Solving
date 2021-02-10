alphabet = ['ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ', 'ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ', '~ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ']
lenAlphabet = [19, 21, 28]

code = 44032
for i in range(3):
    cmd = input()
    for j in range(lenAlphabet[i]):
        if alphabet[i][j] == cmd:
            if not i:
                code += j * 21 * 28
            elif i < 2:
                code += j * 28
            else:
                code += j

print(chr(code))