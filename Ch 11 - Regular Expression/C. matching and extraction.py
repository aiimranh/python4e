# matching and extracting data using re.findall()
# it return a list
import re
x = 'my two favourite number are 69 an 96'
y = re.findall('[0-9]+', x)
z = re.findall('[AEIOU]+', x)
print(y, z)

# greedy matching
x = 'From: using the: none'
y = re.findall('^F.+:', x)
print(y)

# non-greedy matching
x = 'From: using the: none'
y = re.findall('^F.+?:', x)
print(y)
