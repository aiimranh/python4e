# dictionaries declaration
# dictionaries  have no order

# method - I
bag = dict()  # empty dictionaries
print(bag)

# method - II
bag = {'money': 200, 'banana': 2, 'health': 3}
print(bag)

# dictionary assigning
desk = dict()
desk['port'] = 3
desk['book'] = 10
print(desk)

# dictionary expanding
bag['port'] = 3
bag['book'] = 10
print(bag)

# printing the dictionary loop
counts = {'From': 1, 'Sat': 1, 'Jan': 1, 'Return': 1}
for key in counts:
    print(key, ':', counts[key])
