with open('input8.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(instructions, index=0, visited=set()):
    res = 0
    infinite = False
    while (not infinite and index < len(instructions)):
        if index in visited:
            infinite = True
        else:
            visited.add(index)
            infos = instructions[index].split(' ')
            action, value = infos[0], int(infos[1])
            if action == 'acc':
                res += value
                index += 1
            elif action == 'jmp':
                index += value
            else:
                index += 1
    return (not(infinite), res)

# Exo 2

def exo2(instructions):
    index, res = 0, 0
    visited = set()
    while (index < len(lines)):
        infos = instructions[index].split(' ')
        action, value = infos[0], int(infos[1])
        if action == 'acc':
            res += value
            visited.add(index)
            index += 1
        elif action == 'jmp':
            new_instructions = instructions.copy()
            new_instructions[index] = 'nop' + new_instructions[index][3:]
            result = exo1(new_instructions, index, visited.copy())
            if result[0]:
                return res + result[1]
            else:
                visited.add(index)
                index += value
        else:
            new_instructions = instructions.copy()
            new_instructions[index] = 'jmp' + new_instructions[index][3:]
            result = exo1(new_instructions, index, visited.copy())
            if result[0]:
                return res + result[1]
            else:
                visited.add(index)
                index += 1

# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines)[1]))
    print("EXO 2: {}".format(exo2(lines)))
