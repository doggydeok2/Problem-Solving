for _ in range(int(input())):
  N, K = map(int, input().split())
  candies = list(map(int, input().split()))
  print(sum([candy // K for candy in candies]))
