lines = [13,0,10,12,1,5,8]

def spoken_value(instructions, target):
    result = {}
    for i, instruction in enumerate(instructions):
        result[instruction] = (None, i)
    last = instructions[-1]
    for i in range(len(instructions), target):
        value = None
        if result[last][0] == None:
            value = 0
        else:
            value = result[last][1] - result[last][0]
        if value not in result:
            result[value] = (None, i)
        else:
            result[value] = (result[value][1], i)
        last = value
    return last

# Exo 1

def exo1(instructions):
    return spoken_value(instructions, 2020)

# Exo 2

def exo2(instructions):
    return spoken_value(instructions, 30000000)

# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
