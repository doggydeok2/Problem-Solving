def check_right_bigger(_l, _r):
    _x = 1
    while _l + _x < _r - _x:
        if word[_l + _x] < word[_r - _x]:
            return True
        elif word[_l + _x] > word[_r - _x]:
            return False
        _x += 1
    return True


N = int(input())
word, ans = [input() for _ in range(N)], []
l, r = 0, N - 1
while l <= r:
    if word[l] < word[r] or word[l] == word[r] and check_right_bigger(l, r):
        ans.append(word[l])
        l += 1
    else:
        ans.append(word[r])
        r -= 1
for i in range(0, N, 80):
    print(''.join(ans[i:i + 80]))
