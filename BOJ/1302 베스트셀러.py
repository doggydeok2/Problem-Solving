import collections


N = int(input())
books = collections.Counter([input() for _ in range(N)])
print(sorted(books.keys(), key=lambda x: (-books[x], x))[0])
