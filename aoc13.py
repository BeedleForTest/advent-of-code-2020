from functools import reduce
with open('input13.txt','r') as file:
    lines = file.read().splitlines()

def clear(bus_ids_string):
    result = {}
    bus_ids = bus_ids_string.split(',')
    for i in range(len(bus_ids)):
        try:
            val = int(bus_ids[i])
            result[i] = val
        except:
            pass
    return result

# Exo 1

def exo1(target, bus_ids):
    res = bus_ids[0]
    final_bus_id = 0
    for index, bus_id in bus_ids.items():
        temp = (bus_id - target % bus_id) % bus_id
        if temp < res:
            res = temp
            final_bus_id = bus_id
    return res * final_bus_id

# Exo 2

def euclid(a, b):  
    r, u, v, r1, u1, v1 = a, 1, 0, b, 0, 1
    while r1 != 0:
        q = int(r/r1)
        r, u, v, r1, u1, v1 = r1, u1, v1, r-q*r1, u-q*u1, v-q*v1
    return r,u,v

def exo2(bus_ids):
    n = reduce(lambda x, y: x * y, bus_ids.values())
    res = 0
    for key, item in bus_ids.items():
        a = item - key % item
        ni_ = int(n/item)
        pgcd,x,y = euclid(item,ni_)
        res += a * y * ni_
    return res % n

# Display

if __name__ == "__main__":
    bus_ids = clear(lines[1])
    print("EXO 1: {}".format(exo1(int(lines[0]), bus_ids)))
    print("EXO 2: {}".format(exo2(bus_ids)))

