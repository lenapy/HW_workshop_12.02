def gen():
    i = 0
    while True:
        yield i
        i += 1

g = gen()
lst = []
lst.append((g.__next__(), "0"))
lst.append((g.__next__(), "0"))
lst.append((g.__next__(), "0"))
print(lst)
