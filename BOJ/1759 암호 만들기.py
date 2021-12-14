def check_password(passwords, idx, vowel, consonant):
    if len(passwords) == L:
        if vowel > 0 and consonant > 1:
            print(''.join(passwords))
    elif idx >= C:
        pass
    else:
        if chars[idx] in vowels:
            check_password(passwords + [chars[idx]], idx + 1, vowel + 1, consonant)
        else:
            check_password(passwords + [chars[idx]], idx + 1, vowel, consonant + 1)
        check_password(passwords, idx + 1, vowel, consonant)


L, C = map(int, input().split())
chars = sorted(list(input().split()))
vowels = ['a', 'e', 'i', 'o', 'u']
check_password([], 0, 0, 0)
