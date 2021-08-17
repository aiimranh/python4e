lst = [1, 2, [1, 2], (1, 2)]
lus = [7, 8, 9]

# to add multiple item in a list slice squeezing method
lus[1:1] = [9, 10]
print(lus)      # [7, 9, 10, 8, 9]

# negative indexing start -1 refer to 0 index item!
print(lst[1], lst[3])   # 2 (1, 2)
print(lst[-1], lst[-4])  # (1, 2) 1

# Index slicing
print(lst[2:])      # [[1, 2], (1, 2)]
print(lst[-len(lst):-2])      # [1, 2]

# third index step call
print(lst[0:len(lst):2])    # [1, [1, 2]]

# to add a single item to the list in last
lst.append(12)
print(lst)  # [1, 2, [1, 2], (1, 2), 12]

# to add a single item to the list at specific position
lst.insert(2, 44)
print(lst)    # [1, 2, 44, [1, 2], (1, 2), 12]

# to add multiple item to the list in last
lst.extend([11, 12, 13])
print(lst)  # [1, 2, 44, [1, 2], (1, 2), 12, 11, 12, 13]

# to copy list
z = lst.copy()
print(z)    # [1, 2, 44, [1, 2], (1, 2), 12, 11, 12, 13]

# to count specific value in the list
print(lst.count(1))     # 1

# to remove list item using value
lst.remove(2)
print(lst)     # [1, 44, [1, 2], (1, 2), 12, 11, 12, 13]

# to remove item in last using pop() and specific position
lst.pop(2)
print(lst)      # [1, 44, (1, 2), 12, 11, 12, 13]

# to reverse any list.
lst.reverse()
print(lst)      # [13, 12, 11, 12, (1, 2), 44, 1]

# to any list sort
# list in list and tuple in list does not allow!
lus.sort()
print(lus)      # [7, 8, 9, 9, 10]

# to get an index of the item
print(lst.index(11))    # 2

# to empty the list.
lst.clear()
print(lst)      # []
