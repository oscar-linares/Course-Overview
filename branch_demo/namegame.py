name = input('Enter your name: ')

for i in range(len(name), 0, -1):  # prints names minus on letter in every pass
    print(name[0:i], end= ' ')
    for j in range(i, len(name)):  # print letter after space
        print(' ' * (j-i) + name[j], end= '')
    print('')  # print space
