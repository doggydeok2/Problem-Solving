S = input()
arr = [""] * len(S)
for i in range(len(S)):
  arr[i] = S[i:]

for word in sorted(arr):
  print(word)