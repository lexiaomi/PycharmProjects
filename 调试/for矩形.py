rows = 4
for i in range(rows):
    if (i == 0) | (i == rows-1):
        for j in range(rows):
            print(' *', end='')
    else:
        for j in range(1):
            print(' *', end='')
        for j in range(rows-2):
            print('  ', end='')
        for j in range(1):
            print(' *', end='')
    print()