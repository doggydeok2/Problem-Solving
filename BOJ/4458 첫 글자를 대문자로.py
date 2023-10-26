def upperFirst(s):
    return s[0].upper() + s[1:]


for _ in range(int(input())):
    print(upperFirst(input()))
