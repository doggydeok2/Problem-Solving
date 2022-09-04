from collections import defaultdict


a, b = map(int, input().split())
dic = defaultdict(int)
for n in list(map(int, input().split())):
    dic[n] += 1
for n in list(map(int, input().split())):
    dic[n] -= 1
print(len(dic) - list(dic.values()).count(0))
