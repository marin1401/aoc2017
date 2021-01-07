#Day 05

with open('./05.txt') as myinput:
    inputlines = myinput.readlines()

jump_offsets = [int(i) for i in inputlines]

def find_steps(jump_offsets, part_two):
    jumps = jump_offsets.copy()
    i, steps = 0, 0
    while i in range(len(jumps)):
        j = i
        i += jumps[j]
        if jumps[j] > 2 and part_two:
            jumps[j] -= 1
        else:
            jumps[j] += 1
        steps += 1
    return steps

#Part 1

print(find_steps(jump_offsets, False))

#Part 2

print(find_steps(jump_offsets, True))