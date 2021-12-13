import sys
rl = sys.stdin.readline


N, M = map(int, rl().rstrip().split())
monster_dict = {}

for i in range(1, N + 1):
    question = rl().rstrip()
    monster_dict[question] = str(i)
    monster_dict[str(i)] = question

for i in range(1, M + 1):
    print(monster_dict[rl().rstrip()])
