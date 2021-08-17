# list concatenating
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

# list slicing
d = c[3:]
e = c[:3]
print(d)
print(e)

# list copying
f = a
print(f)

# list slicing as copying
g = c[:]
print(g)

# to create a empty list()
# method - 1:
x = list()
print(x)

# method - 2:
y = []
print(y)

# checking operation of list
print(dir(x))

# building a list from scratch
lis = list()
lis.append('Hello')
lis.append(98)
print(lis)

# in / not in to checking a value in list
print('Hello' in lis)
print('Hello' not in lis)

# sorting the list.
# sorting support only in same data type.
li = [1, 23, 5, 3, 9, 0]
li.sort()
print(li)

# more operation in list()
print(len(li))
print(max(li))
print(min(li))
print(sum(li))
