def drawboard(size):
    size = int(size)
    row = " --- "
    col = "|  "
    # The number of rows is equal to size
    row *= size
    # The number of cols is equal to size+1
    col *= (size + 1)
    for i in range(size + 1):
        print(row)
        if (i < size):
            print(col)


drawboard(3)
