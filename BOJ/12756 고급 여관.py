aa, ad = map(int, input().split())
ba, bd = map(int, input().split())
ans = (ad // ba + (not not (ad % ba)) - bd // aa - (not not (bd % aa)))
print('PLAYER A' if ans > 0 else 'PLAYER B' if ans < 0 else 'DRAW')
