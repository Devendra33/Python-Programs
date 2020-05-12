from collections import defaultdict
# default dictionary never throws KEYERROR
# it just returns the default value if key is not found.

d = defaultdict(lambda : 5)     # 5 is default value here.
d['one'] = 1
print('assigned val: ',d['one'])     # gives  1
print('default val: ',d['two'])    # gives 5