grid = [[2,0,0,0,0,9,4,0,5],
    [0,0,0,2,4,0,8,3,0],
    [0,0,0,0,8,0,0,0,0],
    [7,0,0,4,0,0,6,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,9,0,0,0,0,5,7],
    [0,0,0,0,3,0,0,0,0],
    [0,6,5,0,0,0,0,0,0],      
    [1,0,3,8,0,0,0,0,6]]       


print(grid)


import numpy as np
print(np.matrix(grid))


def prettify():
    print("Output: ")
    global grid
    j = 0
    for row in grid:
        i = 0
        j+=1
        for item in row:
            i+=1
            print(f" {item} ", end='')
            if i % 3 == 0 and i <9:
                print (" | ", end='')
        print()
        if j % 3 ==0 and j <9:    
            print('-'*33)

# prettify()


def possible(y,x,n):
    global grid
    for i in range(9):
        if grid[y][i] == n:
            return False
    for i in range(9):
        if grid[i][x] == n:
            return False
    x0 = (x//3)*3
    y0 = (y//3)*3
    
    for i in range(3):
        for j in range(3):
            if grid[y0+i][x0+j] == n:
                return False
    return True


possible(0,2,1)


def solve():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1,10):
                    if possible(y,x,n):
                        grid[y][x] = n
                        solve()
                        grid[y][x] = 0
                return
    prettify()
    input("More?")


solve()
