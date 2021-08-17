# file open
handle = open('mbox-short.txt', 'r')
# file read as sa line sequence
for line in handle:
    print(line, end='')
# file close
handle.close()

handle = open('mbox-short.txt', 'r')
handle_read = handle.read()
print(handle_read)
handle.close()

# file open
handle = open('mbox-short.txt', 'r')
handle_read = handle.readline()
print(handle_read)
handle.close()

handle = open('mbox-short.txt', 'r')
handle_read = handle.readline()
while len(handle_read) > 0:
    print(handle_read, end='')
    handle_read = handle.readline()
handle.close()

# file open
handle = open('mbox-short.txt', 'r')
handle_read = handle.readline(57)
print(handle_read, end='')
handle_read = handle.readline(50)
print(handle_read, end='')
handle_read = handle.readline(60)
print(handle_read, end='')
handle_read = handle.readline(50)
print(handle_read, end='')
handle.close()

handle = open('mbox-short.txt', 'r')
handle_read = handle.read(50)
while len(handle_read) > 0:
    print(handle_read, end='')
    handle_read = handle.read(50)
handle.close()

handle = open('mbox-short.txt', 'r')
handle_read = handle.readlines()
print(handle_read)
handle.close()
