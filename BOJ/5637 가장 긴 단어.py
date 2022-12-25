import re


def get_longest():
    ans = ''
    while True:
        s, p = input(), re.compile('[a-zA-Z\-]+')
        for word in p.findall(s):
            if len(ans) < len(word):
                ans = word
            if word == 'E-N-D':
                return ans


print(get_longest().lower())
