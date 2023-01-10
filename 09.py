#Day 09

with open('./09.txt') as my_input:
    stream = my_input.read()

garbage, exclamation = False, False
level, score, garbage_size = 0, 0, 0
for char in stream:
    if exclamation:
        exclamation = False
    elif char == '!':
        exclamation = True
    elif garbage:
        garbage = False if char == '>' else True
        if garbage:
            garbage_size += 1
    else:
        if char == '<':
            garbage = True
        elif char == '{':
            level += 1
            score += level
        elif char == '}':
            level -= 1

#Part 1

print(score)

#Part 2

print(garbage_size)