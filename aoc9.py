with open('input9.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(numbers, previous):
    saves = []
    for i in range(0, previous):
        saves.append([])
        for j in range(i+1, previous):
            saves[-1].append(numbers[i]+numbers[j])
    for i in range(previous, len(numbers)):
        found = False
        j = 0
        while not(found) and j < previous:
            found = numbers[i] in saves[j]
            j += 1
        if not(found):
            return numbers[i]
        else:
            for j in range(1, previous):
                saves[j].append(numbers[i-previous+j]+numbers[i])
            saves.pop(0)
            saves.append([])

# Exo 2

def exo2(numbers, target):
    somme = 0
    index, first_index = 0, 0
    while somme != target and index < len(lines):
        if somme > target:
            somme -= numbers[first_index]
            first_index += 1
        if somme < target:
            somme += numbers[index]
            index += 1
    min_value = numbers[first_index]
    max_value = numbers[first_index]
    for value in numbers[first_index+1:index]:
        if value > max_value:
            max_value = value
        if value < min_value:
            min_value = value
    return min_value + max_value

# Display

if __name__ == "__main__":
    numbers = [int(line) for line in lines]
    result = exo1(numbers, 25)
    print("EXO 1: {}".format(result))
    print("EXO 2: {}".format(exo2(numbers, result)))
