V = int(input())
votes = sorted(list(input()))
print('Tie' if V % 2 == 0 and votes[V // 2 - 1] != votes[V // 2] else votes[V // 2])
