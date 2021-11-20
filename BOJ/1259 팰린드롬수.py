def is_palindrome(str):
  for i in range(len(num) // 2):
    if num[i] != num[-i - 1]:
      return 0
  return 1


while True:
  num = input()
  if num == "0":
    break
  print("yes" if is_palindrome(num) else "no")
