N = int(input())
Ais = list(map(int, input().split()))
B, C = map(int, input().split())
print(sum([1 + max(Ai - B, 0) // C + (not not max(Ai - B, 0) % C) for Ai in Ais]))
