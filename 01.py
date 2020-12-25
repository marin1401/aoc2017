#Day 01

with open('./01.txt') as myinput:
    sequence = myinput.read()

seq_len = len(sequence)
half_seq_len = seq_len // 2
part1_sequence = sequence[1:] + sequence[0]
part2_sequence = sequence[half_seq_len:] + sequence[:half_seq_len]

def get_sum(sequence, sequence_check):
    digit_sum = 0
    for i in range(len(sequence)):
        if sequence[i] == sequence_check[i]:
            digit_sum += int(sequence[i])
    return digit_sum

#Part 1

print(get_sum(sequence, part1_sequence))

#Part 2

print(get_sum(sequence, part2_sequence))