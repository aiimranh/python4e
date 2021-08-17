# lists vs dictionaries

# lists
lst = list()
lst.append(21)
lst.append('money')
print(lst)
lst[1] = 20
print(lst)

# dictionaries
dic = dict()
dic['money'] = 21
dic['save'] = 'money'
print(dic)
dic['save'] = 20
print(dic)

# dictionary key covert to list()
counts = {'From': 1, 'Sat': 1, 'Jan': 1, 'Return': 1}
lis = list(counts)
print(lis)

#  to show the dictionary values and keys in list view
counts = {'From': 1, 'Sat': 1, 'Jan': 1, 'Return': 1}
key = counts.keys()
value = counts.values()
print(key)
print(value)

# to show the dictionary values and keys in tuple view
counts = {'From': 1, 'Sat': 1, 'Jan': 1, 'Return': 1}
tup = counts.items()
print(tup)

# two iteration variables.
counts = {'From': 1, 'Sat': 1, 'Jan': 1, 'Return': 1}
for a, b in counts.items():
    # two variable work may be only tuple
    print(a, b)
