# re.search(,) vs find()

# re.search(,) first one key and
# second one where and it return True or False
import re
with open('mboxx.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if re.search('Sat', line):
            print(line)

# find()
with open('mboxx.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line.find('Sat') >= 0:
            print(line)

# startswith() vs re.search()
# re.search()
with open('mboxx.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if re.search('^From', line):
            print(line)
# startswith()
with open('mboxx.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith('From'):
            print(line)
