with open('input10.txt','r') as file:
    lines = file.read().splitlines()

# Exo 1

def exo1(jolts):
    records = [0,0,0]
    jolts.sort()
    for i in range(len(jolts)-1):
        diff = jolts[i+1] - jolts[i]
        records[diff-1] += 1
    return records[0] * (records[2]+1)

# Exo 2

def rec_possibilities(index, jolts, cache):
    if index <= 0:
        return 1
    elif cache[index] != 0:
        return cache[index]
    else:
        res = 0
        i = 1
        while index-i >= 0 and jolts[index-i] >= jolts[index]-3:
            res += rec_possibilities(index-i, jolts, cache)
            i += 1
        cache[index] = res
        return res
    
def exo2(jolts):
    cache = [0 for i in range(len(jolts))]
    return rec_possibilities(len(jolts)-1, jolts, cache)
    

# Display

if __name__ == "__main__":
    jolts = [int(jolt) for jolt in lines]
    jolts.append(0)
    print("EXO 1: {}".format(exo1(jolts)))
    print("EXO 2: {}".format(exo2(jolts)))
