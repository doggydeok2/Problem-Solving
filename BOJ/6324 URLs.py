import sys
input = sys.stdin.readline

n = int(input())
for tc in range(1, n + 1):
    link = input()[:-1]
    protocol = link.split('://')[0]
    link = link[link.find('://') + 3:]

    host = port = path = '<default>'
    flag = 1
    for i in range(len(link)):
        if link[i] == '/':
            host, path = link[:i], link[i + 1:]
            flag = 0
            break
    if flag:
        host = link

    for i in range(len(host)):
        if host[i] == ':':
            host, port = host[:i], host[i + 1:]
            break

    print(f'URL #{tc}')
    print(f'Protocol = {protocol}')
    print(f'Host     = {host}')
    print(f'Port     = {port}')
    print(f'Path     = {path}')
    print()
