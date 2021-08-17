# 'w' over writting
handle = open('mbox-write.txt', 'w')
handle.write("hello\n")
handle.close()

# 'r+' working as a append if first read then write.
handle = open('mbox-write.txt', 'r+')
for line in handle:
    print(line, end='')
handle.write("hello\n")
handle.write("hello\n")
handle.close()

# 'a' does not readable
handle = open('mbox-write.txt', 'a')
handle.write("hello\n")
handle.write("hello\n")
handle.close()
