import sys
import collections
rl = sys.stdin.readline


N, M = map(int, rl().rstrip().split())
human_dict = collections.defaultdict(int)
cnt = 0
no_see_no_hear = []

for i in range(N):
    human = rl().rstrip()
    human_dict[human] += 1

for i in range(M):
    human = rl().rstrip()
    if human_dict[human]:
        cnt += 1
        no_see_no_hear.append(human)

print(cnt)
for people in sorted(no_see_no_hear):
    print(people)
