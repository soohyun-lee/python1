for i in range(1,51):
    if ('3' in str(i)) or ('6' in str(i)) or ('9' in str(i)):
        print('*', end =' ')
    else:
        print(i, end=' ')