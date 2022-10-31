R, C, N = map(int, input().split())
print(((R // N + (not not R % N)) * (C // N + (not not C % N))))
