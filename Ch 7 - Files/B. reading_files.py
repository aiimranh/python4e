#  for loop for reading files.
xfile = open('mbox.txt')
for line in xfile:
    print(line)

#  read() handle for reading files and it make the file into a string.
xfile = open('mbox.txt')  # to work any file handle operation, first we take open() operation.
xread = xfile.read()
print(xread)


#  counting number of line in files.
xfile = open('mbox.txt')
count = 0
for line in xfile:
    count = count + 1
print('line n umber:', count)

#  python make whole file in a single string.
xfile = open('mbox.txt')  # to work any file handle operation, first we take open() operation.
xread = xfile.read()
xlen = len(xread)
print('total string len:', xlen)
print(xread[:20])
