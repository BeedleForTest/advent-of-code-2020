with open('input7.txt','r') as file:
    lines = file.read().splitlines()

def parse_rule(rule):
    result = {
        'children': {}
    }
    parent_and_children = rule.split(' bags contain ')
    parent = parent_and_children[0]
    result['parent'] = parent
    children_list = parent_and_children[1].split(', ')
    for child_raw in children_list:
        try:
            child_infos = child_raw.split(' ')
            child_name =  ' '.join(child_infos[1:-1])
            child_number = int(child_infos[0])
            result['children'][child_name] = child_number
        except:
            pass
    return result

# Exo 1

def exo1(rules):
    parents_map = {}
    for rule in rules:
        result = parse_rule(rule)
        for child in result['children']:
            if child in parents_map:
                parents_map[child].append(result['parent'])
            else:
                parents_map[child] = [result['parent']]
    results = set()
    start = parents_map["shiny gold"]
    while len(start) > 0:
        parent = start.pop()
        results.add(parent)
        if parent in parents_map:
            start += parents_map[parent]
    return len(results)

# Exo 2

def weight_rec(bag, children):
    if not bag in children:
        return 1
    else:
        somme = 0
        for key, value in children[bag].items():
            somme += value * (1+weight_rec(key, children))
        return somme

def exo2(rules):
    children_map = {}
    for rule in rules:
        result = parse_rule(rule)
        if not result['parent'] in children_map:
            children_map[result['parent']] = {}
        for child in result['children']:
            children_map[result['parent']][child] = result['children'][child]
    return weight_rec("shiny gold", children_map)

# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
