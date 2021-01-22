#Day 06

with open('./06.txt') as myinput:
    memory_banks = myinput.read().split()

memory_banks = [int(memory_bank) for memory_bank in memory_banks]

configuration = tuple(memory_banks)
states = [configuration]
states_set = {configuration}
counter = 0
while True:
    counter += 1
    position = memory_banks.index(max(memory_banks))
    blocks = memory_banks[position]
    memory_banks[position] = 0
    for _ in range(blocks):
        position += 1
        memory_banks[position % len(memory_banks)] += 1
    configuration = tuple(memory_banks)
    if configuration not in states_set:
        states.append(configuration)
        states_set.add(configuration)
    else:
        #Part 1
        print(counter)
        #Part 2
        print(counter - states.index(configuration))
        break
