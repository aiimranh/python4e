# [0-9]+.[0-9]+ == [0-9.]+
import re
lst = list()
with open('mbox.txt', 'r') as f:
    for line in f:
        line = line.rstrip()
        tem = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
        # tem always clear for the next loop
        if len(tem) == 0:
            continue
        num = float(tem[0])
        lst.append(num)
print('Maxi :', max(lst))

# escape character
x = 'we just received $10.00 for cookies'
y = re.findall('\$[0-9.]+', x)
print(y)
