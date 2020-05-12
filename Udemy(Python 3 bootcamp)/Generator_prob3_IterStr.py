s = 'Hello world'
g = iter(s)
print(next(g))    # when reaches out of range throws StopIteration error.

# for printing the whole string:
for i in g:        # it starts from e as H is already readen by next(g).
    print(i)