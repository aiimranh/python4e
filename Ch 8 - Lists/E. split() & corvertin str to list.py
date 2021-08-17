# split() fn convert str to list()
a = 'there are you'
x = a.split()
# by default it split on white space.
print(x)

# but you can pass any argument and
# split() the str into list().
y = 'first,second,third'
c = y.split(',')
print(c)

# find() vs list() and split()
# extraction email from mboxx.txt using find
with open('mboxx.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("From:"):
            fir = line.find(' ')
            sec = line.find(' ', fir+1)
            print(line[fir:sec])

# extraction email from mboxx.txt using list()
op = list()
with open('mboxx.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("From:"):
            temp = line.split()
            op.append(temp[1])
print(op)

# double or multiple split()
ops = list()
with open('mboxx.txt', 'r') as rf:
    for line in rf:
        line = line.rstrip()
        if line.startswith("From:"):
            tem = line.split(' ')
            sem = tem[1].split('@')
            ops.append(sem[1])
print(ops)
