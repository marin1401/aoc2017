#Day 07

with open('./07.txt') as myinput:
    inputlines = myinput.read().replace(' (', ', ').replace(')', '').replace(' -> ', ', ').splitlines()

programs = {line.split(', ')[0]: line.split(', ')[1:] for line in inputlines}
programs_bak = {k: v[:] for k, v in programs.items()}

#Part 1

def find_bottom_program(next_program, programs):
    for program, upper_programs in programs.items():
        if next_program in upper_programs:
            return find_bottom_program(program, programs)
    return next_program

first_top_program = next(program for program, upper_programs in programs.items() if len(upper_programs) == 1)

print(find_bottom_program(first_top_program, programs))

#Part 2

while True:
    for program in programs.keys():
        if not all(upper_programs.isdigit() for upper_programs in programs[program]):
            for (i, upper_programs) in enumerate(programs[program][1:]):
                if not upper_programs.isdigit() and all(weight.isdigit() for weight in programs[upper_programs]):
                    programs[program][i+1] = str(sum(int(weight) for weight in programs[upper_programs]))
    if all(all(weight.isdigit() for weight in weights) for weights in programs.values()):
        break

for program, all_weights in programs.items():
    weights = all_weights[1:]
    if len(set(weights)) == 2:
        (_, weight_sum), *_, (_, required_weight_sum) = sorted((weights.count(weight), int(weight)) for weight in weights)
        program_with_wrong_weight = programs_bak[program][weights.index(str(weight_sum)) + 1]
        required_weight = int(programs[program_with_wrong_weight][0]) - (weight_sum - required_weight_sum)
        break

print(required_weight)