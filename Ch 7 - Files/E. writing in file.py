xfile = open('mbox-short.txt', 'w')
xfile.write('line\n')
xfile.close()  # to save.

# to print()
xfile = open('mbox-short.txt')
for line in xfile:
    print(line)
