# lists can contain any element with same or different
# types of data.
num_list = [1, 2, 3]
print(num_list)
str_list = ['hello', 'bye']
print(str_list)
com_list = ['hello', 2]
print(com_list)

# Lists can contain also another list.
list_list = [1, "hello", ['Bye', 2]]
print(list_list)

# list can be empty
lis = []
print(lis)

# printing by each element of the list.
for x in list_list:
    print(x)
print("Done!")

# list have order, start with 0 index.
print(num_list[2])

# list are mutable
num_list[2] = 'xxx'
print(num_list)
