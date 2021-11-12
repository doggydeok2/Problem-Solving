N = int(input())
easiest_problem, easiest_score = '', 5
for i in range(N):
  problem, score = input().split()
  score = int(score)
  
  if score < easiest_score:
    easiest_problem = problem
    easiest_score = score

print(easiest_problem)