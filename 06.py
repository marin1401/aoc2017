#Day 06

with open('./06.txt') as myinput:
    memory_banks = myinput.read().split()

memory_banks = [int(memory_bank) for memory_bank in memory_banks]

states = set()
counter, seen_state_cycle = 0, 0
while True:
    position = memory_banks.index(max(memory_banks))
    blocks = memory_banks[position]
    memory_banks[position] = 0
    for _ in range(blocks):
        position = 0 if position == len(memory_banks) - 1 else position + 1
        memory_banks[position] += 1
    configuration = tuple(memory_banks)
    if configuration in states:
        if not seen_state_cycle:
            seen_state_cycle = counter + 1
            states = {configuration}
        else:
            counter -= seen_state_cycle - 1
            break
    else:
        states.add(configuration)
    counter += 1

#Part 1

print(seen_state_cycle)

#Part 2

print(counter)
