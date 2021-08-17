# wild card

# with whitespace
import re
with open('sbox.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if re.search('^X.*:', line):
            print(line)

# without whitespace
with open('sbox.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if re.search('^X-\S+:', line):
            print(line)
