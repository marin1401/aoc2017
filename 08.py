#Day 08

with open('./08.txt') as myinput:
    inputlines = myinput.readlines()

registers = {line.split()[0]: 0 for line in inputlines}

instructions = [line.split() for line in inputlines]

def increase_or_decrease(register, do, value):
    registers[register] = registers[register] + value if do == 'inc' else registers[register] - value

def operations(instruction):
    register, do, value, _, register_check, condition, value_check = instruction
    value, value_check = map(int, (value, value_check))
    if condition == '>':
        if registers[register_check] > value_check:
            increase_or_decrease(register, do, value)
    elif condition == '<':
        if registers[register_check] < value_check:
            increase_or_decrease(register, do, value)
    elif condition == '==':
        if registers[register_check] == value_check:
            increase_or_decrease(register, do, value)
    elif condition == '<=':
        if registers[register_check] <= value_check:
            increase_or_decrease(register, do, value)
    elif condition == '>=':
        if registers[register_check] >= value_check:
            increase_or_decrease(register, do, value)
    elif condition == '!=':
        if registers[register_check] != value_check:
            increase_or_decrease(register, do, value)

max_values = set()
for instruction in instructions:
    operations(instruction)
    max_values.add(max(registers.values()))

#Part 1

print(max(registers.values()))

#Part 2

print(max(max_values))