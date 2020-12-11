import re
with open('input4.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(infos):
    res = 0
    passports = [set()]
    for info in infos:
        if info == '':
            if len(passports[-1]) == 8 or (len(passports[-1]) == 7 and 'cid' not in passports[-1]):
                res += 1
            passports.append(set())
        else:
            items = info.split(' ')
            for item in items:
                key = item.split(':')[0]
                passports[-1].add(key)
    return res

# Exo 2

def is_valid(passport):
    try:
        if ((len(passport["byr"]) == 4 and 1920 <= int(passport["byr"]) <= 2002)
            and (len(passport["iyr"]) == 4 and 2010 <= int(passport["iyr"]) <= 2020)
            and (len(passport["eyr"]) == 4 and 2020 <= int(passport["eyr"]) <= 2030)
            and ((passport["hgt"][-2:] == "cm" and 150 <= int(passport["hgt"][:-2]) <= 193) or (passport["hgt"][-2:] == "in" and 59 <= int(passport["hgt"][:-2]) <= 76))
            and (re.match(r"^#[0-9a-f]{6}$", passport["hcl"]))
            and (passport["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"])
            and (len(passport["pid"]) == 9 and int(passport["pid"]))):
                return True
        return False
    except:
        return False
        

def exo2(infos):
    res = 0
    passports = [{}]
    for info in infos:
        if info == '':
            if (len(passports[-1]) == 8 or (len(passports[-1]) == 7 and 'cid' not in passports[-1])) and is_valid(passports[-1]):
                res += 1
            passports.append({})
        else:
            items = info.split(' ')
            for item in items:
                key_value = item.split(':')
                passports[-1][key_value[0]] = key_value[1]
    return res

# Display

if __name__ == "__main__":
    lines.append('')
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
