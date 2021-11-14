arr = list(input().split())
sorted_arr, reverse_sorted_arr = sorted(arr), sorted(arr, reverse=True)

if arr == sorted_arr:
  print("ascending")
elif arr == reverse_sorted_arr:
  print("descending")
else:
  print("mixed")