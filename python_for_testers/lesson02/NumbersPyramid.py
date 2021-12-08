def create_pyramid(size):
    for i in range(1,size+1):
        for j in range(i):
            print(i, end='')
        print()  # print new line


create_pyramid(9)
