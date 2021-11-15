import collections


N, A, M = int(input()), collections.Counter(list(map(int, input().split()))), int(input())
for num in list(map(int, input().split())):
  print(1 if num in A else 0)
