import collections
import sys
rl = sys.stdin.readline


for _ in range(int(rl())):
    rl()
    dic = collections.Counter(list(map(int, rl().split())))
    rl()
    for num in list(map(int, rl().split())):
        print([0, 1][dic[num] > 0])
