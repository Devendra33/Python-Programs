from collections import Counter

lst = [1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 3, 5, 6, 6, 6, 6, 6, 8, 8, 8, 8, 8]
c = Counter(lst)
print(c)    # prints the counter object.
print(list(c))   # convert it list of unique element
print(dict(c))  # convert it dictionary element
print(set(c))   # convert it set of unique element
print(c.most_common(2))   # returns the highest frequency elements.
                #   |
                #   \/
                # number of tuples
