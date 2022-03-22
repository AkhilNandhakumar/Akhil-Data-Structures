def triangle_pattern():
    row = 9

    for i in range(row):
        for j in range(row-i):
            print(' ', end='')

        for j in range(2*i+1):
            print('*',end='')
        print()
    print("---------------------")