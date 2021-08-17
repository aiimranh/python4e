# tuple and dictionaries
# method  - I
d = dict()
d['a'] = 1
d['b'] = 2
for key, value in d.items():
    print(key, value)

# method  - I
d = dict()
d['a'] = 1
d['b'] = 2
print(d.items())

# dictionaries sorting(by key) using tuple
d = {'a': 10, 'b': 1, 'c': 22}
# # dictionary to tuple pair,
# p = d.items()
# # further tuple to list
# t = sorted(p)
t = sorted(d.items())
# for i in t:  # print tuple pair
#     print(i)
for k, v in t:
    print(k, v)

# dictionaries sorting(by value) using tuple
d = {'a': 10, 'b': 1, 'c': 22}
tmp = list()
for k, v in d.items():
    tmp.append((v, k))
tmp = sorted(tmp)
# ascending sorting
print(tmp)
tmp = sorted(tmp, reverse=True)
# descending sorting
print(tmp)
