with open('input3.txt','r') as file:
    lines = file.read().splitlines()
      
# Exo 1

def exo1(geologies, right, down):
    x,y = 0,0
    res = 0
    width = len(geologies[0])
    while x < len(geologies)-down:
        x,y = x+down, (y+right) % width
        if geologies[x][y] == '#':
            res += 1
    return res

# Exo 2

def exo2(geologies):
    res = 1
    infos = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    for info in infos:
        right, down = info
        res = res * exo1(geologies,right,down)
    return res
    
# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines, 3, 1)))
    print("EXO 2: {}".format(exo2(lines)))

