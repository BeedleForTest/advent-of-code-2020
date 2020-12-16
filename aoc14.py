import re, itertools
from functools import reduce
with open('input14.txt','r') as file:
    lines = file.read().splitlines()

def add_mask(val, mask):
    temp = "{:b}".format(val)
    base2 = ['0' for i in range(len(mask) - len(temp))] + list(temp)
    for i, value in enumerate(mask):
        if value != 'X':
            base2[i] = value
    return int(''.join(base2), 2)

def add_mask2(val, mask):
    temp = "{:b}".format(val)
    base2 = ['0' for i in range(len(mask) - len(temp))] + list(temp)
    nb_unknown = 0
    results = [base2]
    for i, value in enumerate(mask):
        if value == '1':
            for res in results:
                res[i] = value
        elif value == 'X':
            new = []
            for res in results:
                copy0 = res.copy()
                copy0[i] = '0'
                copy1 = res.copy()
                copy1[i] = '1'
                new += [copy0, copy1]
            results = new
    return map(lambda x: int(''.join(x), 2), results)

# Exo 1

def exo1(instructions):
    mask = None
    records = {}
    for instruction in instructions:
        if instruction[:4] == 'mask':
            mask = re.search('[01X]+', instruction).group(0)
        else:
            found = re.search('^mem\[([0-9]+)\]\s=\s([0-9]+)', instruction)
            index = int(found.group(1))
            value = int(found.group(2))
            new_value = add_mask(value,mask)
            records[index] = new_value
    return reduce(lambda x, y: x + y, records.values())

# Exo 2

def exo2(instructions):
    mask = None
    records = {}
    for instruction in instructions:
        if instruction[:4] == 'mask':
            mask = re.search('[01X]+', instruction).group(0)
        else:
            found = re.search('^mem\[([0-9]+)\]\s=\s([0-9]+)', instruction)
            index = int(found.group(1))
            value = int(found.group(2))
            new_indexes = add_mask2(index,mask)
            for new_index in new_indexes:
                records[new_index] = value
    return reduce(lambda x, y: x + y, records.values())

# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
