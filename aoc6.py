with open('input6.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(questions):
    res = 0
    groups = [set()]
    for question in questions:
        if question == '':
            res += len(groups[-1])
            groups.append(set())
        else:
            groups[-1] = groups[-1].union(set(question))
    return res

# Exo 2

def exo2(questions):
    res = 0
    groups = [set('abcdefghijklmnopqrstuvwxyz')]
    for question in questions:
        if question == '':
            res += len(groups[-1])
            groups.append(set('abcdefghijklmnopqrstuvwxyz'))
        else:
            groups[-1] = groups[-1].intersection(set(question))
    return res

# Display

if __name__ == "__main__":
    lines.append('')
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
