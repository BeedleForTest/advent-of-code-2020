with open('input1.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(liste, value):
    store = set()
    for element in liste:
        if value-element in store:
            return element * (value-element)
        else:
            store.add(element)
    return None

# Exo 2

def exo2(liste, value):
    targets = [value-element for element in liste]
    for target in targets:
        res = exo1(liste, target)
        if res:
            return res * (value-target)
    return None

# Display

if __name__ == "__main__":
    valeurs = [int(line) for line in lines]
    print("EXO 1: {}".format(exo1(valeurs, 2020)))
    print("EXO 2: {}".format(exo2(valeurs, 2020)))
