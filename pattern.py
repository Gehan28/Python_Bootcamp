# print('\U0001f600')
print('Pattern')
for i in range(1, 11):
    print('*'*i)

print('------------------------------------------------------------------')
print('Pattern')
for i in range(10, 0, -1):
    print('*'*i)

print('------------------------------------------------------------------')
print('Pattern')
l = []
for x in range(0, 11):
    l.append('*')
for i in range(0, 6):
    print(*l)

print('------------------------------------------------------------------')
print('Pattern')
l = []
for x in range(0, 11):
    l.append('*')
for i in range(0, 6):
    print(*l)
    l[i] = l[10-i] = ' '

print('------------------------------------------------------------------')
print('Pattern')
l = []
for x in range(0, 11):
    l.append(' ')
l[5] = '*'
for i in range(0, 6):
    l[5-i] = l[5+i] = '*'
    print(*l)
