# len() fn return how many of element in list.
# but in str, len() fn return how many character str have.
list_list = [1, "hello", ['Bye', 2]]
print(len(list_list))

# range(int n) fn return a list from 0 upto n-1
x = range(5)
for y in x:
    print(y)

# range fn use in list printing.
list_list = [1, "hello", ['Bye', 2]]
for x in range(len(list_list)):
    print(list_list[x])
