#Day 03

with open('./03.txt') as myinput:
    number = myinput.read()

number = int(number)

def sum_neighbors(current_location, locations):
    r = int(current_location.real)
    i = int(current_location.imag)
    neighbors = [v for k, v in locations.items() if r-1 <= int(k.real) <= r+1 and i-1 <= int(k.imag) <= i+1]
    return sum(neighbors)

direction = -1j
location = 0 + 0j
i, j, n = 0, 1, 1
first_larger, value = 0, 1
locations = {}
locations[location] = value
while n < number:
    direction *= 1j
    for k in range(j):
        location += direction
        if not first_larger:
            value = sum_neighbors(location, locations)
            if value > number:
                first_larger = value
            else:
                locations[location] = value
        n += 1
        if n == number:
            break
    if i % 2 == 1:
        j += 1
    i += 1

#Part 1

print(int(abs(location.real) + abs(location.imag)))

#Part 2

print(first_larger)