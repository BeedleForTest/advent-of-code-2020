import math
with open('input5.txt','r') as file:
    lines = file.read().splitlines()

def calculate_id(sequence):
    rows, columns = sequence[:7], sequence[7:]
    min_x, max_x, min_y, max_y = 0, 127, 0, 7
    for instruction in rows:
        if (instruction == 'B'):
            min_x += math.ceil((max_x - min_x) / 2)
        else:
            max_x = min_x + math.floor((max_x - min_x) / 2)
    for instruction in columns:
        if (instruction == 'L'):
            max_y = min_y + math.floor((max_y - min_y) / 2)
        else:
            min_y += math.ceil((max_y - min_y) / 2)
    return min_x * 8 + min_y

# Exo 1

def exo1(passes):
    res = 0
    for boarding_pass in passes:
        seat = calculate_id(boarding_pass)
        if seat > res:
            res = seat
    return res

# Exo 2

def exo2(passes):
    size = 0
    seats = []
    for boarding_pass in passes:
        seat = calculate_id(boarding_pass)
        # Sorted by insertion
        seats.append(seat)
        index = size
        while index > 0 and seats[index-1] > seat:
            seats[index] = seats[index-1]
            index = index-1
        seats[index] = seat
        size += 1
    for i in range(1,len(seats)):
        if seats[i] != seats[i-1]+1 and seats[i+1] == seats[i]+1:
            return seats[i]-1
    return None


# Display

if __name__ == "__main__":
    print("EXO 1: {}".format(exo1(lines)))
    print("EXO 2: {}".format(exo2(lines)))
    

