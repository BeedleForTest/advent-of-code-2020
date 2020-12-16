with open('input12.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(instructions):
    direction = 'E'
    directions = ['N', 'E', 'S', 'W']
    values = {'N': 0, 'E': 0, 'S': 0, 'W': 0}
    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if action == 'F':
            values[direction] += value
        elif action == 'R' or action == 'L':
            coeff = 1 if action == 'R' else -1
            index = (directions.index(direction) + coeff * int(value/90)) % 4
            direction = directions[index]
        else:
            values[action] += value
    return abs(values['E']-values['W'])+abs(values['S']-values['N'])
            
# Exo 2

def exo2(instructions):
    directions = ['N', 'E', 'S', 'W']
    ship = [0,0,0,0]
    waypoint = [1,10,0,0]
    for instruction in instructions:
        action, value = instruction[0], int(instruction[1:])
        if action == 'F':
            for i in range(4):
                ship[i] += waypoint[i] * value
        elif action == 'R':
            nb = int(value/90)
            for i in range(nb):
                waypoint.insert(0, waypoint.pop())
        elif action == 'L':
            nb = int(value/90)
            for i in range(nb):
                waypoint.append(waypoint.pop(0))
        else:
            index = directions.index(action)
            waypoint[index] += value
    return abs(ship[1]-ship[3])+abs(ship[0]-ship[2])

# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
