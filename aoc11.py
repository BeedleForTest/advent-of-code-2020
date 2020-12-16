import numpy
with open('input11.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def occupied_adjacent_seats(x,y,matrix):
    comp = 0
    for i in range(x-1,x+2):
        for j in range(y-1,y+2):
            if i != x or j != y:
                try:
                    if matrix[i,j] == '#':
                        comp += 1
                except:
                    pass
    return comp

def exo1(array):
    height, width = array.shape
    change = True
    res = 0
    while change:
        matrix = numpy.copy(array)
        change = False
        res = 0
        for x in range(height):
            for y in range(width):
                if array[x,y] == 'L' and occupied_adjacent_seats(x,y,matrix) == 0:
                    array[x,y] = '#'
                    change = True
                if array[x,y] == '#':
                    if occupied_adjacent_seats(x,y,matrix) >= 4:
                        array[x,y] = 'L'
                        change = True
                    else:
                        res += 1
    return res

# Exo 2

def func(x,lim_x,y,lim_y,fx,fy, matrix):
    while x != lim_x and y != lim_y:
        if matrix[x,y] == '#': return 1
        elif matrix[x,y] == 'L': return 0
        else:
            x = fx(x)
            y = fy(y)
    return 0

def occupied_closest_seats(x,y,matrix):
    height, width = matrix.shape
    comp = 0
    comp += func(x-1,height,y,width,lambda x: x-1, lambda y: y, matrix)
    comp += func(x+1,height,y,width,lambda x: x+1, lambda y: y, matrix)
    comp += func(x,height,y-1,width,lambda x: x, lambda y: y-1, matrix)
    comp += func(x,height,y+1,width,lambda x: x, lambda y: y+1, matrix)
    comp += func(x-1,height,y-1,width,lambda x: x-1, lambda y: y-1, matrix)
    comp += func(x+1,height,y+1,width,lambda x: x+1, lambda y: y+1, matrix)
    comp += func(x+1,height,y-1,width,lambda x: x+1, lambda y: y-1, matrix)
    comp += func(x-1,height,y+1,width,lambda x: x-1, lambda y: y+1, matrix)
    return comp

def exo2(array):
    height, width = array.shape
    change = True
    res = 0
    while change:
        matrix = numpy.copy(array)
        change = False
        res = 0
        for x in range(height):
            for y in range(width):
                if array[x,y] == 'L' and occupied_closest_seats(x,y,matrix) == 0:
                    array[x,y] = '#'
                    change = True
                if array[x,y] == '#':
                    if occupied_closest_seats(x,y,matrix) >= 5:
                        array[x,y] = 'L'
                        change = True
                    else:
                        res += 1
    return res

# Display

if __name__ == "__main__":
    array = numpy.array([list(item) for item in lines])
    print("EXO 1: {}".format(exo1(array)))
    print("EXO 2: {}".format(exo2(array)))
    pass
