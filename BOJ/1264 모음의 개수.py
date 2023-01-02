s = input()
while s != '#':
    print([c in 'aeiou' for c in s.lower()].count(1))
    s = input()
