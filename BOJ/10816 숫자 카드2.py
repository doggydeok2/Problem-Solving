import collections

N, cards, M = int(input()), collections.Counter(list(map(int, input().split()))), int(input())
for num in list(map(int, input().split())):
  print(cards[num], end=" ")