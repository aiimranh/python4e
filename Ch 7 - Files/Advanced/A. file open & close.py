# file open & close fn
f = open('mbox-short.txt', 'r+')
#  to read 'r' (by default)
#  to write 'w'
#  to read and write 'r+.
print(f.mode)
#  to print mode f.mode.
#  to print file name f.name.
f.close()

# contact manager auto close() the file.
# outside of the loop file will be closed.
with open('mbox-short.txt', 'r') as f:
    print(f.name)
