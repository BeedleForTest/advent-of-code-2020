import re
with open('input2.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(policies):
    res = 0
    for policy in policies:
        found = re.search('^(\d+)-(\d+)\s([a-z]{1}):\s([a-z]+)', policy)
        min_occ, max_occ, character, password = int(found.group(1)), int(found.group(2)), found.group(3), found.group(4)
        occurences = password.count(character)
        if min_occ <= occurences <= max_occ:
            res += 1
    return res

# Exo 2

def exo2(policies):
    res = 0
    for policy in policies:
        found = re.search('^(\d+)-(\d+)\s([a-z]{1}):\s([a-z]+)', policy)
        x1, x2, character, password = int(found.group(1)), int(found.group(2)), found.group(3), found.group(4)
        if (password[x1-1] == character) != (password[x2-1] == character):
            res += 1
    return res

# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
