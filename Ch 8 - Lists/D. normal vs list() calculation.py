# normal avg calculation
total = 0
count = 0
while True:
    inp = input('Enter the value:\n')
    if inp == 'done':
        break
    else:
        value = float(inp)
        total = total + value
        count = count + 1
avg = total / count
print('avg: ', avg)

# using list() avg calculation
lis = list()
while True:
    inp = input('Enter the value:\n')
    if inp == 'done':
        break
    inp = float(inp)
    lis.append(inp)
print(lis)
avg = sum(lis) / len(lis)
print('avg: ', avg)
