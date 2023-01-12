#Day 10

with open('./10.txt') as my_input:
    lengths_pt1 = list(map(int, my_input.read().split(',')))

def rounds(n, lengths, position, skip):
    for length in lengths:
        sublist, positions = [], []
        for i in range(length):
            p = (i + position) % 256
            sublist.append(num_list[p])
            positions.append(p)
        i = 1
        for p in positions:
            num_list[p] = sublist[-i]
            i += 1
        position = (position + length + skip) % 256
        skip += 1
    n -= 1
    if n:
        rounds(n, lengths, position, skip)

#Part 1

num_list = [i for i in range(256)]

rounds(1, lengths_pt1, 0, 0)

print(num_list[0]*num_list[1])

#Part 2

lengths_pt2 = ''
for char in ''.join(str(length) + ',' for length in lengths_pt1)[:-1]:
    lengths_pt2 += str(ord(char)) + ','
lengths_pt2 += '17,31,73,47,23'

num_list = [i for i in range(256)]

rounds(64, list(map(int, lengths_pt2.split(','))), 0, 0)

knot_hash = ''
element, i = 0, 0
for num in num_list:
    element ^= num
    i += 1
    if not i % 16:
        hs = hex(element)[2:]
        knot_hash = knot_hash + '0' + hs if len(hs) == 1 else knot_hash + hs
        element = 0

print(knot_hash)