strShort, strLong = input(), input()
ls, ll = len(strShort), len(strLong)
if ls > ll:
    strShort, strLong = strLong, strShort
    ls, ll = ll, ls

cntLong = [0] * ll
maxLen = 0

for i in range(ls):
    tmpCntMax = 0
    for j in range(ll):
        if strLong[j] == strShort[i] and cntLong[j] < tmpCntMax + 1:
            cntLong[j] = tmpCntMax + 1
        else:
            if tmpCntMax < cntLong[j]:
                tmpCntMax = cntLong[j]

print(max(cntLong))
