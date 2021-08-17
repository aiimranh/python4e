# fine-tuning string extraction
# [^ ] == \S but it sometimes says invalid
import re
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('[^ ]+@[^ ]+', x)
print(y)

# matching and fine-tuning string extraction
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From ([^ ]+@[^ ]+)', x)
print(y)

# string parsing
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]+)', x)
print(y)

# string parsing more specified
x = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From.*@([^ ]+)', x)
print(y)
