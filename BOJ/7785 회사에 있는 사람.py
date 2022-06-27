members = {}
for _ in range(int(input())):
    member, cmd = input().split()
    if cmd == 'enter':
        members[member] = True
    else:
        if members.get(member):
            del(members[member])
for member in sorted(list(members.keys()), reverse=True):
    print(member)
