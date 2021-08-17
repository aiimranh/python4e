# tuple much like list.
x = ('glenn', 'sally', 'joseph')
print(x)

# it has index start with 0
# they maintain order
y = ('glenn', 'sally', 'joseph')
print(y[0])
for i in y:
    print(i)

# tuple are immutable
z = ('glenn', 'sally', 'joseph')  # z[0] = 'sss'
print(z)

# tuple can assign multiple parameter
(a, b) = (1, 2)
print(a, b)
(c, d, e) = (3, 4, 6)
print(c, d, e)

# tuple are comparable
x = (0, 1, 2) < (5, 1, 2)
print(x)
x = (0, 2, 2) < (0, 1, 5)
print(x)
x = ('abc', 'cde') < ('bcd', 'efg')
print(x)
