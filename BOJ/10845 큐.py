import collections, sys
input = sys.stdin.readline


q = collections.deque()
for _ in range(int(input())):
  user_input = input()
  cmd = user_input.split(" ")[0]
  if cmd == 'push':
    q.append(user_input.split(' ')[1][:-1])
  elif cmd == 'front\n':
    print(q[0] if len(q) else -1)
  elif cmd == 'back\n':
    print(q[-1] if len(q) else -1)
  elif cmd == 'size\n':
    print(len(q))
  elif cmd == 'empty\n':
    print(0 if len(q) else 1)
  elif cmd == 'pop\n':
    print(q.popleft() if len(q) else -1)